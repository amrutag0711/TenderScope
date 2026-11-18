# TenderScope | Academic Project Report

## Title Page

TENDERSCOPE
Government Tender Pattern Mining and Demand Intelligence System Using Web Mining
Web Data Mining Laboratory Mini-Project
Submitted by: [Student Name] | Roll No.: [Roll Number]
Department of Electronics Engineering | [Institute Name]
Academic Year: [Academic Year]

## Certificate

[Insert official institute certificate format, signatures, guide name, department seal and date.]

## Declaration

I declare that the submitted software implementation and report are my own work, with tools and sources acknowledged. The bundled tender records are synthetic demonstration data, not genuine government procurement records.
Signature: __________ Date: __________

## Acknowledgement

I express my gratitude to my project guide, department faculty, and laboratory staff for guidance in understanding web data mining, information retrieval, and applied data analysis. I acknowledge the open-source software libraries and official procurement portals referenced in this project.

## Abstract

TenderScope is a Python-based exploratory procurement analytics application that transforms structured tender listings into searchable patterns. It supports CSV/Excel import, cleaning, keyword frequency analysis, time and regional summaries, Apriori association mining, TF-IDF cosine similarity, K-Means clustering, estimated value exploration and interactive Streamlit charts. A 720-record fully synthetic dataset enables a reproducible demonstration without claiming government data access. The platform distinguishes listing frequency from actual procurement, and estimated values from awarded contracts. The project demonstrates an end-to-end web-content-mining workflow while acknowledging that live government scraping is not implemented.

## Introduction

Government tender notices contain titles, departments, locations, dates, descriptions and financial estimates. Analyzing many notices manually is time-consuming. Web content mining transforms available text and tabular fields into structured features and summaries. TenderScope demonstrates this process with a modular Python pipeline and dashboard.

## Problem Statement

Procurement listings can be dispersed across multiple portals and formats. Searching manually does not readily reveal repeated product combinations, activity over time, or textual similarity. The goal is to build a reproducible system for exploratory analysis of imported public tender records.

## Objectives

1. Validate and import tabular tender listings.
2. Normalize dates, currency, missing values and text.
3. Identify frequent terms and categories.
4. Analyze temporal, regional and organizational distributions.
5. Mine co-occurring requirements using Apriori.
6. Rank similar tenders and search results with TF-IDF.
7. Group documents using K-Means.
8. Provide interactive visualizations and exports.

## Existing System

Traditional workflows rely on visiting procurement portals, filtering listings and manually reviewing individual notices. Some portals offer built-in search, but cross-record exploratory text mining and reusable analytical exports may require additional processing. This project does not benchmark a specific official portal.

## Proposed System

A Streamlit dashboard connects a standardized tender schema to preprocessing and mining modules. Users start with an explicitly synthetic sample or import authorized CSV/Excel records. Results are computed from the currently selected dataset, with download options for tabular data and a concise PDF summary.

## Literature Review

The project uses established algorithms rather than claiming novel research: Salton and Buckley (1988) discuss term weighting for information retrieval; Agrawal and Srikant (1994) introduce fast algorithms for association rules; MacQueen (1967) describes classification and analysis of multivariate observations using cluster centers. These references support algorithm selection, not claims about Indian procurement trends.

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

## Screenshots

[Insert screenshots captured from the locally running Streamlit app: Overview; Data Collection; Preprocessing; Demand Analytics; Trend Analysis; Association Rules; Similarity; Clustering; Search; Value Analysis; Reports; Evaluation.] Screenshots are not fabricated in this report.

## Results and Discussion

The supplied data generator creates 720 synthetic records with recurring category-specific term combinations. The system is designed to calculate category counts, state counts, monthly frequency, estimated-value summaries, itemsets, rules, similarity rankings and clusters directly from the selected data. Do not interpret synthetic patterns as real-world government demand. [Insert actual screenshots and any additional metrics observed after running the application.]

## Evaluation

Source-code compilation was checked during package preparation. A full end-to-end test run could not be completed in the preparation environment because the mlxtend dependency was unavailable for installation. Run python -m pytest -q after installing requirements on the target machine and record the actual results here. Evaluation views show missing-estimate percentages and remaining duplicate source/ID counts. Cluster inertia/silhouette and Apriori metrics are calculated in their respective pages. Search precision, classification accuracy and real-world retrieval performance are not claimed without labelled ground truth.

## Limitations

The default dataset is synthetic; no automated live CPPP/GeM collector is included. Keyword baskets use a fixed English vocabulary and may miss synonyms. Porter stemming can reduce readability. Clusters are sensitive to K and feature representation. Similarity does not prove duplication. Estimated values may be missing and are not actual expenditure. The PDF export is a concise summary rather than a full narrative report. The dashboard does not include user authentication or a production-grade deployment.

## Future Scope

Add a permission-checked collector for approved public endpoints; maintain detailed import audit logs; improve organization and category normalization; add state choropleths, configurable term dictionaries, labelled retrieval benchmarks, a closing-soon view and richer PDF reports. Forecasting should only be attempted with sufficient genuine chronological observations and out-of-time evaluation.

## Conclusion

TenderScope demonstrates a coherent Python workflow for preparing, mining and visualizing tender-style text records. Its main educational value is combining data cleaning, TF-IDF retrieval, cosine similarity, Apriori co-occurrence and K-Means clustering in an interactive interface. Because the sample is synthetic, outputs demonstrate algorithm behavior rather than verified government procurement intelligence.

## References

[1] Salton, G., and Buckley, C. (1988). Term-weighting approaches in automatic text retrieval. Information Processing & Management, 24(5), 513–523.
[2] Agrawal, R., and Srikant, R. (1994). Fast Algorithms for Mining Association Rules in Large Databases. Proceedings of VLDB.
[3] MacQueen, J. (1967). Some Methods for Classification and Analysis of Multivariate Observations. Proceedings of the Fifth Berkeley Symposium.
[4] Central Public Procurement Portal: https://eprocure.gov.in/eprocure/app (portal reference, not scraped).
[5] Government e-Marketplace Bid Portal: https://bidplus.gem.gov.in/ (portal reference, not scraped).
[6] scikit-learn documentation: https://scikit-learn.org/stable/
[7] Streamlit documentation: https://docs.streamlit.io/
[8] mlxtend documentation: https://rasbt.github.io/mlxtend/

## Updated interface and demonstration dataset (November 2026)
The enhanced TenderScope release uses 850 labelled synthetic records across twelve Indian states and eight product categories. Its Streamlit interface has improved contrast, navy styling, revised chart labels, data-driven overview insights, positive-lift rule filtering, and percentage-formatted similarity results. The examples are not genuine tenders. Replace older screenshot placeholders with screenshots from this updated application; recompute any metrics from the currently loaded dataset.
