# claude-trading-skills-india

A set of Claude skills for Indian equity and derivatives markets — modelled on
[tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)
and extending it with India-specific workflows for NSE/BSE.

> **Not investment advice.** All skills produce educational analysis based on
> publicly available data. Verify figures before acting on them.

---

## Skills

| Skill | Purpose |
|---|---|
| [nse-market-regime](skills/nse-market-regime/SKILL.md) | Score the Indian market regime (risk-on / selective / defensive) from Nifty, India VIX and breadth |
| [fii-dii-flow-tracker](skills/fii-dii-flow-tracker/SKILL.md) | Track FII/FPI and DII cash & F&O flows and classify absorption/outflow patterns |
| [nse-sector-rotation](skills/nse-sector-rotation/SKILL.md) | RRG-style quadrant map of Nifty sectoral indices |
| [india-stock-screener](skills/india-stock-screener/SKILL.md) | Trend template, VCP, CANSLIM and quality screens for Nifty 500 |
| [india-fno-expiry-planner](skills/india-fno-expiry-planner/SKILL.md) | Option-chain reading (PCR, max pain, OI), lot sizing and expiry-day event risk |
| [india-position-sizer](skills/india-position-sizer/SKILL.md) | INR risk-based sizing with STT/brokerage/GST/stamp charges |
| [india-trade-journal](skills/india-trade-journal/SKILL.md) | Log and review trades; R-multiple, process score, tax-bucket tagging |

---

## Quick-start (no API required)

1. Install the three zero-API skills first:

```
nse-market-regime   →  feed it an NSE bhavcopy CSV or a screenshot
india-position-sizer →  run scripts/position_sizer.py locally (Python 3.8+)
india-trade-journal  →  paste a CSV of your trades
```

2. Add `fii-dii-flow-tracker` next — NSE publishes its FII/DII report daily for free.

3. `india-stock-screener` and `nse-sector-rotation` pair well with a
   [Screener.in](https://www.screener.in) export (free account) or
   yfinance (`pip install yfinance`; append `.NS` or `.BO` to NSE/BSE tickers).

---

## Suggested starter workflow

```
nse-market-regime
  → regime label + exposure ceiling
fii-dii-flow-tracker
  → flow context: absorption or selling pressure
nse-sector-rotation
  → leading and improving sectors
india-stock-screener
  → candidate list from leading sectors
india-fno-expiry-planner   (if options)
india-position-sizer       (size the trade)
india-trade-journal        (log and review)
```

---

## Installing in Claude Code

```bash
git clone https://github.com/<your-username>/claude-trading-skills-india
# Personal install (available in every project)
cp -r skills/* ~/.claude/skills/
# Project install
cp -r skills/* /path/to/your/project/.claude/skills/
```

Claude Code detects skills automatically.

For the Claude web app, build a `.skill` package per skill or follow the
packaging guide in the parent repo.

---

## Data sources

| Source | Free | Used by |
|---|---|---|
| NSE bhavcopy / daily FII report | ✅ | nse-market-regime, fii-dii-flow-tracker |
| NSE F&O participant OI (CSV) | ✅ | fii-dii-flow-tracker, india-fno-expiry-planner |
| NSE option chain page | ✅ | india-fno-expiry-planner |
| yfinance (`.NS` / `.BO`) | ✅ | india-stock-screener, nse-sector-rotation |
| Screener.in export | ✅ free tier | india-stock-screener |
| NSDL FPI sector data | ✅ | fii-dii-flow-tracker |

---

## Relationship to tradermonty/claude-trading-skills

These skills are India-specific companions. They follow the same
`SKILL.md` + optional `scripts/` layout and are designed to work alongside the
parent repo's universal skills (position-sizer, trade-journal, canslim-screener,
technical-analyst, etc.) when you also have the US-market skills installed.

---

## License

MIT. Educational use. Not financial advice. Charges, regulations and exchange rules
change frequently — always verify from the current NSE/BSE circular before use.
