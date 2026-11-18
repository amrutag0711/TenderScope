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