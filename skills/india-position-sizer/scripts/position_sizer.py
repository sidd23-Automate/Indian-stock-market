#!/usr/bin/env python3
"""Risk-based position sizer for NSE/BSE cash equities (INR).

Example:
  python position_sizer.py --capital 1000000 --risk-pct 1 --entry 1250 --stop 1195 --target 1400
"""
import argparse
import json
import math
import sys

# Illustrative defaults for cash equity. Rates change: verify against the
# exchange/SEBI/broker schedule and override with --charges-file.
DEFAULT_CHARGES = {
    "delivery": {"stt_buy": 0.001, "stt_sell": 0.001, "brokerage_pct": 0.0},
    "intraday": {"stt_buy": 0.0, "stt_sell": 0.00025, "brokerage_pct": 0.0003},
    "exchange_txn_pct": 0.0000307,
    "sebi_pct": 0.000001,
    "stamp_buy_delivery": 0.00015,
    "stamp_buy_intraday": 0.00003,
    "gst_pct": 0.18,
}


def round_tick(price, tick=0.05):
    return round(round(price / tick) * tick, 2)


def side_cost(value, side, mode, c):
    m = c[mode]
    stt = value * (m["stt_buy"] if side == "buy" else m["stt_sell"])
    brokerage = value * m["brokerage_pct"]
    txn = value * c["exchange_txn_pct"]
    sebi = value * c["sebi_pct"]
    gst = (brokerage + txn + sebi) * c["gst_pct"]
    stamp = 0.0
    if side == "buy":
        stamp = value * (c["stamp_buy_delivery"] if mode == "delivery" else c["stamp_buy_intraday"])
    return stt + brokerage + txn + sebi + gst + stamp


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--capital", type=float, required=True, help="Trading capital in INR")
    p.add_argument("--risk-pct", type=float, default=1.0, help="Percent of capital risked per trade")
    p.add_argument("--entry", type=float, required=True)
    p.add_argument("--stop", type=float, required=True)
    p.add_argument("--target", type=float)
    p.add_argument("--mode", choices=["delivery", "intraday"], default="delivery")
    p.add_argument("--short", action="store_true", help="Short (intraday only)")
    p.add_argument("--max-position-pct", type=float, default=25.0, help="Cap on position size as %% of capital")
    p.add_argument("--tick", type=float, default=0.05)
    p.add_argument("--charges-file", help="JSON file overriding default charge rates")
    a = p.parse_args()

    if a.short and a.mode != "intraday":
        sys.exit("Shorting cash equities is intraday only in India.")
    if (a.stop >= a.entry) == (not a.short):
        sys.exit("Stop must be below entry for longs and above entry for shorts.")

    charges = DEFAULT_CHARGES
    if a.charges_file:
        with open(a.charges_file) as f:
            charges = json.load(f)

    entry, stop = round_tick(a.entry, a.tick), round_tick(a.stop, a.tick)
    risk_budget = a.capital * a.risk_pct / 100
    per_share = abs(entry - stop)
    qty_risk = math.floor(risk_budget / per_share)
    qty_cap = math.floor(a.capital * a.max_position_pct / 100 / entry)
    qty = max(min(qty_risk, qty_cap), 0)

    out = {
        "entry": entry, "stop": stop, "quantity": qty,
        "position_value": round(qty * entry, 2),
        "position_pct_of_capital": round(qty * entry / a.capital * 100, 2),
        "risk_per_share": round(per_share, 2),
        "planned_risk_inr": round(qty * per_share, 2),
        "limited_by": "position cap" if qty_cap < qty_risk else "risk budget",
    }

    buy, sell = (stop, entry) if a.short else (entry, None)
    if a.short:
        sell_val, buy_val = qty * entry, qty * stop
    else:
        buy_val, sell_val = qty * entry, qty * stop
    out["stop_out_charges_inr"] = round(side_cost(buy_val, "buy", a.mode, charges) + side_cost(sell_val, "sell", a.mode, charges), 2)
    out["risk_incl_charges_inr"] = round(out["planned_risk_inr"] + out["stop_out_charges_inr"], 2)

    if a.target:
        tgt = round_tick(a.target, a.tick)
        gain = abs(tgt - entry) * qty
        tb, ts = (qty * tgt, qty * entry) if a.short else (qty * entry, qty * tgt)
        cost = side_cost(tb, "buy", a.mode, charges) + side_cost(ts, "sell", a.mode, charges)
        out["target"] = tgt
        out["reward_risk"] = round(abs(tgt - entry) / per_share, 2)
        out["net_gain_at_target_inr"] = round(gain - cost, 2)

    print(json.dumps(out, indent=2))
    print("\nCharges use illustrative rates (excl. DP charges and taxes on gains); verify before relying on them.", file=sys.stderr)


if __name__ == "__main__":
    main()
