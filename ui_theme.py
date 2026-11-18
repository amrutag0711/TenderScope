"""UI THEME: custom CSS (colours, fonts, cards) injected into Streamlit."""

import streamlit as st

CSS = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --paper: #f3f1ed;
    --ink: #1c2431;
    --muted: #596579;
    --purple: #6553d7;
    --violet: #8e79f2;
    --cyan: #13a4a5;
    --line: #dfe2e9;
}

/* ========== GENERAL APP ========== */

html, body, .stApp,
[data-testid="stAppViewContainer"] {
    font-family: 'DM Sans', sans-serif !important;
    color: var(--ink) !important;
}

.stApp,
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(
            ellipse at 90% 5%,
            #e9e5ff 0%,
            transparent 34%
        ),
        radial-gradient(
            ellipse at 0% 85%,
            #dff3f1 0%,
            transparent 30%
        ),
        var(--paper) !important;
}

[data-testid="stHeader"] {
    background: rgba(243,241,237,.83) !important;
    backdrop-filter: blur(14px);
}

.block-container {
    max-width: 1680px !important;
    padding: 2.2rem 3rem 5rem !important;
}

/* ========== TYPOGRAPHY ========== */

h1, h2, h3, h4 {
    font-family: 'Space Grotesk', sans-serif !important;
    letter-spacing: -.035em !important;
    color: #20243c !important;
}

h1 {
    font-size: clamp(2.3rem, 3.8vw, 3.7rem) !important;
}

h2 {
    font-size: 2rem !important;
}

h3 {
    font-size: 1.4rem !important;
}

[data-testid="stMain"] p,
[data-testid="stMain"] li {
    color: #30384c;
    line-height: 1.6 !important;
}

[data-testid="stMain"] [data-testid="stMarkdownContainer"] {
    color: #30384c;
}

[data-testid="stMain"] [data-testid="stCaptionContainer"] p {
    color: #596579 !important;
    opacity: 1 !important;
    font-size: .85rem !important;
}

/* ========== SIDEBAR ========== */

[data-testid="stSidebar"] {
    background: #191a32 !important;
    border-right: 1px solid #393958 !important;
}

[data-testid="stSidebar"] * {
    color: #f7f6ff !important;
}

[data-testid="stSidebar"] [role="radiogroup"] label {
    padding: 10px 12px !important;
    border-radius: 12px !important;
    margin: 3px 0;
    transition: all .2s;
    border: 1px solid transparent;
}

[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: #343354 !important;
    border-color: #57517f !important;
}

[data-testid="stSidebar"]
[role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(
        95deg,
        #5e51c8,
        #34365f
    ) !important;
    border-color: #8577f2 !important;
}

[data-testid="stSidebar"] [role="radiogroup"] label p {
    color: #ffffff !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    opacity: 1 !important;
}

[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
    color: #c7c5e5 !important;
}

/* ========== METRIC CARDS ========== */

[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        #ffffff,
        #f9f8ff
    ) !important;

    border: 1px solid #e2dff1 !important;
    border-radius: 19px !important;
    padding: 23px !important;

    box-shadow:
        0 12px 28px #30246c0d,
        0 3px 0 #ded9f6 !important;

    min-height: 136px;
}

[data-testid="stMetricLabel"] p {
    color: #505b77 !important;
    font-weight: 800 !important;
    text-transform: uppercase;
    letter-spacing: .09em;
    font-size: .77rem !important;
}

[data-testid="stMetricValue"] {
    color: #272452 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: clamp(1.5rem, 2.1vw, 2.4rem) !important;
    font-weight: 700 !important;
}

/* ========== CHARTS ========== */

[data-testid="stPlotlyChart"] {
    background: #ffffff !important;
    border: 1px solid #e0e3ec !important;
    border-radius: 20px !important;
    padding: 14px !important;
    box-shadow: 0 9px 24px #252c510b;
}

/* ========== DATA TABLES ========== */

[data-testid="stDataFrame"] {
    border: 1px solid #d7dbe8 !important;
    border-radius: 14px !important;
    overflow: hidden;
    background: #ffffff !important;
}

