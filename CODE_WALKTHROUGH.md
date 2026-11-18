# TenderScope – Code Walkthrough (for explaining to your teacher)

**One-line summary:** TenderScope is a Streamlit web app that loads tender records (synthetic demo data or an uploaded CSV/Excel), cleans them, and applies web/data-mining techniques to find patterns.

## Data flow
Upload / sample CSV -> `preprocessing/cleaning.py` -> clean DataFrame -> `mining/analytics.py` algorithms -> charts/tables in `app.py` -> export (CSV / Excel / PDF) or save to SQLite.

## File-by-file
| File | Purpose |
|---|---|
| `app.py` | Main Streamlit UI: sidebar with 13 pages (Overview, Data Collection, Preprocessing, Demand Analytics, Trend Analysis, Association Rules, Similarity, Clustering, Tender Search, Value Analysis, Reports, Evaluation, About). |
| `config.py` | File paths and the required column list (`FIELDS`). |
| `ui_theme.py` | Custom CSS styling. |
| `preprocessing/cleaning.py` | `preprocess()`: validation, duplicate removal, missing values, date parsing, money parsing (lakh/crore), stop-word removal + Porter stemming. |
| `mining/analytics.py` | The algorithms (below). |
| `database/db.py`, `init_db.py` | SQLite storage (tenders, import log). |
| `collectors/` | CSV/Excel reading; BeautifulSoup HTML parser demo. |
| `utils/exports.py` | Excel (openpyxl) and PDF (reportlab) export. |
| `generate_realistic_sample.py` | Creates the 850 synthetic tenders. |
| `tests/test_core.py` | 9 pytest tests. |
| `data/sample/synthetic_tenders.csv` | Demo dataset (fake, clearly labelled). |
| `docs/` | Project report, methodology, viva questions. |

## Algorithms (in `mining/analytics.py`)
1. **Keyword counts** – CountVectorizer (bag of words, 1–2 word phrases).
2. **Search** – TF-IDF vectors + cosine similarity ranks tenders against a query.
3. **Similar tenders** – cosine similarity between a chosen tender and all others.
4. **Clustering** – K-Means on TF-IDF; quality shown by inertia and silhouette score.
5. **Association rules** – Apriori (mlxtend) on "baskets" of product terms; metrics: support, confidence, lift.
6. **Trends** – tenders grouped by publish month/quarter/year.

## Key viva points
- Data is **synthetic**; the app does not scrape live government portals (ethical/legal reason).
- Lift > 1 means terms co-occur more than chance, not causation.
- Estimated values are published estimates, not awarded contract values.
- Preprocessing is needed so text algorithms work on consistent, stemmed words.

## Run
```
pip install -r requirements.txt
python -m database.init_db
python -m pytest -q
streamlit run app.py
```
