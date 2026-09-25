import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="E-commerce Purchase Prediction",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Custom CSS – Light, professional, clean
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Global */
    .stApp {
        background: #f7f9fc;
    }
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* ---- Label visibility fix ---- */
    /* All widget labels (selectbox, etc.) */
    .stApp label,
    .stApp .stSelectbox label,
    .stApp .stTextInput label,
    .stApp .stNumberInput label,
    .stApp .stRadio label,
    .stApp .stCheckbox label,
    .stApp .stMultiSelect label {
        color: #1a2332 !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
        letter-spacing: 0.01em;
    }
    /* Streamlit's internal label container */
    div[data-testid="stWidgetLabel"] > label,
    div[data-testid="stWidgetLabel"] p {
        color: #1a2332 !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
    }
    /* Selectbox placeholder / selected value text */
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div {
        color: #1a2332 !important;
    }

    /* Header */
    .header-container {
        background: #ffffff;
        border-radius: 16px;
        padding: 1.75rem 2rem;
        border: 1px solid #e6eaf0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        margin-bottom: 1.5rem;
    }
    .header-title {
        font-size: 1.9rem;
        font-weight: 700;
        color: #1a2332;
        margin: 0 0 0.25rem 0;
        letter-spacing: -0.02em;
    }
    .header-subtitle {
        font-size: 1rem;
        color: #5a6a7e;
        margin: 0 0 0.9rem 0;
        font-weight: 400;
    }
    .header-badge {
        display: inline-block;
        background: #eef3fb;
        color: #2b5a9e;
        font-size: 0.78rem;
        font-weight: 600;
        padding: 0.3rem 0.85rem;
        border-radius: 20px;
        border: 1px solid #d4e0f0;
        letter-spacing: 0.02em;
    }

    /* Cards */
    .card {
        background: #ffffff;
        border-radius: 16px;
        padding: 1.5rem 1.75rem;
        border: 1px solid #e6eaf0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        margin-bottom: 1.25rem;
    }
    .card-title {
        font-size: 1.1rem;
        font-weight: 650;
        color: #1a2332 !important;
        margin: 0 0 1.1rem 0;
        padding-bottom: 0.65rem;
        border-bottom: 1px solid #eef2f7;
        letter-spacing: -0.01em;
    }

    /* Result cards */
    .result-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 1.5rem 1.75rem;
        border: 1px solid #e6eaf0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        margin-bottom: 1.25rem;
    }
    .result-card-success {
        border-left: 5px solid #2e7d32;
    }
    .result-card-warning {
        border-left: 5px solid #b26a00;
    }
    .result-label {
        font-size: 1.35rem;
        font-weight: 700;
        margin: 0 0 1rem 0;
        letter-spacing: -0.01em;
    }
    .result-label-success {
        color: #2e7d32;
    }
    .result-label-warning {
        color: #b26a00;
    }

    /* Metric row inside result */
    .metric-row {
        display: flex;
        gap: 1.5rem;
        flex-wrap: wrap;
        margin-top: 0.5rem;
    }
    .metric-item {
        flex: 1;
        min-width: 140px;
    }
    .metric-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #5a6a7e;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 0.2rem;
    }
    .metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a2332;
        letter-spacing: -0.02em;
    }
    .metric-value-small {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a2332;
    }

    /* Probability bar */
    .prob-bar-container {
        width: 100%;
        height: 14px;
        background: #eef2f7;
        border-radius: 8px;
        overflow: hidden;
        margin-top: 0.4rem;
    }
    .prob-bar-fill {
        height: 100%;
        border-radius: 8px;
        transition: width 0.3s ease;
    }

    /* Threshold note */
    .threshold-note {
        font-size: 0.85rem;
        color: #5a6a7e;
        margin-top: 0.5rem;
        line-height: 1.5;
    }
    .threshold-badge {
        display: inline-block;
        background: #f0f4fa;
        color: #3a5a8a;
        font-size: 0.8rem;
        font-weight: 600;
        padding: 0.2rem 0.65rem;
        border-radius: 6px;
        border: 1px solid #dce4f0;
    }

    /* Interpretation */
    .interpretation-text {
        font-size: 0.95rem;
        color: #3a4a5e;
        line-height: 1.65;
        margin: 0;
    }

    /* Model info */
    .model-info-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem 2rem;
    }
    .model-info-item {
        margin-bottom: 0.25rem;
    }
    .model-info-label {
        font-size: 0.78rem;
        font-weight: 600;
        color: #5a6a7e;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 0.15rem;
    }
    .model-info-value {
        font-size: 0.95rem;
        font-weight: 500;
        color: #1a2332;
    }

    /* Button */
    .stButton > button {
        background: #1a3a6b;
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 0.7rem 2rem;
        font-size: 1rem;
        font-weight: 600;
        letter-spacing: 0.01em;
        transition: background 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 2px 6px rgba(26, 58, 107, 0.2);
        width: 100%;
    }
    .stButton > button:hover {
        background: #142e55;
        box-shadow: 0 4px 12px rgba(26, 58, 107, 0.3);
    }
    .stButton > button:active {
        background: #0f2340;
    }

    /* Selectbox styling */
    .stSelectbox > div > div {
        border-radius: 8px;
        border-color: #dce4f0;
        background: #ffffff;
    }
    .stSelectbox > div > div:focus-within {
        border-color: #1a3a6b;
        box-shadow: 0 0 0 2px rgba(26, 58, 107, 0.12);
    }

    /* Responsive */
    @media (max-width: 768px) {
        .header-title { font-size: 1.5rem; }
        .metric-value { font-size: 1.25rem; }
        .model-info-grid { grid-template-columns: 1fr; }
        .block-container { padding-left: 1rem; padding-right: 1rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Load model (exact same path and method)
# ---------------------------------------------------------------------------
model = joblib.load("models/rf_purchase_model.pkl")

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="header-container">
        <div class="header-title">E-commerce Purchase Prediction</div>
        <div class="header-subtitle">Predict the probability of a customer session resulting in a purchase.</div>
        <span class="header-badge">Machine Learning &nbsp;|&nbsp; Random Forest</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Input Section
# ---------------------------------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">Customer Session Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    channel = st.selectbox(
        "Channel",
        ["Organic", "Paid Ads", "Social", "Email"],
        key="channel",
    )
    campaign_type = st.selectbox(
        "Campaign Type",
        ["New Launch", "Influencer", "Discount"],
        key="campaign_type",
    )
    device = st.selectbox(
        "Device",
        ["Mobile", "Desktop"],
        key="device",
    )
    user_type = st.selectbox(
        "User Type",
        ["New", "Returning"],
        key="user_type",
    )
    region = st.selectbox(
        "Region",
        ["Metro", "Non-Metro"],
        key="region",
    )

with col2:
    visited_website = st.selectbox(
        "Visited Website",
        ["Yes", "No"],
        key="visited_website",
    )
    viewed_product = st.selectbox(
        "Viewed Product",
        ["Yes", "No"],
        key="viewed_product",
    )
    added_to_cart = st.selectbox(
        "Added to Cart",
        ["Yes", "No"],
        key="added_to_cart",
    )
    checkout_started = st.selectbox(
        "Checkout Started",
        ["Yes", "No"],
        key="checkout_started",
    )

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Prediction Button
# ---------------------------------------------------------------------------
predict_clicked = st.button("Predict Purchase", key="predict_button")

# ---------------------------------------------------------------------------
# Prediction Logic (RESTORED working version)
# ---------------------------------------------------------------------------
if predict_clicked:
    # 1. Build raw_data from exact inputs
    raw_data = {
        "channel": [channel],
        "campaign_type": [campaign_type],
        "device": [device],
        "user_type": [user_type],
        "region": [region],
        "visited_website": [visited_website],
        "viewed_product": [viewed_product],
        "added_to_cart": [added_to_cart],
        "checkout_started": [checkout_started],
    }

    # 2. Create the DataFrame
    input_data = pd.DataFrame(raw_data)

    # 3. Convert categorical values into dummy variables
    input_data = pd.get_dummies(input_data)

    # 4. Align columns safely using reindex
    input_data = input_data.reindex(
        columns=model.feature_names_in_,
        fill_value=0,
    )

    # 5. Prediction
    probability = model.predict_proba(input_data)[0][1]

    # 6. Threshold (fixed, do not change)
    threshold = 0.92

    # 7. Prediction logic
    if probability >= threshold:
        purchase_predicted = True
        st.success("Purchase Predicted")
    else:
        purchase_predicted = False
        st.warning("No Purchase Predicted")

    # -----------------------------------------------------------------------
    # Visual Result Card
    # -----------------------------------------------------------------------
    if purchase_predicted:
        st.markdown(
            f"""
            <div class="result-card result-card-success">
                <div class="result-label result-label-success">Purchase Predicted</div>
                <div class="metric-row">
                    <div class="metric-item">
                        <div class="metric-label">Purchase Probability</div>
                        <div class="metric-value">{probability * 100:.2f}%</div>
                    </div>
                </div>
                <div class="prob-bar-container">
                    <div class="prob-bar-fill" style="width: {probability * 100:.2f}%; background: linear-gradient(90deg, #2e7d32, #43a047);"></div>
                </div>
                <div class="threshold-note">
                    <span class="threshold-badge">Decision Threshold: 92%</span>
                    &nbsp; Purchase is predicted when the model probability is at least 92%.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="result-card result-card-warning">
                <div class="result-label result-label-warning">No Purchase Predicted</div>
                <div class="metric-row">
                    <div class="metric-item">
                        <div class="metric-label">Purchase Probability</div>
                        <div class="metric-value">{probability * 100:.2f}%</div>
                    </div>
                </div>
                <div class="prob-bar-container">
                    <div class="prob-bar-fill" style="width: {probability * 100:.2f}%; background: linear-gradient(90deg, #b26a00, #e69500);"></div>
                </div>
                <div class="threshold-note">
                    <span class="threshold-badge">Decision Threshold: 92%</span>
                    &nbsp; Purchase is predicted when the model probability is at least 92%.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -----------------------------------------------------------------------
    # Prediction Summary
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Prediction Summary</div>', unsafe_allow_html=True)

    summary_col1, summary_col2, summary_col3 = st.columns(3)

    with summary_col1:
        st.markdown(
            f"""
            <div class="metric-item">
                <div class="metric-label">Prediction</div>
                <div class="metric-value-small">{'Purchase Predicted' if purchase_predicted else 'No Purchase Predicted'}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with summary_col2:
        st.markdown(
            f"""
            <div class="metric-item">
                <div class="metric-label">Probability</div>
                <div class="metric-value-small">{probability * 100:.2f}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with summary_col3:
        st.markdown(
            """
            <div class="metric-item">
                <div class="metric-label">Decision Threshold</div>
                <div class="metric-value-small">92%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------------
    # Business Interpretation
    # -----------------------------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Business Interpretation</div>', unsafe_allow_html=True)

    if purchase_predicted:
        interpretation = (
            "Based on the selected session characteristics, the model estimates a high likelihood of purchase."
        )
    else:
        interpretation = (
            "Based on the selected session characteristics, the model estimates that the session is below the purchase decision threshold."
        )

    st.markdown(f'<p class="interpretation-text">{interpretation}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Model Information (always visible at bottom)
# ---------------------------------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">Model Information</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="model-info-grid">
        <div class="model-info-item">
            <div class="model-info-label">Model</div>
            <div class="model-info-value">Random Forest Classifier</div>
        </div>
        <div class="model-info-item">
            <div class="model-info-label">Decision Threshold</div>
            <div class="model-info-value">92%</div>
        </div>
        <div class="model-info-item">
            <div class="model-info-label">Target</div>
            <div class="model-info-value">Purchase Completion</div>
        </div>
        <div class="model-info-item">
            <div class="model-info-label">Purpose</div>
            <div class="model-info-value">Predict purchase likelihood from customer session behavior and attributes.</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True) 