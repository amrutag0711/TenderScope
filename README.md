# TenderScope

Government Tender Pattern Mining and Demand Intelligence System Using Web Mining.

**Data warning:** The bundled 720 records are entirely SYNTHETIC. They are not government tenders, and the app does not claim live portal extraction.

## Quick start (Linux / macOS)

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -m database.init_db
python -m pytest -q
streamlit run app.py
```

Python 3.11+ is supported (tested on 3.12). No API keys or credentials are required.

## Windows PowerShell quick start

1. Install Python 3.11 or newer from python.org and check `py --version`.
2. Extract the ZIP and open PowerShell in the `TenderScope` folder.
3. Run:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m database.init_db
python -m pytest -q
streamlit run app.py
```

If PowerShell blocks activation, use `venv\Scripts\python.exe -m pip install -r requirements.txt` and `venv\Scripts\python.exe -m streamlit run app.py` instead. For Command Prompt, activation is `venv\Scripts\activate.bat`. Stop the server with Ctrl+C; deactivate with `deactivate`.

## Demonstration

Open http://localhost:8501. Explore Overview, Demand Analytics, Trend Analysis, Association Rules, Similarity, Clustering, Tender Search and Reports. Upload CSV or XLSX from Data Collection to replace the synthetic dataset in the current session. The SQLite import is saved only after clicking Use uploaded dataset. The CSV template is downloadable from the same page.

## Troubleshooting

- `streamlit` not recognized: activate the virtual environment or run `python -m streamlit run app.py`.
- Module missing: run `python -m pip install -r requirements.txt` in the active environment.
- Empty association rules: reduce support/confidence thresholds.
- Invalid upload: include `tender_id` and `tender_title` headers.
- Date parsing issue: use ISO `YYYY-MM-DD` where possible.
- Run tests from the project root: `python -m pytest -q`.

## Data and ethics

The local HTML parser demonstrates BeautifulSoup without fetching a live site. For real records, download only publicly permitted exports from official portals and import them; obey terms, robots.txt and privacy rules. No CAPTCHA bypass, authentication bypass, or personal contact collection. Synthetic rows have empty source URLs and `SYNTHETIC DEMO` as source portal. Published estimates are not awarded values.

## Project structure

`app.py` UI, `preprocessing/` normalization, `mining/` algorithms, `database/` SQLite, `collectors/` local HTML and CSV, `utils/` exports, `tests/` automated tests, `docs/` academic material, `data/sample/` synthetic dataset.


## Updated November 2026 edition
- Refreshed dark-navy Streamlit styling with readable KPI cards.
- 850 varied, clearly labelled synthetic tender records; regenerate with `python generate_realistic_sample.py`.
- Horizontal charts with appropriate axis labels; positive lift rules highlighted; similarity percentages.
- Data are synthetic and cannot establish actual government demand or open tender availability.
- Start with `python -m database.init_db` and `streamlit run app.py`.
- Run `python -m pytest -q` to check automated tests.
- If the dashboard was already running, stop it with Ctrl+C, restart it, and use **Data Collection → Reset to synthetic sample**.


## Configuration
- `TENDERSCOPE_DB` (optional): path of the SQLite file; default `data/tenders.sqlite` (created automatically).
- `.streamlit/config.toml`: 50 MB upload limit, XSRF protection, telemetry off.
