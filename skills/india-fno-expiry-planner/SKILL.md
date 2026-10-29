---
name: india-fno-expiry-planner
description: Plan around NSE/BSE F&O expiries, lot sizes, margin and event risk for Nifty, Bank Nifty and stock derivatives. Use for expiry-day questions, option-chain reading (PCR, max pain, OI build-up) and lot-based sizing.
---

# India F&O Expiry Planner

## Always verify (rules change often)
Expiry weekdays, which indices have weekly contracts, lot sizes, and STT on derivatives have all been revised by SEBI/NSE/BSE and the Union Budget. Fetch the current NSE circular or contract specification page before stating any of them. Do not quote these from memory.

## Workflow
1. Identify the underlying and fetch the current lot size, expiry list and tick size from NSE.
2. Read the option chain: PCR, highest call/put OI strikes (resistance/support), OI change, India VIX and implied move to expiry.
3. Compute lot-based sizing: max loss = (entry - stop) x lot size x lots; keep within the user's per-trade risk %.
4. For option buyers show breakeven, theta decay per day and days to expiry; for sellers show margin required (use the broker margin calculator figure) and worst-case loss.
5. List event risks before expiry: RBI policy, US Fed, results from index heavyweights, budget, global cues via GIFT Nifty.

## Guardrails
- F&O carries high loss rates for retail traders per SEBI studies; state this once, briefly.
- Never recommend naked option selling without a defined hedge unless the user explicitly describes their experience and margin buffer.
