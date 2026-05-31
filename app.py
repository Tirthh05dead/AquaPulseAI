import streamlit as st
import pandas as pd

from data import (
    load_station_data,
    load_forecast_data,
    load_ai_actions
)

from styles import load_theme

from components import (
    render_header,
    render_kpis,
    render_executive_summary,
    render_citizen_impact
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AquaPulse AI",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# LOAD THEME
# --------------------------------------------------

load_theme()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = load_station_data()

forecast_df = load_forecast_data()

action_df = load_ai_actions()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🚀 AquaPulse AI")

st.sidebar.markdown(
    """
    Smart Water Intelligence Platform

    Research Paper → Prototype
    """
)

scenario = st.sidebar.selectbox(
    "Simulation Scenario",
    [
        "Normal Conditions",
        "Heavy Rainfall",
        "Industrial Spill",
        "Pipe Leakage",
        "Extreme Drought"
    ]
)

# --------------------------------------------------
# AI SIMULATION ENGINE
# --------------------------------------------------

if scenario == "Normal Conditions":

    sim_ph = 7.1
    sim_tds = 110
    sim_turbidity = 2

elif scenario == "Heavy Rainfall":

    sim_ph = 6.4
    sim_tds = 210
    sim_turbidity = 6

elif scenario == "Industrial Spill":

    sim_ph = 5.1
    sim_tds = 450
    sim_turbidity = 9

elif scenario == "Pipe Leakage":

    sim_ph = 6.2
    sim_tds = 290
    sim_turbidity = 5

else:

    sim_ph = 5.5
    sim_tds = 380
    sim_turbidity = 7

# --------------------------------------------------
# AI RISK ENGINE
# --------------------------------------------------

health_score = 100

if sim_ph < 6:
    health_score -= 20

if sim_turbidity > 5:
    health_score -= 30

if sim_tds > 300:
    health_score -= 30

health_score = max(0, health_score)

contamination_probability = 0

if sim_turbidity > 5:
    contamination_probability += 40

if sim_tds > 300:
    contamination_probability += 30

if sim_ph < 6:
    contamination_probability += 30

contamination_probability = min(
    contamination_probability,
    100
)
# --------------------------------------------------
# RISK LEVEL
# --------------------------------------------------

if contamination_probability < 30:

    risk_level = "LOW"

elif contamination_probability < 60:

    risk_level = "MEDIUM"

else:

    risk_level = "HIGH"

# --------------------------------------------------
# WATER GRADE
# --------------------------------------------------

if health_score >= 90:

    water_grade = "A"

elif health_score >= 70:

    water_grade = "B"

elif health_score >= 50:

    water_grade = "C"

else:

    water_grade = "D"

# --------------------------------------------------
# POPULATION IMPACT MODEL
# --------------------------------------------------

if risk_level == "HIGH":

    population_impact = 8200

elif risk_level == "MEDIUM":

    population_impact = 4300

else:

    population_impact = 1200

# --------------------------------------------------
# AI CONFIDENCE ENGINE
# --------------------------------------------------

ai_confidence = 91

# --------------------------------------------------
# HEADER
# --------------------------------------------------

render_header()

# --------------------------------------------------
# COMMAND CENTER ALERT
# --------------------------------------------------

if risk_level == "HIGH":

    st.error(
        """
        🚨 CRITICAL WATER EVENT DETECTED

        AI has identified a high probability contamination event.

        Immediate intervention recommended.
        """
    )

elif risk_level == "MEDIUM":

    st.warning(
        """
        ⚠ Elevated contamination probability detected.

        Increase monitoring frequency.
        """
    )

else:

    st.success(
        """
        ✅ Water network operating normally.

        No critical contamination detected.
        """
    )

# --------------------------------------------------
# KPI DASHBOARD
# --------------------------------------------------

render_kpis(
    health_score,
    contamination_probability,
    risk_level,
    water_grade,
    population_impact
)

# --------------------------------------------------
# CITIZEN IMPACT
# --------------------------------------------------

render_citizen_impact(
    population_impact
)

# --------------------------------------------------
# EXECUTIVE AI SUMMARY
# --------------------------------------------------

render_executive_summary(
    risk_level,
    contamination_probability
)

# --------------------------------------------------
# AI CONFIDENCE
# --------------------------------------------------

st.header("🤖 AI Confidence Engine")

st.progress(
    ai_confidence / 100
)

st.write(
    f"Prediction Confidence: {ai_confidence}%"
)

st.divider()
import plotly.express as px
import folium
from streamlit_folium import st_folium

# --------------------------------------------------
# WATER NETWORK MAP
# --------------------------------------------------

st.header(
    "🌍 Smart Water Network"
)

m = folium.Map(
    location=[12.978,77.60],
    zoom_start=12
)

for _, row in df.iterrows():

    color = (
        "red"
        if row["Turbidity"] > 5
        else "green"
    )

    folium.Marker(

        [
            row["Latitude"],
            row["Longitude"]
        ],

        popup=
        f"""
        {row['Station']}
        """,

        icon=
        folium.Icon(
            color=color
        )

    ).add_to(m)

st_folium(
    m,
    height=500,
    width=1200
)

st.divider()

# --------------------------------------------------
# ANALYTICS
# --------------------------------------------------

st.header(
    "📈 Water Analytics"
)

left,right = st.columns(2)

with left:

    fig1 = px.bar(

        df,

        x="Station",

        y="TDS",

        title=
        "TDS Distribution"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with right:

    fig2 = px.line(

        df,

        x="Station",

        y="Turbidity",

        markers=True,

        title=
        "Contamination Trend"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# AI PRIORITY ACTIONS
# --------------------------------------------------

st.header(
    "🚨 AI Priority Actions"
)

st.dataframe(
    action_df,
    use_container_width=True
)

st.divider()
# --------------------------------------------------
# WATER DEMAND FORECAST
# --------------------------------------------------

st.header(
    "🔮 AI Demand Forecasting Engine"
)

forecast_fig = px.area(

    forecast_df,

    x="Day",

    y="Demand",

    title=
    "Predicted Weekly Water Demand",

)

forecast_fig.update_layout(

    template="plotly_dark",

    paper_bgcolor="#020617",

    plot_bgcolor="#020617"

)

st.plotly_chart(

    forecast_fig,

    use_container_width=True

)

st.divider()

# --------------------------------------------------
# SDG IMPACT DASHBOARD
# --------------------------------------------------

st.header(
    "🌍 Sustainable Development Goals"
)

sdg1, sdg2, sdg3, sdg4 = st.columns(4)

sdg1.metric(

    "SDG 6",

    "Clean Water"

)

sdg2.metric(

    "Water Saved",

    "18,000 L"

)

sdg3.metric(

    "Disease Prevention",

    "+24%"

)

sdg4.metric(

    "Community Reach",

    "8.2K"

)

st.divider()

# --------------------------------------------------
# CARBON INTELLIGENCE
# --------------------------------------------------

st.header(
    "♻ Carbon & Sustainability Intelligence"
)

carbon1, carbon2, carbon3 = st.columns(3)

carbon1.metric(

    "Carbon Reduction",

    "14%"

)

carbon2.metric(

    "Leak Reduction",

    "22%"

)

carbon3.metric(

    "Energy Savings",

    "19%"

)

st.progress(0.82)

st.write(
    "Overall Sustainability Index: 82/100"
)

st.divider()

# --------------------------------------------------
# DIGITAL TWIN STATUS
# --------------------------------------------------

st.header(
    "🏙 Smart City Digital Twin"
)

digital_df = pd.DataFrame({

    "Infrastructure":[
        "Water Network",
        "Treatment Plant",
        "Distribution Line",
        "Emergency Unit",
        "Sensor Grid"
    ],

    "Status":[
        "Operational",
        "Operational",
        "Monitoring",
        "Ready",
        "Active"
    ],

    "Health":[
        96,
        92,
        88,
        95,
        91
    ]
})

st.dataframe(

    digital_df,

    use_container_width=True

)

st.divider()

# --------------------------------------------------
# RISK RANKING ENGINE
# --------------------------------------------------

st.header(
    "🏆 AI Risk Ranking Engine"
)

risk_df = df.copy()

risk_df["Risk Score"] = (

    risk_df["Turbidity"] * 10

    +

    risk_df["TDS"] / 10

)

risk_df = risk_df.sort_values(

    by="Risk Score",

    ascending=False

)

st.dataframe(

    risk_df[
        [
            "Station",
            "Risk Score"
        ]
    ],

    use_container_width=True

)

st.divider()

# --------------------------------------------------
# RESEARCH IMPACT
# --------------------------------------------------

st.header(
    "📚 Research → Prototype Transformation"
)

st.success(
    """
    Original Research Focus:
    IoT-Based Water Quality Monitoring

    Prototype Innovation:

    • AI Risk Prediction

    • Smart Water Intelligence

    • Sustainability Analytics

    • Digital Twin Visualization

    • Citizen Impact Modeling

    • Decision Support System

    • SDG Alignment
    """
)

st.divider()

# --------------------------------------------------
# FUTURE AI MODULES
# --------------------------------------------------

st.header(
    "🚀 Future AI Modules"
)

future_df = pd.DataFrame({

    "Module":[

        "Satellite Monitoring",

        "Drone Inspection",

        "Flood Prediction",

        "Generative AI Reports",

        "IoT Live Sensors"

    ],

    "Status":[

        "Planned",

        "Planned",

        "In Development",

        "Prototype",

        "Next Phase"

    ]
})

st.dataframe(

    future_df,

    use_container_width=True

)

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    
    <h2 style="color:#00e5ff;">

    🌊 AquaPulse AI

    </h2>

    <p>

    Smart Water Intelligence &
    Sustainability Command Center

    </p>

    <p>

    Research Paper ➜ Prototype

    </p>

    <p>

    AI Risk Prediction • Smart Cities • SDG Impact

    </p>

    </div>
    """,

    unsafe_allow_html=True
)