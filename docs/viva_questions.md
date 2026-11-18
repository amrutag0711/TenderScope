# TenderScope | 100 Viva Questions and Answers

## Basic

1. **What is the Web?** A collection of linked resources accessed over the Internet.

2. **What is a URL?** A web resource address.

3. **What is HTML?** The markup language that structures a web page.

4. **What is HTTP?** The protocol used to transfer web requests and responses.

5. **What is scraping?** Extracting data from web pages with software.

6. **What is crawling?** Following links to discover web pages.

7. **What is DOM?** The document object representation of an HTML page.

8. **What is BeautifulSoup?** A Python library for parsing HTML.

9. **What is a dataset?** A collection of records and fields.

10. **What is a CSV?** A comma-separated text table.

11. **What is pandas?** A Python library for tabular data processing.

12. **What is Streamlit?** A Python framework for interactive web applications.

13. **What is SQLite?** A lightweight file-based relational database.

14. **What is SQLAlchemy?** A Python database toolkit.

15. **What is a primary key?** A unique row identifier.

16. **What is missing data?** A field whose value is unavailable.

17. **What is a duplicate?** A repeated record under a chosen identity rule.

18. **What is tokenization?** Splitting text into terms.

19. **What is a stopword?** A common word often removed from text analysis.

20. **What is stemming?** Reducing words to approximate roots.

21. **What is lemmatization?** Mapping words to dictionary base forms.

22. **What is web mining?** Finding useful patterns in web-related data.

23. **Types of web mining?** Content, structure and usage mining.

24. **Which type is used here?** Primarily web content mining.

25. **What is data cleaning?** Correcting or standardizing inconsistent data.

26. **What is a chart?** A visual representation of measurements.

27. **What is a dashboard?** An interface combining metrics and visualizations.

28. **What is an API?** An interface for software communication.

29. **What is robots.txt?** A file expressing crawler access preferences.

30. **What is a virtual environment?** An isolated Python dependency environment.

## Intermediate

1. **What is TF-IDF?** A score balancing a term’s frequency in one document against its rarity across documents.

2. **Why use TF-IDF?** It emphasizes informative words for text matching.

3. **What is cosine similarity?** A measure of how closely two document vectors point in the same direction.

4. **What is a vectorizer?** A tool that turns text into numeric features.

5. **What is an n-gram?** A sequence of n adjacent tokens.

6. **What is Apriori?** An algorithm that finds frequent item combinations.

7. **What is support?** The fraction of transactions containing an itemset.

8. **What is confidence?** The proportion of X-containing transactions that also contain Y.

9. **What is lift?** Confidence divided by the overall prevalence of Y.

10. **What does lift above one mean?** Positive co-occurrence relative to independence.

11. **What is a transaction?** Here, the set of extracted terms in one tender.

12. **Why use multiple terms?** One category per tender cannot reveal item co-occurrence.

13. **What is K-Means?** An algorithm grouping vectors around K centroids.

14. **What is a centroid?** The center of a cluster in feature space.

15. **What is inertia?** The sum of squared distances to assigned centroids.

16. **What is silhouette score?** A measure of cluster cohesion and separation.

17. **Why normalize dates?** To compare records consistently over time.

18. **Why preserve null values?** Missing is not equivalent to zero.

19. **What is a filter?** A condition restricting the displayed records.

20. **What is ranking?** Ordering results by relevance.

21. **What is search relevance?** How well a record matches the query.

22. **What is overfitting?** Learning patterns that do not generalize.

23. **What is unsupervised learning?** Finding structure without labelled targets.

24. **What is clustering?** Grouping similar records.

25. **What is classification?** Predicting a defined label.

26. **What is a time trend?** Change in an observed measure across periods.

27. **What is an outlier?** An unusually extreme observation.

28. **What is a unit test?** A check of one small behavior.

29. **What is a data schema?** The set of fields and their expected meanings.

30. **Why use SQL indexes?** To speed up some database lookups.

## Advanced

1. **Can high cosine similarity prove duplication?** No; separate tenders may use similar templates.

