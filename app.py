"""MAIN APP (Streamlit): sidebar navigation + one section per page. Run: streamlit run app.py"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from config import SAMPLE, FIELDS
from preprocessing.cleaning import preprocess
from mining.analytics import keyword_counts, search, similar, cluster, associations, trends
from database.db import initialize, store, load
from collectors.csv_collector import read_table
from utils.exports import excel_bytes, pdf_bytes

st.set_page_config(page_title='TenderScope', page_icon='🔎', layout='wide')
from ui_theme import apply_theme

apply_theme()
initialize()


@st.cache_data
def sample():
    return preprocess(pd.read_csv(SAMPLE))


@st.cache_data
def raw_sample():
    return pd.read_csv(SAMPLE)


@st.cache_data(show_spinner=False)
def c_assoc(d, s, c):
    return associations(d, s, c)


@st.cache_data(show_spinner=False)
def c_cluster(d, k):
    return cluster(d, k)


@st.cache_data(show_spinner=False)
def c_keywords(d, n=20):
    return keyword_counts(d, n)


if 'df' not in st.session_state:
    st.session_state.df = sample()
if 'raw' not in st.session_state:
    st.session_state.raw = raw_sample()
st.sidebar.markdown('### ◈ TENDERSCOPE')
st.sidebar.caption('◉ INTELLIGENCE LAB / 03')
page = st.sidebar.radio(
    'Navigation',
    [
        'Overview',
        'Data Collection',
        'Preprocessing',
        'Demand Analytics',
        'Trend Analysis',
        'Association Rules',
        'Similarity',
        'Clustering',
        'Tender Search',
        'Value Analysis',
        'Reports',
        'Evaluation',
        'About & Methodology',
    ],
)
st.sidebar.caption('Synthetic demonstration dataset by default. Not live government tenders.')
df = st.session_state.df
st.markdown(
    """<section class="tenderscope-hero"><div class="eyebrow">INTELLIGENCE / PATTERNS / DISCOVERY</div><div class="name">TenderScope<span style="color:#7be2df"> ✳</span></div><div class="sub">Explore procurement patterns, detect semantic relationships, and uncover regional signals with explainable machine learning.</div><div class="chip">● SYNTHETIC DEMONSTRATION DATA · NOT LIVE TENDERS</div></section>""",
    unsafe_allow_html=True,
)


def readable_chart(fig, horizontal=False):
    """Use explicit axis/legend colors: Plotly defaults can be faint on custom themes."""
    fig.update_layout(
        template='plotly_white',
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        font=dict(family='Arial, sans-serif', size=14, color='#273449'),
        title_font=dict(size=18, color='#17243A'),
        xaxis=dict(
            tickfont=dict(size=12, color='#34445C'),
            title_font=dict(size=13, color='#34445C'),
            gridcolor='#E8ECF3',
            linecolor='#A4ADBE',
            automargin=True,
            zeroline=False,
        ),
        yaxis=dict(
            tickfont=dict(size=12, color='#34445C'),
            title_font=dict(size=13, color='#34445C'),
            gridcolor='#E8ECF3',
            linecolor='#A4ADBE',
            automargin=True,
            zeroline=False,
        ),
        legend=dict(font=dict(size=12, color='#273449')),
        hoverlabel=dict(bgcolor='#17243A', font=dict(color='#FFFFFF', size=13)),
        margin=dict(l=155 if horizontal else 65, r=25, t=65, b=75),
    )
    return fig


def bar(counts, title, dimension='Category', measure='Tender count'):
    if counts.empty:
        st.info('No records to chart.')
        return
    data = pd.DataFrame({'Name': counts.index.astype(str), 'Value': counts.values})
    fig = px.bar(
        data,
        x='Value',
        y='Name',
        orientation='h',
        color='Value',
        color_continuous_scale=['#c5befb', '#8073e7', '#12a3a4'],
        title=title,
    )
    fig.update_layout(
        template='plotly_white',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='DM Sans', size=14, color='#37425a'),
        coloraxis_showscale=False,
        xaxis_title=measure,
        yaxis_title=dimension,
        height=max(390, len(counts) * 40),
        margin=dict(l=18, r=25, t=76, b=30),
        title_font=dict(size=19, color='#262448'),
        xaxis=dict(gridcolor='#edf0f6', zeroline=False),
        yaxis=dict(gridcolor='rgba(0,0,0,0)'),
    )
    readable_chart(fig, horizontal=True)
    fig.update_yaxes(autorange='reversed')
    fig.update_traces(hovertemplate='%{y}: %{x:,.0f}<extra></extra>')
    st.plotly_chart(fig, width='stretch')


def line_chart(data, x, y, title):
    fig = px.line(data, x=x, y=y, markers=True, title=title)
    fig.update_layout(
        template='plotly_white',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='DM Sans', size=14, color='#37425a'),
        height=420,
        title_font=dict(size=19, color='#262448'),
        xaxis=dict(gridcolor='#edf0f6'),
        yaxis=dict(gridcolor='#edf0f6'),
    )
    readable_chart(fig)
    fig.update_traces(line_color='#6858d8', marker_color='#12a3a4', line_width=3, marker_size=7)
    st.plotly_chart(fig, width='stretch')


def download(df, name='tenders.csv'):
    st.download_button(
        'Download CSV', df.to_csv(index=False).encode('utf-8'), name, mime='text/csv'
    )


st.markdown(f'<div class="ts-section">WORKSPACE / {page.upper()}</div>', unsafe_allow_html=True)
st.markdown(f'## {page if page != "Overview" else "Intelligence overview"}')
if page == 'Overview':
    cols = st.columns(5)
    for c, (label, val) in zip(
        cols,
        [
            ('Tenders', len(df)),
            ('Organizations', df.organization.nunique()),
            ('States', df.state.nunique()),
            ('Categories', df.product_category.nunique()),
            (
                'Avg estimate (₹)',
                f'{df.estimated_value.mean():,.0f}' if df.estimated_value.notna().any() else 'N/A',
            ),
        ],
    ):
        c.metric(label, val)
    st.info(
        'Tender counts represent observed listing frequency in the selected dataset, not completed purchases or verified market demand.'
    )
    if len(df):
        top_cat = df.product_category.value_counts()
        top_state = df.state.value_counts()
        st.markdown('#### Intelligence snapshot')
        st.write(
            f'**{top_cat.index[0]}** appears in **{top_cat.iloc[0]}** records. **{top_state.index[0]}** leads the selected sample with **{top_state.iloc[0]}** listings. These are calculated sample observations, not verified government statistics.'
        )
        closing = pd.to_datetime(df.closing_date, errors='coerce')
        now = pd.Timestamp.now().normalize()
        soon = df[(closing >= now) & (closing <= now + pd.Timedelta(days=14))]
        st.caption(
            f'{len(soon)} listings in this dataset have a closing date within the next 14 days (synthetic sample dates are not actionable opportunities).'
        )
    a, b = st.columns(2)
    with a:
        bar(df.product_category.value_counts().head(10), 'Top procurement categories')
    with b:
        t = trends(df)
        if not t.empty:
            line_chart(t, 'month', 'count', 'Monthly activity')
    st.dataframe(df.sort_values('publish_date', ascending=False).head(15), width='stretch')
elif page == 'Data Collection':
    st.subheader('Upload a CSV or Excel file')
    st.write(
        'Official portals: https://eprocure.gov.in/eprocure/app and https://bidplus.gem.gov.in/ . Use permitted manual exports; this application does not bypass access controls or claim live scraping.'
    )
    upload = st.file_uploader('Choose dataset', type=['csv', 'xlsx'])
    if upload is not None:
        try:
            raw = read_table(upload, upload.name)
            clean = preprocess(raw)
            st.success(f'Validated {len(clean)} records')
            if st.button('Use uploaded dataset'):
                st.session_state.raw = raw
                st.session_state.df = clean
                store(clean, upload.name)
                st.rerun()
        except Exception as e:
            st.error(f'Import failed: {e}')
    if st.button('Reset to synthetic sample'):
        st.session_state.df = sample()
        st.session_state.raw = raw_sample()
        st.rerun()
    if st.button('Load saved SQLite records'):
        saved = load()
        if not saved.empty:
            st.session_state.raw = saved
            st.session_state.df = preprocess(saved)
            st.rerun()
        st.warning('No saved records yet')
    st.download_button(
        'CSV template', pd.DataFrame(columns=FIELDS).to_csv(index=False), 'tender_template.csv'
    )
elif page == 'Preprocessing':
    raw = st.session_state.raw
    a, b, c = st.columns(3)
    a.metric('Raw rows', len(raw))
    b.metric('Cleaned rows', len(df))
    c.metric('Removed rows', len(raw) - len(df))
    st.write('Raw preview')
    st.dataframe(raw.head(20), width='stretch')
    st.write('Cleaned preview')
    st.dataframe(df.head(20), width='stretch')
    st.write('Missing values in cleaned data')
    st.dataframe(df.isna().sum().rename('missing').to_frame())
    download(df, 'cleaned_tenders.csv')
elif page == 'Demand Analytics':
    a, b = st.columns(2)
    with a:
        bar(df.product_category.value_counts().head(10), 'Top 10 categories')
        bar(df.state.value_counts().head(15), 'State-wise listing activity', 'State')
    with b:
        bar(c_keywords(df), 'Top 20 keywords / phrases')
        bar(
            df.organization.value_counts().head(12),
            'Organization-wise listing activity',
            'Organization',
        )
    bar(df.department.value_counts().head(12), 'Department-wise listing activity', 'Department')
elif page == 'Trend Analysis':
    t = trends(df)
    if not t.empty:
        line_chart(t, 'month', 'count', 'Monthly tender listings')
        z = df.dropna(subset=['publish_date']).copy()
        z['quarter'] = z.publish_date.dt.to_period('Q').astype(str)
        bar(z.quarter.value_counts().sort_index(), 'Quarterly activity', 'Quarter')
        z['year'] = z.publish_date.dt.year.astype(str)
        bar(z.year.value_counts().sort_index(), 'Year comparison', 'Year')
        mid = z.publish_date.median()
        earlier = z[z.publish_date < mid]
        later = z[z.publish_date >= mid]
        e = keyword_counts(earlier, 100)
        l = keyword_counts(later, 100)
        growth = l.div(max(len(later), 1)).sub(e.div(max(len(earlier), 1)), fill_value=0)
        st.write('Emerging terms (relative frequency change; exploratory):')
        st.dataframe(growth.sort_values(ascending=False).head(15).rename('change'))
elif page == 'Association Rules':
    s = st.slider('Minimum support', 0.01, 0.40, 0.04, 0.01)
    c = st.slider('Minimum confidence', 0.10, 1.0, 0.35, 0.05)
    items, rules = c_assoc(df, s, c)
    if items.empty:
        st.warning('No frequent itemsets at these settings')
    else:
        x = items.copy()
        x['itemsets'] = x.itemsets.map(lambda z: ', '.join(sorted(z)))
        st.write('Frequent itemsets')
        st.dataframe(x, width='stretch')
    if not rules.empty:
        rules = rules[rules.lift > 1].sort_values(['lift', 'confidence'], ascending=False)
    if rules.empty:
        st.warning(
            'No positive association rules at these settings. Try lowering support/confidence.'
        )
    else:
        r = rules.copy()
        for col in ['antecedents', 'consequents']:
            r[col] = r[col].map(lambda z: ', '.join(sorted(z)))
        st.dataframe(
            r[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(100),
            width='stretch',
        )
        download(r, 'association_rules.csv')
    st.caption(
        'Support = fraction of tenders containing a combination. Confidence = conditional fraction. Lift > 1 suggests positive co-occurrence, not causation.'
    )
elif page == 'Similarity':
    if len(df) > 1:
        i = st.selectbox(
            'Select a tender',
            range(len(df)),
            format_func=lambda i: f'{df.iloc[i].tender_id}: {df.iloc[i].tender_title}',
        )
        threshold = st.slider('Minimum similarity', 0.0, 1.0, 0.10, 0.05)
        out = similar(df, i, min(25, len(df) - 1))
        out = out[out.similarity >= threshold]
        out = out.copy()
        out['Similarity (%)'] = (out.similarity * 100).round(1)
        st.dataframe(
            out[['tender_id', 'tender_title', 'product_category', 'Similarity (%)', 'source_url']],
            width='stretch',
            hide_index=True,
        )
        st.caption('High textual similarity does not prove records are duplicates.')
elif page == 'Clustering':
    if len(df) > 2:
        k = st.slider('Number of clusters', 2, min(12, len(df) - 1), min(5, len(df) - 1))
        out, names, metrics = c_cluster(df, k)
        a, b = st.columns(2)
        a.metric('K-Means inertia', f'{metrics["inertia"]:.2f}')
        b.metric(
            'Silhouette score',
            f'{metrics["silhouette"]:.3f}' if metrics['silhouette'] is not None else 'Not defined',
        )
        bar(out.cluster.value_counts().sort_index(), 'Cluster distribution', 'Cluster')
        st.dataframe(
            pd.DataFrame({'cluster': range(len(names)), 'top_terms': names}), width='stretch'
        )
        st.dataframe(
            out[['tender_id', 'tender_title', 'cluster', 'cluster_terms']].head(100),
            width='stretch',
        )
        st.caption('Cluster terms are algorithmic descriptions, not verified category labels.')
elif page == 'Tender Search':
    q = st.text_input('Search ID, title, organization, department, location or keywords')
    filtered = df.copy()
    for col in ['state', 'department', 'organization', 'product_category', 'tender_status']:
        vals = st.multiselect(
            col.replace('_', ' ').title(), sorted(filtered[col].dropna().unique().tolist())
        )
        if vals:
            filtered = filtered[filtered[col].isin(vals)]
    dates = filtered.publish_date.dropna()
    if not dates.empty:
        dr = st.date_input('Publishing date range', (dates.min().date(), dates.max().date()))
        if len(dr) == 2:
            filtered = filtered[
                filtered.publish_date.between(
                    pd.Timestamp(dr[0]),
                    pd.Timestamp(dr[1]) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1),
                )
            ]
    maxval = filtered.estimated_value.max()
    if pd.notna(maxval) and maxval > 0:
        limit = st.number_input(
            'Maximum estimated value (INR, 0 = no limit)', min_value=0.0, value=0.0
        )
        if limit > 0:
            filtered = filtered[filtered.estimated_value <= limit]
    out = search(filtered, q, 100) if q else filtered
    st.write(f'{len(out)} results')
    st.dataframe(out, width='stretch')
    download(out, 'search_results.csv')
elif page == 'Value Analysis':
    d = df.dropna(subset=['estimated_value'])
    if d.empty:
        st.warning('No numeric estimates')
    else:
        a, b, c = st.columns(3)
        a.metric('Mean ₹', f'{d.estimated_value.mean():,.0f}')
        b.metric('Median ₹', f'{d.estimated_value.median():,.0f}')
        c.metric('Maximum ₹', f'{d.estimated_value.max():,.0f}')
        fig = px.histogram(
            d, x='estimated_value', nbins=35, title='Estimated value distribution (INR)'
        )
        fig.update_layout(
            template='plotly_white',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='DM Sans', size=14, color='#37425a'),
            xaxis_title='Estimated value (₹)',
            yaxis_title='Number of tenders',
        )
        readable_chart(fig)
        st.plotly_chart(fig, width='stretch')
        for col in ['product_category', 'state', 'organization']:
            bar(
                d.groupby(col).estimated_value.sum().sort_values(ascending=False).head(12),
                f'Total estimated tender value by {col.replace("_"," " )} (₹)',
                col.replace('_', ' ').title(),
                'Estimated value (₹)',
            )
        st.caption(
            'Published estimates are neither awarded contract values nor actual expenditure. Missing values are excluded.'
        )
elif page == 'Reports':
    st.write(
        'Export datasets and reproducible research outputs. Each export reflects the currently selected dataset.'
    )
    a, b = st.columns(2)
    with a:
        st.markdown(
            '<div class="ts-report"><strong>◫ Dataset · CSV</strong><p>Portable, analysis-ready tender records.</p></div>',
            unsafe_allow_html=True,
        )
        st.download_button(
            'Export CSV',
            df.to_csv(index=False).encode('utf-8'),
            'tenders.csv',
            mime='text/csv',
            key='report_csv',
        )
        st.markdown(
            '<div class="ts-report"><strong>▤ Analytical summary · PDF</strong><p>Research summary with descriptive metrics.</p></div>',
            unsafe_allow_html=True,
        )
        st.download_button(
            'Export PDF',
            pdf_bytes(df),
            'tenders_summary.pdf',
            mime='application/pdf',
            key='report_pdf',
        )
    with b:
        st.markdown(
            '<div class="ts-report"><strong>▦ Workbook · Excel</strong><p>Spreadsheet format for review and sharing.</p></div>',
            unsafe_allow_html=True,
        )
        st.download_button('Export Excel', excel_bytes(df), 'tenders.xlsx', key='report_xlsx')
        st.markdown(
            '<div class="ts-report"><strong>⌘ Discovered associations</strong><p>Export co-occurrence rules for further inspection.</p></div>',
            unsafe_allow_html=True,
        )
        items, rules = c_assoc(df, 0.04, 0.35)
        if not rules.empty:
            r = rules.copy()
            for col in ['antecedents', 'consequents']:
                r[col] = r[col].map(lambda z: ', '.join(sorted(z)))
            st.download_button(
                'Export association rules',
                r.to_csv(index=False).encode('utf-8'),
                'rules.csv',
                mime='text/csv',
                key='report_rules',
            )
        else:
            st.caption('No association rules available at default thresholds.')
    if len(df) > 2:
        st.markdown(
            '<div class="ts-report"><strong>◈ Cluster assignments</strong><p>Explore machine-learning groupings outside the app.</p></div>',
            unsafe_allow_html=True,
        )
        clusters, _, _ = c_cluster(df, 5)
        st.download_button(
            'Export clusters',
            clusters.to_csv(index=False).encode('utf-8'),
            'clusters.csv',
            mime='text/csv',
            key='report_clusters',
        )
elif page == 'Evaluation':
    a, b, c, d = st.columns(4)
    a.metric('Rows analyzed', len(df))
    b.metric(
        'Missing estimate %', f'{df.estimated_value.isna().mean()*100:.1f}%' if len(df) else 'N/A'
    )
    c.metric('Valid IDs %', f'{df.tender_id.notna().mean()*100:.1f}%' if len(df) else 'N/A')
    d.metric('Duplicate source+ID pairs', int(df.duplicated(['source_portal', 'tender_id']).sum()))
    st.write(
        'Clustering quality and association metrics are computed on the Clustering and Association Rules pages. Search precision and classification accuracy require independently labelled ground truth and are not claimed here.'
    )
elif page == 'About & Methodology':
    st.markdown('''### Problem and objective
TenderScope analyzes imported public procurement listings to discover textual patterns, recurring requirements, geographic distribution, time trends and estimated values.
### Methods
- **Collection:** user-supplied CSV/Excel and safe local HTML parsing example; no CAPTCHA bypass or automatic live scraping.
- **Preprocessing:** missing values, deduplication, normalization, Porter stemming and date parsing.
- **TF-IDF and cosine similarity:** information retrieval and similar tenders.
- **Apriori:** co-occurring product terms per tender, with support/confidence/lift.
- **K-Means:** unsupervised clustering of tender text.
### Ethics and limitations
Synthetic demonstration records are not official tenders. Frequency is a proxy for observed listing activity, not purchases. Estimated values are not awards. Clusters and rules are exploratory. Source portals: [CPPP](https://eprocure.gov.in/eprocure/app), [GeM](https://bidplus.gem.gov.in/).
''')
