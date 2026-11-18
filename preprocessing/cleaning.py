"""PREPROCESSING: turns raw uploaded data into a clean, uniform table."""

import re
import pandas as pd
from config import FIELDS
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.stem import PorterStemmer

STEM = PorterStemmer()


def clean_text(s):
    """Lowercase, keep letters only, drop stop words, then stem (Porter) each word."""
    words = re.findall(r'[a-z]+', str(s).lower())
    return ' '.join(STEM.stem(w) for w in words if len(w) > 2 and w not in ENGLISH_STOP_WORDS)


def money(v):
    """Convert values like '2 lakh' or '1.5 crore' to a plain rupee number (NaN if missing)."""
    if pd.isna(v) or str(v).strip() == '':
        return float('nan')
    s = str(v).lower().replace(',', '').replace('₹', '').replace('rs.', '').strip()
    m = re.search(r'([0-9]+(?:\.[0-9]+)?)\s*(crore|cr|lakh|lac)?', s)
    if not m:
        return float('nan')
    return (
        float(m.group(1)) * {'crore': 1e7, 'cr': 1e7, 'lakh': 1e5, 'lac': 1e5, None: 1}[m.group(2)]
    )


def preprocess(df):
    """Full cleaning pipeline: validate columns -> remove blanks/duplicates -> fill
    missing text -> parse dates -> normalise money -> build stemmed text column."""
    if 'tender_id' not in df or 'tender_title' not in df:
        raise ValueError('Required columns: tender_id, tender_title')
    d = df.copy()
    for c in FIELDS:
        if c not in d:
            d[c] = pd.NA
    d = d[FIELDS].copy()
    d['tender_id'] = d['tender_id'].astype('string').str.strip()
    d = d[
        d.tender_id.notna()
        & d.tender_id.ne('')
        & d.tender_title.notna()
        & d.tender_title.astype(str).str.strip().ne('')
    ]
    d = d.drop_duplicates(subset=['source_portal', 'tender_id'], keep='last')
    for c in [
        'organization',
        'department',
        'state',
        'city',
        'tender_category',
        'product_category',
        'tender_status',
        'source_portal',
    ]:
        d[c] = d[c].fillna('Unknown').astype(str).str.strip().replace('', 'Unknown')
    for c in ['publish_date', 'closing_date']:
        d[c] = pd.to_datetime(d[c], errors='coerce', dayfirst=False, format='mixed')
    d['estimated_value'] = d['estimated_value'].apply(money)
    d['cleaned_description'] = (
        d.tender_title.fillna('') + ' ' + d.tender_description.fillna('')
    ).map(clean_text)
    return d.reset_index(drop=True)