/* ========== BUTTONS ========== */

.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(
        110deg,
        #6553d7,
        #5142ad
    ) !important;

    color: #ffffff !important;
    border: 0 !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    padding: .65rem 1.15rem !important;
    box-shadow: 0 4px 12px #5142ad2b !important;
    min-height: 43px;
    transition: all .2s ease;
}

.stButton > button *,
.stDownloadButton > button * {
    color: #ffffff !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background: linear-gradient(
        110deg,
        #4534aa,
        #278d99
    ) !important;

    color: #ffffff !important;
    transform: translateY(-1px);
}

/* ========== WIDGET LABELS ========== */

[data-testid="stMain"] [data-testid="stWidgetLabel"],
[data-testid="stMain"] [data-testid="stWidgetLabel"] p,
[data-testid="stMain"] [data-testid="stWidgetLabel"] label {
    color: #252641 !important;
    opacity: 1 !important;
    font-size: 14px !important;
    font-weight: 700 !important;
}

/* ========== TEXT INPUT ========== */

[data-testid="stTextInput"] input {
    color: #252641 !important;
    background: #ffffff !important;
    font-size: 14px !important;
    min-height: 43px !important;
    border-radius: 11px !important;
}

[data-testid="stTextInput"] input::placeholder {
    color: #697188 !important;
    opacity: 1 !important;
}

/* ========== SELECTBOX ========== */

[data-testid="stMain"] [data-baseweb="select"] > div {
    background: #ffffff !important;
    border-radius: 11px !important;
    min-height: 43px !important;
}

[data-testid="stMain"] [data-baseweb="select"] input,
[data-testid="stMain"] [data-baseweb="select"] span {
    color: #252641 !important;
    opacity: 1 !important;
}

[data-testid="stMain"] [data-baseweb="select"] input::placeholder {
    color: #697188 !important;
    opacity: 1 !important;
}

[data-testid="stMain"] [data-baseweb="select"] svg {
    fill: #5142ad !important;
}

/* ========== MULTISELECT ========== */

[data-testid="stMultiSelect"] [data-baseweb="select"] > div {
    background: #ffffff !important;
    border: 1px solid #cfd3e1 !important;
}

[data-testid="stMultiSelect"] [data-baseweb="tag"] {
    background: #e8e4ff !important;
    border-radius: 8px !important;
}

[data-testid="stMultiSelect"] [data-baseweb="tag"] span {
    color: #352a83 !important;
    font-weight: 600 !important;
}

/* ========== DROPDOWN MENU ========== */

[data-baseweb="popover"] [role="listbox"],
[data-baseweb="menu"] {
    background: #ffffff !important;
}

[data-baseweb="popover"] [role="option"],
[data-baseweb="menu"] [role="option"] {
    color: #252641 !important;
    background: #ffffff !important;
}

[data-baseweb="popover"] [role="option"]:hover,
[data-baseweb="menu"] [role="option"]:hover {
    background: #f0edff !important;
}

/* ========== NUMBER INPUT ========== */

[data-testid="stNumberInput"] input {
    background: #ffffff !important;
    color: #252641 !important;
    font-size: 14px !important;
    min-height: 43px !important;
}

[data-testid="stNumberInput"] button {
    background: #5142ad !important;
    color: #ffffff !important;
}

/* ========== DATE INPUT ========== */

[data-testid="stDateInput"] input {
    background: #ffffff !important;
    color: #252641 !important;
    font-size: 14px !important;
}

[data-testid="stDateInput"] svg {
    color: #5142ad !important;
}

/* ========== FILE UPLOADER ========== */

[data-testid="stFileUploader"] {
    background: #ffffff !important;
    border: 1px solid #dcdfea !important;
    border-radius: 16px !important;
    padding: 15px !important;
}

[data-testid="stFileUploader"] section {
    background: #f8f7ff !important;
    border: 1px dashed #a49be3 !important;
    border-radius: 12px !important;
}

