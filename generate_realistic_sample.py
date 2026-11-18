"""Generates the synthetic (fake) demo dataset in data/sample/synthetic_tenders.csv."""

from pathlib import Path
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

SEED = 2026
random.seed(SEED)
rng = np.random.default_rng(SEED)
ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'data' / 'sample' / 'synthetic_tenders.csv'
STATES = {
    'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Nashik'],
    'Karnataka': ['Bengaluru', 'Mysuru', 'Hubballi'],
    'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara'],
    'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai'],
    'Telangana': ['Hyderabad', 'Warangal'],
    'Delhi': ['New Delhi'],
    'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Noida'],
    'West Bengal': ['Kolkata', 'Siliguri'],
    'Kerala': ['Kochi', 'Thiruvananthapuram'],
    'Rajasthan': ['Jaipur', 'Jodhpur'],
    'Odisha': ['Bhubaneswar', 'Cuttack'],
    'Madhya Pradesh': ['Bhopal', 'Indore'],
}
CATEGORIES = {
    'IT and Networking': {
        'items': [
            'desktop computers',
            'laptops',
            'network switches',
            'routers',
            'firewalls',
            'UPS systems',
            'monitors',
            'printers',
        ],
        'base': (150000, 18000000),
    },
    'Electrical Equipment': {
        'items': [
            'distribution transformers',
            'power cables',
            'smart meters',
            'LED streetlights',
            'control panels',
            'circuit breakers',
        ],
        'base': (350000, 38000000),
    },
    'Solar Energy': {
        'items': [
            'rooftop solar modules',
            'solar inverters',
            'battery storage',
            'mounting structures',
            'solar cables',
        ],
        'base': (600000, 65000000),
    },
    'Healthcare': {
        'items': [
            'patient monitors',
            'ventilators',
            'ultrasound machines',
            'hospital beds',
            'diagnostic scanners',
        ],
        'base': (250000, 55000000),
    },
    'Construction': {
        'items': [
            'cement',
            'reinforcement steel',
            'road resurfacing',
            'drainage pipes',
            'bridge repair',
        ],
        'base': (800000, 80000000),
    },
    'Office Supplies': {
        'items': [
            'office furniture',
            'stationery kits',
            'multifunction printers',
            'filing cabinets',
            'conference tables',
        ],
        'base': (45000, 5500000),
    },
    'Transport': {
        'items': [
            'passenger vehicles',
            'fleet tracking devices',
            'vehicle maintenance',
            'electric buses',
            'tyres',
        ],
        'base': (250000, 75000000),
    },
    'IT Infrastructure': {
        'items': [
            'rack servers',
            'data storage',
            'network racks',
            'backup systems',
            'structured cabling',
        ],
        'base': (450000, 42000000),
    },
}
ORG = {
    'Maharashtra': [
        'Public Works Department',
        'Municipal Corporation',
        'State Electricity Distribution Company',
        'Government Medical College',
    ],
    'Karnataka': [
        'Urban Development Department',
        'State Health Department',
        'Public Works Department',
    ],
    'Gujarat': ['Municipal Corporation', 'Energy Development Agency', 'Education Department'],
    'Tamil Nadu': [
        'State Transport Corporation',
        'Public Works Department',
        'Medical Services Corporation',
    ],
    'Telangana': [
        'State IT Department',
        'Municipal Administration Department',
        'Health Department',
    ],
    'Delhi': ['Government Hospital', 'Public Works Department', 'Education Directorate'],
}
ORG_DEFAULT = [
    'District Administration',
    'Public Works Department',
    'State Health Directorate',
    'Education Department',
]
TEMPLATES = [
    'Supply, installation and commissioning of {main} at {city} facilities',
    'Procurement of {main} with {extra} for departmental operations',
    'Annual rate contract for supply and maintenance of {main}',
    'Upgradation of public infrastructure using {main} and {extra}',
    'Purchase and deployment of {main} for {org}',
    'Supply of {main} including testing, training and warranty support',
    'Replacement and modernization of existing {main} systems',
    'Design, supply and installation of {main} including {extra}',
]
WEIGHTS = [0.18, 0.13, 0.10, 0.12, 0.14, 0.10, 0.09, 0.14]
rows = []
for i in range(850):
    state = random.choices(list(STATES), weights=[19, 13, 11, 10, 9, 8, 8, 6, 5, 5, 3, 3])[0]
    city = random.choice(STATES[state])
    org = random.choice(ORG.get(state, ORG_DEFAULT))
    category = random.choices(list(CATEGORIES), weights=[19, 15, 10, 12, 15, 8, 10, 11])[0]
    spec = CATEGORIES[category]
    items = random.sample(spec['items'], k=random.choice([2, 3, 3, 4]))
    main, extra = items[:2]
    title = random.choices(TEMPLATES, weights=WEIGHTS)[0].format(
        main=main, extra=extra, city=city, org=org
    )
    title += f' - Package {random.randint(1,9)} / {random.choice(["A","B","C","D"])}'
    published = datetime(2023, 1, 1) + timedelta(days=random.randrange(0, 1350))
    duration = random.randint(15, 75)
    closing = published + timedelta(days=duration)
    low, high = spec['base']
    value = int(np.exp(rng.uniform(np.log(low), np.log(high))) // 1000 * 1000)
    if rng.random() < 0.09:
        value = np.nan
    status = 'Closed' if closing < datetime(2026, 11, 15) else 'Open'
    description = (
        f'{org} invites bids for {main}, {extra} and {", ".join(items[2:]) if len(items)>2 else "related accessories"} '
        f'for facilities in {city}, {state}. Scope includes delivery, installation, testing, commissioning, '
        f'technical documentation, warranty and training where applicable. Estimated quantity: '
        f'{random.randint(5,250)} units. Completion period: {random.choice([30,45,60,90,120,180])} days. '
        f'Eligibility and detailed specifications are provided in the tender documents.'
    )
    rows.append(
        dict(
            tender_id=f'SYN-{i+1:05d}',
            tender_title=title,
            organization=org,
            department=org,
            state=state,
            city=city,
            tender_category=(
                'Goods' if category not in ['Construction', 'Transport'] else 'Goods and Services'
            ),
            product_category=category,
            tender_description=description,
            publish_date=published.date().isoformat(),
            closing_date=closing.date().isoformat(),
            estimated_value=value,
            tender_type='Open Tender',
            procurement_method=random.choice(
                ['e-Procurement', 'Open Competitive Bidding', 'Two-Bid System']
            ),
            tender_status=status,
            source_portal='SYNTHETIC DEMONSTRATION DATA',
            source_url='',
            collected_at='2026-11-15T00:00:00',
            keywords=', '.join(items),
            cleaned_description='',
        )
    )
OUT.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame(rows).to_csv(OUT, index=False)
print(f'Generated {len(rows)} clearly labelled SYNTHETIC records at {OUT}')
