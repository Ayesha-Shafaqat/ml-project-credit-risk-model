import streamlit as st
from prediction_helper import predict

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Credit Risk Modelling",
    page_icon="📊",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main Container */
.block-container {
    max-width: 1050px;
    padding-top: 1.5rem;
    padding-bottom: 1rem;
    margin: auto;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    color: #1f77b4;
    margin-bottom: 0px;
    margin-top: 14px;
}

.sub-title {
    text-align: center;
    color: #6b7280;
    font-size: 15px;
    margin-bottom: 20px;
}

/* Cards */
.card {
    background-color: #ffffff;
    padding: 14px 18px;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    margin-bottom: 15px;
}

/* Section Headers */
.section-header {
    font-size: 18px;
    font-weight: 600;
    color: #1f77b4;
    margin-bottom: 10px;
    border-left: 5px solid #1f77b4;
    padding-left: 10px;
}

/* Reduce Vertical Gaps */
div[data-testid="stVerticalBlock"] {
    gap: 0.55rem;
}

/* Button */
.stButton > button {
    background-color: #1f77b4;
    color: white;
    font-size: 17px;
    font-weight: 600;
    border-radius: 10px;
    height: 50px;
    border: none;
}

.stButton > button:hover {
    background-color: #155a8a;
    color: white;
}

/* Metric Cards */
[data-testid="stMetric"] {
    background: white;
    border-radius: 12px;
    padding: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

/* Label color */
div[data-testid="stTextInput"] label {
    color: #374151 !important;
    -webkit-text-fill-color: #374151 !important;
    opacity: 1 !important;
    font-weight: 500 !important;
}

         
div[data-testid="stTextInput"] input:disabled {
    color: #374151 !important;
    -webkit-text-fill-color: #374151 !important;
    opacity: 1 !important;
}

/* Increase spacing between form rows */
div[data-testid="stVerticalBlock"] {
    gap: 1.1rem !important;
}

     
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    "<div class='main-title'>📊 Credit Risk Modelling</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Predict loan default probability and evaluate borrower risk using Machine Learning</div>",
    unsafe_allow_html=True
)

# ---------------- INPUT SECTION ----------------


# Row 1
row1 = st.columns(3)

with row1[0]:
    age = st.number_input(
        'Age',
        min_value=18,
        max_value=100,
        step=1,
        value=28
    )

with row1[1]:
    income = st.number_input(
        'Income',
        min_value=0,
        value=1200000
    )

with row1[2]:
    loan_amount = st.number_input(
        'Loan Amount',
        min_value=0,
        value=2560000
    )

# Loan To Income Ratio
loan_to_income_ratio = loan_amount / income if income > 0 else 0

# Row 2
row2 = st.columns(3)


with row2[0]:
    st.text_input(
        "Loan to Income Ratio",
        value=f"{loan_to_income_ratio:.2f}",
        disabled=True       
    )


with row2[1]:
    loan_tenure_months = st.number_input(
        'Loan Tenure (Months)',
        min_value=0,
        step=1,
        value=36
    )

with row2[2]:
    avg_dpd_per_delinquency = st.number_input(
        'Avg DPD',
        min_value=0,
        value=20
    )

# Row 3
row3 = st.columns(3)

with row3[0]:
    delinquency_ratio = st.number_input(
        'Delinquency Ratio',
        min_value=0,
        max_value=100,
        step=1,
        value=30
    )

with row3[1]:
    credit_utilization_ratio = st.number_input(
        'Credit Utilization Ratio',
        min_value=0,
        max_value=100,
        step=1,
        value=30
    )

with row3[2]:
    num_open_accounts = st.number_input(
        'Open Loan Accounts',
        min_value=1,
        max_value=4,
        step=1,
        value=2
    )

# Row 4
row4 = st.columns(3)

with row4[0]:
    residence_type = st.selectbox(
        'Residence Type',
        ['Owned', 'Rented', 'Mortgage']
    )

with row4[1]:
    loan_purpose = st.selectbox(
        'Loan Purpose',
        ['Education', 'Home', 'Auto', 'Personal']
    )

with row4[2]:
    loan_type = st.selectbox(
        'Loan Type',
        ['Unsecured', 'Secured']
    )

# ---------------- BUTTON ----------------
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    calculate = st.button(
        "🔍 Calculate Credit Risk",
        use_container_width=True
    )

# ---------------- PREDICTION ----------------
if calculate:

    probability, credit_score, rating = predict(
        age,
        income,
        loan_amount,
        loan_tenure_months,
        avg_dpd_per_delinquency,
        delinquency_ratio,
        credit_utilization_ratio,
        num_open_accounts,
        residence_type,
        loan_purpose,
        loan_type
    )

    st.markdown("### 📈 Risk Assessment Result")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Default Probability",
            f"{probability:.2%}"
        )

    with c2:
        st.metric(
            "Credit Score",
            credit_score
        )

    with c3:
        st.metric(
            "Risk Rating",
            rating
        )

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown(
    "<p style='text-align:center;color:gray;font-size:12px;'>"
    "Credit Risk Modelling | Built with Machine Learning & Streamlit"
    "</p>",
    unsafe_allow_html=True
)

