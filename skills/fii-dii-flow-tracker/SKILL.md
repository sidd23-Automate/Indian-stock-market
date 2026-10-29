---
name: fii-dii-flow-tracker
description: Track FII/FPI and DII cash-market flows, FII index-futures positioning and participant-wise open interest for India. Use when asked about foreign or domestic institutional buying/selling, or flow-driven market moves.
---

# FII / DII Flow Tracker

## Data sources (fetch live)
- NSE daily FII/DII provisional cash activity (nseindia.com market data).
- NSE participant-wise open interest and volume (F&O archives).
- NSDL FPI monthly/fortnightly sector-wise investment data.

## Workflow
1. Pull the latest 20 trading days of net FII and DII cash flows (Rs crore).
2. Compute 5-, 10- and 20-day rolling nets and whether FII selling is being absorbed by DII.
3. From participant OI, compute FII index-futures long/short ratio and its 5-day change.
4. Classify: Aligned inflow, Domestic absorption, Aligned outflow, or Mixed.
5. Add NSDL sector tilt (which sectors FPIs are adding or cutting) if monthly data is available.

## Caveats
- NSE daily numbers are provisional and revised; cite the date.
- Flows lag price and are not a standalone signal; pair with `nse-market-regime`.
