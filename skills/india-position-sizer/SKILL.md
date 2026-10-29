---
name: india-position-sizer
description: Size NSE/BSE cash-equity trades in INR by risk per trade, with tick-size rounding, position caps and estimated STT/brokerage/GST/stamp charges. Use when the user asks "how many shares", "position size", or "risk per trade" for an Indian stock.
---

# India Position Sizer

## Workflow
1. Collect: capital (INR), risk % (default 1), entry, stop, optional target, mode (`delivery` or `intraday`).
2. Run `python scripts/position_sizer.py --capital <C> --risk-pct <R> --entry <E> --stop <S> [--target <T>] [--mode intraday] [--short]`.
3. Report quantity, position value, % of capital, planned risk, risk including charges, reward:risk and net gain at target.
4. Flag when the position cap (default 25% of capital) limits size instead of the risk budget.

## India-specific rules
- Price tick is Rs 0.05 for most equities; the script rounds to it.
- Shorting cash equities is intraday only; delivery is long only.
- Circuit limits (5/10/20%) and T2 / ASM / GSM stage restrictions can make a stop unexecutable; mention them for volatile small caps.
- Charge rates in the script are illustrative defaults. Pass `--charges-file` to override, and tell the user to verify against their broker's current schedule.
- Never present output as advice; it is arithmetic on the user's own inputs.
