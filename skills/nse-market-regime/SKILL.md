---
name: nse-market-regime
description: Assess the Indian equity market regime (Nifty 50, Nifty Next 50, Nifty Midcap/Smallcap, Bank Nifty, India VIX, breadth) and output a posture such as risk-on, selective or defensive with an exposure ceiling. Use for "how is the Indian market", "Nifty outlook", or daily/weekly market briefs.
---

# NSE Market Regime

## Inputs (fetch fresh; never rely on memory)
- Index levels vs 20/50/200 DMA: Nifty 50, Bank Nifty, Nifty Midcap 150, Nifty Smallcap 250.
- India VIX level and 5-day change.
- Breadth: % of Nifty 500 above 50 DMA and 200 DMA, advance/decline, 52-week highs vs lows (NSE bhavcopy or a screener export).
- Flows: see `fii-dii-flow-tracker`.
- Macro: USD/INR, 10Y G-Sec yield, Brent crude, RBI policy stance, GIFT Nifty for the open.

## Scoring (0-100, equal weights, state the sub-scores)
1. Trend: Nifty above 50 and 200 DMA, 50 DMA above 200 DMA, slope of 50 DMA.
2. Breadth: Nifty 500 % above 200 DMA (>60 healthy, <40 weak).
3. Volatility: India VIX <14 calm, 14-20 normal, >20 stressed.
4. Leadership: midcap/smallcap relative strength vs Nifty over 3 months.
5. Flows: 10-day net FII + DII trend.

## Output
- Regime label: Risk-on (>=70), Selective (45-69), Defensive (<45).
- Suggested max equity exposure band, key levels (support/resistance), the 2-3 events to watch (RBI, US Fed, results season, Union Budget, monthly expiry).
- Include data timestamps and sources. Mark any missing input and re-weight rather than guessing.

Educational use only; not investment advice.
