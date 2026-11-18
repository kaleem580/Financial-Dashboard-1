
import streamlit as st
import numpy_financial as npf
import plotly.graph_objects as go

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="FinEdge Financial Calculator",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# 2. CUSTOM CSS - COLORFUL INTERFACE AND ANIMATIONS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
    radial-gradient(circle at 10% 5%, rgba(64,110,255,.16), transparent 28%),
    radial-gradient(circle at 90% 10%, rgba(0,214,170,.12), transparent 25%),
    linear-gradient(135deg, #081226, #101b35, #0a1428);
    color: #f4f7ff;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #101d38, #0a1429);
    border-right: 1px solid rgba(255,255,255,.09);
}

/* Headings */

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #f5f7ff;
}

/* Main Header */

.hero {
    padding: 28px 30px;
    border-radius: 22px;
    margin-bottom: 22px;

    background: linear-gradient(
        115deg,
        rgba(44,92,220,.34),
        rgba(0,194,155,.18)
    );

    border: 1px solid rgba(255,255,255,.15);
    box-shadow: 0 15px 45px rgba(0,0,0,.18);

    animation: rise .75s ease-out both;
}

.hero h1 {
    margin: 0;
    font-size: 2.5rem;
    letter-spacing: -1.5px;
}

.hero p {
    color: #c5d2ee;
    margin-top: 8px;
    font-size: 1.02rem;
}

/* Animations */

