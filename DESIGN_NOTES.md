# TenderScope Intelligence Studio — Design Notes

This edition replaces the generic navy dashboard with a custom editorial identity: forest graphite, parchment, terracotta coral and sage, with Space Grotesk headlines and DM Sans interface text.

## What changed
- `ui_theme.py`: new bespoke theme, card geometry, controls, sidebar and typography.
- `app.py`: branded header and revised Plotly chart palette.
- Data-mining and database logic are unchanged.

## Run
`streamlit run app.py`

Fonts are loaded from Google Fonts when available; local system fonts are used as fallback. No AI API is needed. This is an AI-assisted visual redesign, not an AI prediction model.
