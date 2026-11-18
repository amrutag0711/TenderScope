## Dataset Description
The bundled file data/sample/synthetic_tenders.csv contains 720 generated rows, 20 columns, 12 named states, 8 product categories, 7 fictional organization labels, publishing/closing dates and hypothetical INR estimates. Every thirteenth row has an absent estimated value. All source_portal values read SYNTHETIC DEMO, and source_url is empty. No row represents a real tender. Required import fields are tender_id and tender_title; missing optional fields are inserted as nulls.

## System Architecture
Data source (synthetic CSV or user-imported CSV/XLSX) -> schema validation -> pandas preprocessing -> current dataset in session -> analytics (frequency, trend, association, similarity, clustering, search) -> Plotly/Streamlit presentation -> CSV/XLSX/PDF exports. SQLite/SQLAlchemy stores explicitly imported records. Modules are organized in preprocessing/, mining/, database/, collectors/ and utils/.

## Methodology
The system loads records, validates required columns, removes duplicate source-and-ID pairs, standardizes text, parses dates, converts INR amounts and creates cleaned descriptions. Keyword counts use a count vectorizer; retrieval uses TF-IDF; similarity uses cosine distance; co-occurrence uses a binary term basket; clustering uses K-Means. All summaries use the active dataset.

## Data Collection
Automated extraction from CPPP or GeM is intentionally not claimed. The project provides manual public CSV/Excel import and a local BeautifulSoup HTML table parsing example. A future collector must check portal terms and robots.txt, avoid CAPTCHA/authentication bypass, respect rate limits, and retain provenance. Official portals: https://eprocure.gov.in/eprocure/app and https://bidplus.gem.gov.in/.

## Data Preprocessing
The code enforces tender_id and tender_title, inserts missing optional columns, removes duplicate (source_portal,tender_id) records, normalizes categories and organizations by trimming blanks, parses dates, converts monetary strings including lakh/crore, and stems non-stopword tokens using PorterStemmer. Null estimated values remain missing rather than becoming zero. The original imported DataFrame is retained in session for before/after inspection.

## Algorithms Used
TF-IDF(t,d) = TF(t,d) × IDF(t): highlights terms informative for a document.
Cosine(A,B) = (A·B)/(||A|| ||B||): measures similarity between vectorized descriptions.
Support(X) = count(transactions containing X)/N.
Confidence(X→Y) = Support(X∪Y)/Support(X).
Lift(X→Y) = Confidence(X→Y)/Support(Y).
Apriori enumerates frequent itemsets from multiple product terms per tender.
K-Means assigns vectors to the nearest of K centroids, minimizing within-cluster squared distance (inertia). A silhouette score summarizes separation when defined. None of these methods proves completed procurement or causal relationships.

## Implementation
Python modules include app.py (13 navigable views), preprocessing/cleaning.py, mining/analytics.py, database/db.py, collectors/local_html.py and utils/exports.py. The dashboard includes import, preprocessing comparison, frequency plots, time trends, association thresholds, similar-tender ranking, clustering, search filters, value analysis, exports, evaluation and methodology. See README.md for Windows PowerShell commands and tests/test_core.py for automated checks.