@keyframes rise {
    from {
        opacity: 0;
        transform: translateY(18px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes glow {
    0%, 100% {
        box-shadow: 0 0 12px rgba(0,214,170,.08);
    }

    50% {
        box-shadow: 0 0 25px rgba(0,214,170,.28);
    }
}

/* Result Cards */

.metric-card {
    background: linear-gradient(
        145deg,
        rgba(29,47,82,.95),
        rgba(18,31,57,.95)
    );

    border: 1px solid rgba(145,175,235,.2);
    border-radius: 17px;

    padding: 17px 19px;
    min-height: 112px;

    animation: rise .55s ease-out both;
}

.metric-label {
    color: #aabbdc;
    font-size: .84rem;
    margin-bottom: 7px;
}

.metric-value {
    color: #fff;
    font-family: 'Space Grotesk';
    font-size: 1.65rem;
    font-weight: 700;
}

.metric-note {
    color: #7fe4ca;
    font-size: .78rem;
    margin-top: 4px;
}

/* Buttons */

div.stButton > button {
    background: linear-gradient(100deg, #456cff, #00b995);
    color: white;
    border: 0;
    border-radius: 11px;
    padding: .65rem 1.3rem;
    font-weight: 700;
    transition: all .2s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    filter: brightness(1.12);
    box-shadow: 0 8px 22px rgba(0,190,160,.2);
}

/* Tabs */

.stTabs [data-baseweb="tab"] {
    color: #c9d6f2;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    color: #75e5ce !important;
}

/* Inputs */

div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input {
    background: #111f3b;
    color: #f4f7ff;
    border-radius: 9px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# 3. HELPER FUNCTIONS
# =====================================================

def money(value, currency):
    """Format financial values."""
    return f"{currency} {value:,.2f}"


def metric(label, value, note=""):
    """Display attractive financial result cards."""

    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-label">
                {label}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-note">
                {note}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def show_result_chart(labels, values, title, currency=None):
    """Create interactive financial charts."""

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=labels,
            y=values,

            marker=dict(
                color=values,
                colorscale=[
                    [0, "#426bff"],
                    [1, "#00c6a0"]
                ]
            ),

            text=[
                f"{currency or ''}{v:,.2f}"
                for v in values
            ],

            textposition="outside"
        )
    )

    fig.update_layout(
        title=title,
        template="plotly_dark",
        height=340,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(color="#eaf0ff"),

        margin=dict(
            l=10,
            r=10,
            t=55,
            b=10
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# 4. MAIN HEADER
# =====================================================

st.markdown("""
<div class="hero">

    <h1>
        💹 FinEdge Financial Calculator
    </h1>

    <p>
        Make smarter financial decisions with clear
        calculations, interactive charts and an
        easy-to-use financial workspace.
    </p>

</div>
""", unsafe_allow_html=True)


# =====================================================
# 5. SIDEBAR SETTINGS
# =====================================================

with st.sidebar:

    st.markdown("## ⚙️ Calculator Settings")

    currency = st.selectbox(
        "Select Currency",

        [
            "PKR",
            "USD",
            "GBP",
            "EUR",
            "AED"
        ],

        index=0
    )

    st.markdown("---")

    st.markdown("### 🧭 Financial Tools")

    st.caption(
        "Choose your desired calculator "
        "from the main dashboard."
    )

    st.markdown("---")

    st.caption(
        "FinEdge Financial Calculator"
    )

    st.caption(
        "Designed for financial learning and analysis."
    )


# =====================================================
# 6. MAIN CALCULATOR TABS
# =====================================================

tab_tvm, tab_loan, tab_interest, tab_invest, tab_ratios = st.tabs(

    [
        "⏳ Time Value of Money",
        "🏠 Loan / EMI",
        "📈 Interest",
        "💼 Investment",
        "📊 Financial Ratios"
    ]

)


# =====================================================
# 7. TIME VALUE OF MONEY CALCULATOR
# =====================================================

with tab_tvm:

    st.subheader("Time Value of Money Calculator")

    st.caption(
        "Calculate Present Value, Future Value and "
        "Periodic Payments."
    )

    col1, col2 = st.columns(2)

    with col1:

        principal = st.number_input(
            "Payment / Cash Flow Amount",
            min_value=0.0,
            value=10000.0,
            step=500.0
        )

        annual_rate = st.number_input(
            "Annual Interest Rate (%)",
            min_value=0.0,
            value=10.0,
            step=0.5
        )

        years = st.number_input(
            "Number of Years",
            min_value=0.0,
            value=5.0,
            step=1.0
        )

    with col2:

        frequency = st.selectbox(
            "Payment Frequency",

            [
                "Annually",
                "Semi-annually",
                "Quarterly",
                "Monthly"
            ]
        )

        timing = st.radio(
            "Payment Timing",

            [
                "End of period (Ordinary Annuity)",
                "Beginning of period (Annuity Due)"
            ]
        )

        tvm_type = st.selectbox(
            "Select Calculation",

            [
                "Future Value (FV)",
                "Present Value (PV)",
                "Periodic Payment (PMT)"
            ]
        )

    periods_per_year = {
        "Annually": 1,
        "Semi-annually": 2,
        "Quarterly": 4,
        "Monthly": 12
    }[frequency]

    n = int(round(years * periods_per_year))

    r = annual_rate / 100 / periods_per_year

    due = 1 if timing.startswith("Beginning") else 0

    if st.button("Calculate TVM"):

        if n <= 0:

            st.error(
                "Please enter a number of years greater than zero."
            )

        else:

            if tvm_type.startswith("Future"):

                factor = (
                    ((1 + r) ** n - 1) / r
                    if r else n
                )

                result = principal * factor * (1 + r * due)

                st.success("Future Value Calculated!")

                metric(
                    "Future Value",
                    money(result, currency),
                    "FV of regular payments"
                )

            elif tvm_type.startswith("Present"):

                factor = (
                    (1 - (1 + r) ** (-n)) / r
                    if r else n
                )

                result = principal * factor * (1 + r * due)

                st.success("Present Value Calculated!")

                metric(
                    "Present Value",
                    money(result, currency),
                    "PV of regular payments"
                )

            else:

                factor = (
                    (1 - (1 + r) ** (-n)) / r
                    if r else n
                )

                factor *= (1 + r * due)

                result = principal / factor

                st.success("Periodic Payment Calculated!")

                metric(
                    "Periodic Payment",
                    money(result, currency),
                    f"Payment every {frequency.lower()} period"
                )

            st.info(
                "For FV and PV, the entered amount is treated "
                "as a regular payment. For PMT, it is treated "
                "as the target present value."
            )

            st.balloons()


# =====================================================
# 8. LOAN / EMI CALCULATOR
# =====================================================

with tab_loan:

    st.subheader("Loan Repayment Calculator")

    st.caption(
        "Calculate loan instalments, total repayment "
        "and total interest."
    )

    c1, c2 = st.columns(2)

    with c1:

        loan_amount = st.number_input(
            "Loan Amount",
            min_value=0.0,
            value=1000000.0,
            step=10000.0
        )

        loan_rate = st.number_input(
            "Annual Loan Interest Rate (%)",
            min_value=0.0,
            value=18.0,
            step=0.5
        )

    with c2:

        loan_years = st.number_input(
            "Loan Term (Years)",
            min_value=0.5,
            value=3.0,
            step=0.5
        )

        payments_year = st.selectbox(
            "Instalment Frequency",

            [
                "Monthly",
                "Quarterly",
                "Annually"
            ]
        )

    if st.button("Calculate Loan Instalment"):

        ppy = {
            "Monthly": 12,
            "Quarterly": 4,
            "Annually": 1
        }[payments_year]

        total_periods = int(round(loan_years * ppy))

        periodic_rate = loan_rate / 100 / ppy

        if loan_amount <= 0 or total_periods <= 0:

            st.error(
                "Enter a positive loan amount and loan term."
            )

        else:

            if periodic_rate == 0:

                emi = loan_amount / total_periods

            else:

                emi = (
                    loan_amount * periodic_rate /
                    (1 - (1 + periodic_rate) ** (-total_periods))
                )

            total_paid = emi * total_periods

            interest_paid = total_paid - loan_amount

            a, b, c = st.columns(3)

            with a:

                metric(
                    "Regular Instalment",
                    money(emi, currency),
                    payments_year
                )

            with b:

                metric(
                    "Total Repayment",
                    money(total_paid, currency),
                    f"{total_periods} instalments"
                )

            with c:

                metric(
                    "Total Interest",
                    money(interest_paid, currency),
                    "Estimated borrowing cost"
                )

            # Loan balance calculation

            balances = []

            balance = loan_amount

            for _ in range(total_periods):

                interest_part = balance * periodic_rate

                principal_part = min(
                    balance,
                    emi - interest_part
                )

                balance = max(
                    0,
                    balance - principal_part
                )

                balances.append(balance)

            # Loan chart

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    y=balances,
                    mode="lines",
                    name="Remaining Balance",
                    line=dict(
                        color="#00d1a4",
                        width=3
                    ),
                    fill="tozeroy"
                )
            )

            fig.update_layout(
                title="Loan Balance Over Time",
                template="plotly_dark",
                height=320,
                xaxis_title="Instalment Number",
                yaxis_title=currency
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.balloons()


# =====================================================
# 9. SIMPLE AND COMPOUND INTEREST
# =====================================================

with tab_interest:

    st.subheader("Simple and Compound Interest Calculator")

    c1, c2 = st.columns(2)

    with c1:

        deposit = st.number_input(
            "Initial Principal",
            min_value=0.0,
            value=100000.0,
            step=5000.0
        )

        rate = st.number_input(
            "Annual Interest Rate (%)",
            min_value=0.0,
            value=12.0,
            step=0.5,
            key="interest_rate"
        )

    with c2:

        duration = st.number_input(
            "Time (Years)",
            min_value=0.0,
            value=4.0,
            step=1.0
        )

        compound_frequency = st.selectbox(
            "Compounding Frequency",

            [
                "Annually",
                "Semi-annually",
                "Quarterly",
                "Monthly",
                "Daily"
            ]
        )

    if st.button("Calculate Interest"):

        # Simple Interest Formula:
        # SI = P x R x T

        simple_interest = (
            deposit *
            (rate / 100) *
            duration
        )

        # Compound Interest Formula:
        # FV = P(1 + r/m)^(mt)

        m = {
            "Annually": 1,
            "Semi-annually": 2,
            "Quarterly": 4,
            "Monthly": 12,
            "Daily": 365
        }[compound_frequency]

        compound_value = (
            deposit *
            (1 + rate / 100 / m) ** (m * duration)
        )

        compound_interest = (
            compound_value - deposit
        )

        x, y, z = st.columns(3)

        with x:

            metric(
                "Simple Interest",
                money(simple_interest, currency)
            )

        with y:

            metric(
                "Compound Interest",
                money(compound_interest, currency)
            )

        with z:

            metric(
                "Compound Future Value",
                money(compound_value, currency)
            )

        show_result_chart(

            [
                "Principal",
                "Simple FV",
                "Compound FV"
            ],

            [
                deposit,
                deposit + simple_interest,
                compound_value
            ],

            "Simple vs Compound Growth",

            currency + " "
        )

        st.balloons()


# =====================================================
# 10. INVESTMENT APPRAISAL
# =====================================================

with tab_invest:

    st.subheader("Investment Appraisal Calculator")

    st.caption(
        "Calculate NPV and IRR to evaluate investment projects."
    )

    initial_outflow = st.number_input(
        "Initial Investment",
        min_value=0.0,
        value=500000.0,
        step=10000.0
    )

    discount_rate = st.number_input(
        "Discount Rate (%)",
        min_value=0.0,
        value=12.0,
        step=0.5
    )

    number_flows = st.number_input(
        "Number of Annual Cash Flows",
        min_value=1,
        max_value=20,
        value=5,
        step=1
    )

    st.markdown(
        "**Enter Expected Cash Inflows for Each Year**"
    )

    flow_cols = st.columns(
        min(int(number_flows), 5)
    )

    cash_flows = []

    for i in range(int(number_flows)):

        with flow_cols[i % len(flow_cols)]:

            cash_flows.append(
                st.number_input(
                    f"Year {i + 1}",
                    min_value=0.0,
                    value=150000.0,
                    step=5000.0,
                    key=f"cashflow_{i}"
                )
            )

    if st.button("Evaluate Investment"):

        rate_decimal = discount_rate / 100

        # NPV Formula

        npv = (
            -initial_outflow
            +
            sum(
                cf / ((1 + rate_decimal) ** (i + 1))
                for i, cf in enumerate(cash_flows)
            )
        )

        # IRR Formula

        try:

            irr = float(
                npf.irr(
                    [-initial_outflow] + cash_flows
                )
            ) * 100

            irr_text = f"{irr:.2f}%"

        except (
            ValueError,
            TypeError,
            OverflowError
        ):

            irr = None
            irr_text = "Not Available"

        a, b = st.columns(2)

        with a:

            metric(
                "Net Present Value (NPV)",
                money(npv, currency),
                "Positive NPV generally indicates value creation"
            )

        with b:

            metric(
                "Internal Rate of Return (IRR)",
                irr_text,
                "Compared with the required return"
            )

        st.markdown("### Investment Decision")

        if npv > 0:

            st.success(
                "Positive NPV: The project is expected "
                "to add value at the selected discount rate."
            )

        elif npv < 0:

            st.warning(
                "Negative NPV: The project does not "
                "meet the selected required return."
            )

        else:

            st.info(
                "Zero NPV: The project exactly meets "
                "the selected required return."
            )

        st.balloons()


# =====================================================
# 11. FINANCIAL RATIO CALCULATOR
# =====================================================

with tab_ratios:

    st.subheader("Financial Ratio Calculator")

    st.caption(
        "Calculate important liquidity, leverage "
        "and profitability ratios."
    )

    ratio_choice = st.selectbox(

        "Select Financial Ratio",

        [
            "Current Ratio",
            "Quick Ratio",
            "Debt-to-Equity Ratio",
            "Net Profit Margin",
            "Return on Assets (ROA)",
            "Return on Equity (ROE)"
        ]

    )

    # LIQUIDITY RATIOS

    if ratio_choice in [
        "Current Ratio",
        "Quick Ratio"
    ]:

        current_assets = st.number_input(
            "Current Assets",
            min_value=0.0,
            value=500000.0
        )

        current_liabilities = st.number_input(
            "Current Liabilities",
            min_value=0.0,
            value=250000.0
        )

        inventory = 0.0

        if ratio_choice == "Quick Ratio":

            inventory = st.number_input(
                "Inventory",
                min_value=0.0,
                value=100000.0
            )

        if st.button("Calculate Ratio"):

            if current_liabilities == 0:

                st.error(
                    "Current liabilities cannot be zero."
                )

            else:

                if ratio_choice == "Current Ratio":

                    numerator = current_assets

                else:

                    numerator = (
                        current_assets - inventory
                    )

                result = (
                    numerator / current_liabilities
                )

                metric(
                    ratio_choice,
                    f"{result:.2f} : 1",
                    "Liquidity Measure"
                )

    # DEBT TO EQUITY

    elif ratio_choice == "Debt-to-Equity Ratio":

        debt = st.number_input(
            "Total Debt / Liabilities",
            min_value=0.0,
            value=600000.0
        )

        equity = st.number_input(
            "Total Shareholders' Equity",
            min_value=0.0,
            value=400000.0
        )

        if st.button("Calculate Ratio"):

            if equity == 0:

                st.error(
                    "Equity cannot be zero."
                )

            else:

                result = debt / equity

                metric(
                    "Debt-to-Equity Ratio",
                    f"{result:.2f} : 1",
                    "Capital Structure Measure"
                )

    # PROFITABILITY RATIOS

    else:

        if ratio_choice == "Net Profit Margin":

            profit = st.number_input(
                "Net Profit",
                min_value=0.0,
                value=120000.0
            )

            denominator = st.number_input(
                "Net Sales / Revenue",
                min_value=0.0,
                value=800000.0
            )

            label = "Net Profit Margin"

        elif ratio_choice == "Return on Assets (ROA)":

            profit = st.number_input(
                "Net Income",
                min_value=0.0,
                value=120000.0
            )

            denominator = st.number_input(
                "Average Total Assets",
                min_value=0.0,
                value=1000000.0
            )

            label = "Return on Assets (ROA)"

        else:

            profit = st.number_input(
                "Net Income",
                min_value=0.0,
                value=120000.0
            )

            denominator = st.number_input(
                "Average Shareholders' Equity",
                min_value=0.0,
                value=600000.0
            )

            label = "Return on Equity (ROE)"

        if st.button("Calculate Percentage"):

            if denominator == 0:

                st.error(
                    "The denominator cannot be zero."
                )

            else:

                result = (
                    profit / denominator
                ) * 100

                metric(
                    label,
                    f"{result:.2f}%",
                    "Profitability Measure"
                )


# =====================================================
# 12. FOOTER
# =====================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#91a5ca;
        padding:8px;
    ">

        <h3>💹 FinEdge Financial Calculator</h3>

        Built with Python, Streamlit and Plotly.

        <br>

        <small>
        For educational and estimation purposes only.
        Results depend on the assumptions and inputs provided.
        </small>

    </div>
    """,
    unsafe_allow_html=True
)

