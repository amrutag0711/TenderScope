"""MINING: the data-mining algorithms (TF-IDF search, similarity, K-Means, Apriori, trends)."""

import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from mlxtend.frequent_patterns import apriori, association_rules

TERMS = [
    'desktop',
    'monitor',
    'keyboard',
    'router',
    'switch',
    'server',
    'laptop',
    'printer',
    'solar',
    'panel',
    'inverter',
    'battery',
    'transformer',
    'cable',
    'led',
    'meter',
    'hospital',
    'ventilator',
    'scanner',
    'medicine',
    'cement',
    'steel',
    'road',
    'bridge',
    'vehicle',
    'transport',
    'furniture',
    'stationery',
    'security',
    'maintenance',
    'installation',
    'network',
    'computer',
    'medical',
    'electrical',
]


def keyword_counts(df, n=20):
    """Most frequent words/2-word phrases (Bag-of-Words counts)."""
    if df.empty:
        return pd.Series(dtype=int)
    v = CountVectorizer(stop_words='english', ngram_range=(1, 2), max_features=2000)
    try:
        x = v.fit_transform(
            (df.tender_title.fillna('') + ' ' + df.tender_description.fillna('')).astype(str)
        )
        return (
            pd.Series(np.asarray(x.sum(axis=0)).ravel(), index=v.get_feature_names_out())
            .sort_values(ascending=False)
            .head(n)
        )
    except ValueError:
        return pd.Series(dtype=int)


def search(df, q, k=30):
    """Rank tenders against a query using TF-IDF + cosine similarity (information retrieval)."""
    if df.empty:
        return df.copy()
    if not q.strip():
        return df.head(k)
    docs = (
        df.tender_id.astype(str)
        + ' '
        + df.tender_title.fillna('')
        + ' '
        + df.organization.fillna('')
        + ' '
        + df.department.fillna('')
        + ' '
        + df.state.fillna('')
        + ' '
        + df.product_category.fillna('')
        + ' '
        + df.tender_description.fillna('')
    ).tolist()
    v = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    x = v.fit_transform(docs + [q])
    scores = cosine_similarity(x[-1], x[:-1]).ravel()
    result = df.copy()
    result['relevance'] = scores
    return result[result.relevance > 0].sort_values('relevance', ascending=False).head(k)


def similar(df, index, k=10):
    """Find the k tenders whose text is most similar to tender number `index`."""
    if len(df) < 2:
        return pd.DataFrame()
    v = TfidfVectorizer(stop_words='english')
    x = v.fit_transform(
        (
            df.tender_title.fillna('')
            + ' '
            + df.product_category.fillna('')
            + ' '
            + df.cleaned_description.fillna('')
        ).astype(str)
    )
    scores = cosine_similarity(x[index], x).ravel()
    scores[index] = -1
    ids = np.argsort(-scores)[:k]
    result = df.iloc[ids].copy()
    result['similarity'] = scores[ids]
    return result


def cluster(df, k=5):
    """Group tenders into k clusters with K-Means on TF-IDF vectors; also returns
    top terms per cluster, inertia and silhouette score (cluster quality)."""
    if len(df) < 3:
        return pd.DataFrame(), [], None
    k = min(max(2, k), len(df) - 1)
    v = TfidfVectorizer(stop_words='english', max_features=1200)
    x = v.fit_transform(df.cleaned_description.fillna('').astype(str))
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(x)
    words = v.get_feature_names_out()
    names = [' / '.join(words[np.argsort(c)[-4:][::-1]]) for c in model.cluster_centers_]
    out = df.copy()
    out['cluster'] = labels
    out['cluster_terms'] = [names[i] for i in labels]
    score = silhouette_score(x, labels) if len(set(labels)) > 1 and len(df) > k else None
    return out, names, {'inertia': model.inertia_, 'silhouette': score}


def baskets(df, terms=TERMS):
    """Build a True/False table: does each tender mention each product term?
    Each tender acts like a shopping 'basket' for Apriori."""
    texts = (
        (df.tender_title.fillna('') + ' ' + df.tender_description.fillna(''))
        .astype(str)
        .str.lower()
    )
    return pd.DataFrame(
        {t: texts.str.contains(r'\b' + re.escape(t) + r'\b', regex=True).to_numpy() for t in terms},
        index=df.index,
    )


def associations(df, support=0.04, confidence=0.35):
    """Apriori association-rule mining: finds terms that appear together.
    support = how common; confidence = P(B | A); lift > 1 = appear together more than chance."""
    if df.empty:
        return pd.DataFrame(), pd.DataFrame()
    b = baskets(df)
    b = b.loc[:, b.any(axis=0)]
    if b.shape[1] < 2:
        return pd.DataFrame(), pd.DataFrame()
    items = apriori(b, min_support=support, use_colnames=True, max_len=3)
    if items.empty or not (items.itemsets.map(len) > 1).any():
        return items, pd.DataFrame()
    import inspect

    kwargs = {'metric': 'confidence', 'min_threshold': confidence}
    if 'num_itemsets' in inspect.signature(association_rules).parameters:
        kwargs['num_itemsets'] = len(df)
    rules = association_rules(items, **kwargs)
    return items, rules.sort_values('lift', ascending=False) if not rules.empty else rules


def trends(df):
    """Count tenders published per month."""
    x = df.dropna(subset=['publish_date']).copy()
    if x.empty:
        return pd.DataFrame(columns=['month', 'count'])
    x['month'] = x.publish_date.dt.to_period('M').astype(str)
    return x.groupby('month').size().reset_index(name='count')