2. **Does confidence imply causation?** No; it is an association statistic.

3. **Can synthetic data validate market demand?** No; it only tests software behavior.

4. **How do you avoid data leakage?** Separate evaluation data from model development and avoid future information in earlier predictions.

5. **How would you evaluate search?** Use labelled relevant records and calculate precision at K.

6. **How would you evaluate classification?** Compare predictions with verified labels using precision, recall and F1.

7. **How would you choose K?** Compare interpretability, inertia and silhouette, then inspect clusters.

8. **Why is K-Means sensitive to initialization?** Different starting centroids can produce different local solutions.

9. **What is sparse representation?** Storing mostly zero features efficiently.

10. **Why use bigrams?** They preserve short phrases such as solar panel.

11. **What is IDF?** A weight that decreases for terms present in many documents.

12. **What is data provenance?** Information about where and when records originated.

13. **How can a collector be ethical?** Use permitted endpoints, limit requests and respect access rules.

14. **Why avoid CAPTCHA bypass?** It circumvents site access controls and may violate policy.

15. **What is concept drift?** Changes in data patterns over time.

16. **Why are estimated and awarded values different?** One is a pre-award estimate; the other is a contractual outcome.

17. **What is a temporal holdout?** Testing on later records than the training period.

18. **What is precision at K?** The fraction of the top K retrieved records judged relevant.

19. **How do you validate trends?** Compare chart totals with independent group-by counts.

20. **What are limitations of fixed keyword baskets?** They miss synonyms and may include irrelevant occurrences.

## Project-specific

1. **Why TenderScope?** It applies several web data mining techniques to a practical procurement-listing format.

2. **What is the main problem?** Extracting patterns from many scattered tender descriptions.

3. **Where is your dataset from?** The bundled 720 records were generated synthetically for demonstration.

4. **Are they genuine tenders?** No; every record is explicitly synthetic.

5. **Does the app scrape CPPP live?** No; it imports permitted exports and demonstrates local HTML parsing.

6. **What happens when scraping is blocked?** We do not bypass controls; we use authorized manual exports.

7. **Why use Streamlit?** It makes Python analytics interactive with minimal frontend code.

8. **Why SQLite?** It is simple to run locally without a separate database server.

9. **Why Apriori?** It reveals recurring combinations of product requirements.

10. **Why TF-IDF?** It supports relevance ranking from tender text.

11. **Why K-Means?** It explores unlabeled groups of similar descriptions.

12. **What are your input columns?** Tender ID and title are required; other fields are optional.

13. **What is the key output?** Interactive patterns, rankings, rules, clusters and downloadable summaries.

14. **How are duplicates handled?** The same source portal and tender ID are kept once.

15. **What are your ethics rules?** Public authorized data only, source attribution and no access bypass.

16. **How do you run the project?** Install dependencies, initialize SQLite and run streamlit run app.py.

17. **How do you test it?** Run python -m pytest -q and inspect the dashboard.

18. **What is not implemented?** Live portal scraping, forecasting and labelled accuracy benchmarks.

19. **What is your contribution?** Integrating text mining and visualization in a single reproducible app.

20. **What would you improve?** Add permitted live sources, better normalization and labelled evaluation.

## Three-minute demonstration script

Good morning. My project is TenderScope, a government tender pattern mining and demand intelligence system. It demonstrates how we can transform tender-style records into searchable insights using Python and web content mining. The bundled 720 records are synthetic and not real government tenders. First, on the Overview page, I can see category, organization and state counts. On Data Collection, I can upload authorized CSV or Excel files. Preprocessing handles missing values, dates, currency and duplicates. Demand Analytics shows frequent terms and category distribution, while Trend Analysis groups listings by month and quarter. Association Rules uses Apriori to discover product terms appearing together, with support, confidence and lift. Similarity uses TF-IDF and cosine similarity to rank related tender descriptions. Clustering uses K-Means to explore natural text groups. The Search page ranks matches and applies filters. Finally, Reports exports the results. The key limitation is that tender frequency is not proof of actual purchases, and the demonstration data is synthetic. Thank you.
