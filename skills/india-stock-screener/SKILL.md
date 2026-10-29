---
name: india-stock-screener
description: Screen Indian stocks using momentum (Minervini-style trend template, VCP), CANSLIM-style growth, and quality/value filters with India-specific liquidity and governance checks. Use for "find breakout stocks in NSE" or "screen Nifty 500 for quality".
---

# India Stock Screener

## Universe and liquidity
- Default universe: Nifty 500. Exclude stocks in ASM/GSM frameworks, under 20-day average traded value of Rs 5 crore, or with promoter pledge above 25%.

## Screens
**Trend template (momentum)**: price above 150 and 200 DMA; 150 above 200 DMA; 200 DMA rising 1 month+; price within 25% of 52-week high and 30%+ above 52-week low; RS rank vs Nifty 500 in top 30%.

**VCP**: two or more progressively tighter pullbacks, volume dry-up in the final contraction, pivot at the contraction high. Output pivot, stop (below last contraction low) and size via `india-position-sizer`.

**Growth (CANSLIM-style)**: latest quarter EPS and sales YoY growth >= 20-25%, 3-year EPS CAGR >= 20%, ROE >= 15%, rising institutional (FII+DII+MF) holding.

**Quality/value**: ROCE >= 15%, debt/equity < 1 (non-financials), interest cover > 3, 5-year sales CAGR >= 10%, P/E below sector median or PEG < 1.5, promoter holding stable or rising.

## Data sources
Screener.in exports (user's own login), NSE bhavcopy, yfinance (`.NS` / `.BO` suffix), company filings on BSE/NSE. State which source and as-of date were used; flag any figure that could not be verified.

## Output
Ranked table with ticker, price, trigger/pivot, stop, RS rank, key fundamentals, and one-line risk note. Educational only.
