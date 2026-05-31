import streamlit as st

def render_header():

    st.markdown(
        """
        <div class='main-title'>

        🌊 AquaPulse AI

        </div>

        <div class='sub-title'>

        Smart Water Intelligence
        & Sustainability Command Center

        </div>
        """,

        unsafe_allow_html=True
    )

    st.divider()


def render_kpis(
    health_score,
    contamination_probability,
    risk_level,
    water_grade,
    population_impact
):

    st.header(
        "📊 Smart City Command Dashboard"
    )

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric(
        "Health Score",
        f"{health_score}/100"
    )

    c2.metric(
        "AI Probability",
        f"{contamination_probability}%"
    )

    c3.metric(
        "Risk Level",
        risk_level
    )

    c4.metric(
        "Water Grade",
        water_grade
    )

    c5.metric(
        "Population Impact",
        population_impact
    )

    st.divider()


def render_citizen_impact(
    population_impact
):

    st.header(
        "👥 Citizen Impact Intelligence"
    )

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Citizens Protected",
        population_impact
    )

    c2.metric(
        "Disease Reduction",
        "24%"
    )

    c3.metric(
        "Emergency Response",
        "18 mins"
    )

    st.divider()


def render_executive_summary(
    risk_level,
    contamination_probability
):

    st.header(
        "🧠 Executive AI Summary"
    )

    if risk_level == "HIGH":

        st.error(
            f"""
            Critical contamination probability detected.

            Risk Score:
            {contamination_probability}%

            Immediate intervention required.
            """
        )

    elif risk_level == "MEDIUM":

        st.warning(
            f"""
            Moderate contamination probability.

            Risk Score:
            {contamination_probability}%

            Increased monitoring advised.
            """
        )

    else:

        st.success(
            """
            Water network operating normally.

            Continue routine monitoring.
            """
        )

    st.divider()