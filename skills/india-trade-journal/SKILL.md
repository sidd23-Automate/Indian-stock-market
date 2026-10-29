---
name: india-trade-journal
description: Log and review Indian-market trades (equity, F&O) with process-adherence scoring, net P&L after charges, and tax-bucket tagging (intraday speculative, F&O non-speculative business income, STCG, LTCG). Use for trade reviews, weekly digests and post-mortems.
---

# India Trade Journal

## Entry schema (CSV/YAML, one row per trade)
date, symbol, segment (EQ/FUT/OPT), side, qty, entry, exit, stop, target, setup, charges, thesis, regime at entry, followed_plan (Y/N), notes.

## Review workflow
1. Compute gross and net P&L (after brokerage, STT, exchange fees, GST, stamp), R-multiple, hit rate, average win/loss, max drawdown.
2. Score process: planned stop respected, size within risk %, setup matched thesis, no revenge trades after a loss.
3. Tag tax bucket for the user's reference only: intraday equity = speculative business income; F&O = non-speculative business income; delivery equity = STCG (held under 12 months) or LTCG. Rates and exemptions change; tell the user to confirm with a CA.
4. Weekly digest: best/worst trade, rule breaks, one process change for next week.

Not tax or investment advice.
