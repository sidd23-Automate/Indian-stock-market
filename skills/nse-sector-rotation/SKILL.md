---
name: nse-sector-rotation
description: Rank NSE sectoral indices (Bank, IT, Auto, FMCG, Pharma, Metal, Realty, Energy, PSU Bank, Financial Services, Infra, Consumption) by relative strength and momentum to show sector rotation. Use for "which sectors are leading" in India.
---

# NSE Sector Rotation

## Workflow
1. Fetch closing prices for the Nifty sectoral indices and Nifty 50 (benchmark) for 1 year.
2. For each sector compute: relative strength vs Nifty (sector / Nifty ratio), RS change over 1, 3 and 6 months, % above 50 DMA, and distance from 52-week high.
3. Place each sector in a quadrant (RRG-style):
   - Leading: RS above its 50 DMA and rising
   - Weakening: RS above but falling
   - Lagging: RS below and falling
   - Improving: RS below but rising
4. Output a ranked table, the top 3 leaders and improving sectors, and 2-3 liquid constituents per leading sector to feed `india-stock-screener`.

## Notes
- Banks and financials dominate Nifty weight; call that out when explaining relative moves.
- Check sector-specific drivers: RBI rates (banks, realty), USD/INR (IT, pharma), commodity prices (metals, energy), monsoon and rural demand (FMCG, auto).
