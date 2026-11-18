"""EXPORTS: builds downloadable Excel and PDF files."""

from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


def _safe(v):
    return "'" + v if isinstance(v, str) and v[:1] in ('=', '+', '-', '@') else v


def excel_bytes(df):
    b = BytesIO()
    df = df.copy()
    for c in df.select_dtypes(include='object').columns:
        df[c] = df[c].map(_safe)
    with __import__('pandas').ExcelWriter(b, engine='openpyxl') as w:
        df.to_excel(w, index=False, sheet_name='Tenders')
    return b.getvalue()


def pdf_bytes(df):
    b = BytesIO()
    doc = SimpleDocTemplate(b, pagesize=A4)
    styles = getSampleStyleSheet()
    story = [
        Paragraph('TenderScope | Analytical Summary', styles['Title']),
        Spacer(1, 15),
        Paragraph(
            'Dataset provenance: check source_portal and source_url. Synthetic records are not real procurement notices.',
            styles['Normal'],
        ),
        Spacer(1, 12),
    ]
    data = [
        ['Metric', 'Value'],
        ['Tender records', str(len(df))],
        ['Organizations', str(df.organization.nunique())],
        ['States', str(df.state.nunique())],
        ['Categories', str(df.product_category.nunique())],
    ]
    if df.estimated_value.notna().any():
        data.append(['Average estimated value (INR)', f'{df.estimated_value.mean():,.0f}'])
    t = Table(data, colWidths=[260, 160])
    t.setStyle(
        TableStyle(
            [
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#16304e')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('GRID', (0, 0), (-1, -1), 0.3, colors.grey),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ]
        )
    )
    story.append(t)
    doc.build(story)
    return b.getvalue()
