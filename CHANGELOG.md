# Changelog

## Fixed / improved
- Database: missing values and dates now saved as JSON null/ISO (previously `<NA>`/`NaT` strings corrupted reloaded records); batched upsert; optional `TENDERSCOPE_DB` path override.
- Upload: CSV encoding fallback (UTF-8 -> latin-1); loading saved SQLite records now refreshes the Preprocessing view.
- Performance: association rules, clustering and keyword counts cached across Streamlit reruns.
- Compatibility: replaced deprecated `use_container_width` with `width='stretch'`; Streamlit minimum raised to 1.50.
- Security: Excel export neutralises formula-injection cells; upload size limit and XSRF protection in `.streamlit/config.toml`.
- Packaging: removed bundled `venv/`, caches and generated SQLite file; `.gitignore` updated; README gained Linux/macOS steps.
- Tests: 6 -> 9 (DB round-trip/upsert, encoding fallback, export sanitising).
- Readability: all source files reformatted to standard multi-line Python with docstrings; added CODE_WALKTHROUGH.md.

## Validation
`pytest`: 9 passed. All 13 app pages rendered headlessly via Streamlit AppTest with no exceptions (Python 3.12, Streamlit 1.67). Not tested: Windows, live browser rendering, Google Fonts loading.
