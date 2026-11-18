"""Central settings: file paths and the list of columns every tender record must have."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SAMPLE = ROOT / 'data/sample/synthetic_tenders.csv'
import os

DB = Path(os.environ.get('TENDERSCOPE_DB') or ROOT / 'data/tenders.sqlite')
FIELDS = [
    'tender_id',
    'tender_title',
    'organization',
    'department',
    'state',
    'city',
    'tender_category',
    'product_category',
    'tender_description',
    'publish_date',
    'closing_date',
    'estimated_value',
    'tender_type',
    'procurement_method',
    'tender_status',
    'source_portal',
    'source_url',
    'collected_at',
    'keywords',
    'cleaned_description',
]