[data-testid="stFileUploader"] section p,
[data-testid="stFileUploader"] section span,
[data-testid="stFileUploader"] section small {
    color: #30344d !important;
    opacity: 1 !important;
}

[data-testid="stFileUploader"] button {
    background: #6553d7 !important;
    color: #ffffff !important;
    border: 1px solid #6553d7 !important;
    border-radius: 9px !important;
    font-weight: 700 !important;
}

[data-testid="stFileUploader"] button * {
    color: #ffffff !important;
}

/* ========== SLIDERS ========== */

[data-testid="stSlider"] {
    padding: 8px 0 !important;
}

[data-testid="stMain"] [data-testid="stSlider"] p,
[data-testid="stMain"] [data-testid="stSlider"] label {
    color: #252641 !important;
    opacity: 1 !important;
}

[data-testid="stSlider"] [role="slider"] {
    background: #6553d7 !important;
    border-color: #6553d7 !important;
}

/* ========== ALERTS ========== */

[data-testid="stAlert"] {
    border-radius: 13px !important;
    border: 1px solid #dcdcf0 !important;
}

/* ========== HERO SECTION ========== */

.tenderscope-hero {
    padding: 37px 44px 38px;
    border-radius: 24px;

    background:
        radial-gradient(
            circle at 84% 14%,
            #5a4ba0 0%,
            transparent 38%
        ),
        linear-gradient(
            110deg,
            #1c203d,
            #25254e 65%,
            #35306b
        );

    color: #ffffff !important;
    margin: 0 0 32px;
    position: relative;
    overflow: hidden;

    box-shadow: 0 18px 36px #25214d25;
}

.tenderscope-hero:after {
    content: '';
    position: absolute;
    right: 7%;
    top: -105px;
    width: 350px;
    height: 350px;
    border: 1px solid #9e96ec88;
    border-radius: 50%;

    box-shadow:
        0 0 0 36px #a49aff10,
        0 0 0 75px #a49aff09;

    pointer-events: none;
}

.tenderscope-hero .eyebrow {
    font-size: .75rem;
    letter-spacing: .22em;
    color: #90e2e3 !important;
    font-weight: 800;
}

.tenderscope-hero .name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2.4rem, 4.5vw, 4.2rem);
    letter-spacing: -.055em;
    font-weight: 700;
    line-height: 1.12;
    margin: 13px 0;
    color: #ffffff !important;
}

.tenderscope-hero .sub {
    color: #e0e3fa !important;
    font-size: 1.05rem;
    max-width: 780px;
    line-height: 1.7;
}

.tenderscope-hero .chip {
    display: inline-block;
    border: 1px solid #8987bd;
    background: #ffffff12;
    border-radius: 30px;
    padding: 8px 15px;
    margin-top: 20px;
    font-size: .75rem;
    letter-spacing: .07em;
    color: #e9e8ff !important;
    font-weight: 700;
}

/* ========== SECTION LABELS ========== */

.ts-section {
    font-size: .75rem;
    letter-spacing: .18em;
    text-transform: uppercase;
    color: #6758b4 !important;
    font-weight: 800;
    margin: 14px 0 5px;
}

/* ========== REPORT CARDS ========== */

.ts-report {
    background: #ffffff;
    border: 1px solid #e0e1ed;
    border-radius: 18px;
    padding: 22px;
    margin: 12px 0;
    min-height: 100px;
    box-shadow: 0 7px 20px #252c510a;
}

.ts-report strong {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.2rem;
    color: #28254b !important;
}

.ts-report p {
    color: #596579 !important;
    margin: 6px 0 0;
}

/* ========== DIVIDERS ========== */

hr {
    border-color: #dadde8 !important;
}

/* ========== RESPONSIVE ========== */

@media (max-width: 900px) {
    .block-container {
        padding: 1.4rem 1rem 3rem !important;
    }

    .tenderscope-hero {
        padding: 27px 22px;
    }

    .tenderscope-hero:after {
        opacity: .35;
    }
}

</style>
"""


def apply_theme():
    st.markdown(CSS, unsafe_allow_html=True)
