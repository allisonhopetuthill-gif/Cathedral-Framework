import streamlit as st
import pandas as pd
import json
import time
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

LOG_FILE = "cathedral_chronicle.jsonl"

st.set_page_config(page_title="Cathedral Dashboard", layout="wide")
st.title("⛪ Cathedral Deployment Kit Dashboard v10.2.3")

st.sidebar.header("Controls")
auto_refresh = st.sidebar.checkbox("Auto-Refresh", value=True)
refresh_rate = st.sidebar.slider("Refresh Rate (sec)", 1, 10, 3)

@st.cache_data(ttl=refresh_rate)
def load_logs():
    path = Path(LOG_FILE)
    if not path.exists():
        return pd.DataFrame(columns=["timestamp","event","details","severity","extra"])
    with open(LOG_FILE, "r") as f:
        rows = [json.loads(line.strip()) for line in f if line.strip()]
    return pd.DataFrame(rows)

while True:
    df = load_logs()

    if df.empty:
        st.warning("No logs yet... Run choir.py to generate entries.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Recent Events")
            st.dataframe(df.tail(15)[["timestamp","event","details","severity"]])

            st.subheader("Event Severity Overview")
            severity_count = df["severity"].value_counts()
            st.bar_chart(severity_count)

        with col2:
            st.subheader("Risk Heatmap")
            if "EthicalScalability" in df["event"].values:
                risks = [row["extra"].get("compliance", 1.0) for _, row in df[df["event"]=="EthicalScalability"].iterrows()]
                if risks:
                    fig, ax = plt.subplots()
                    heatmap = ax.imshow(np.array(risks).reshape(1, -1), cmap="RdYlGn", aspect="auto")
                    ax.set_xticks(range(len(risks)))
                    ax.set_yticks([])
                    plt.colorbar(heatmap)
                    st.pyplot(fig)

            st.subheader("Individuation Velocity Trend")
            vel_records = df[df["event"]=="IndividuationVelocity"]
            if not vel_records.empty:
                velocities = [row["extra"].get("velocity", 0) for _, row in vel_records.iterrows()]
                if velocities:
                    st.line_chart(pd.Series(velocities, name="Velocity"))

        st.subheader("Integrity Metrics")
        eir_records = df[df["event"].isin(["EIRCheck","IntegrityCheck"])]
        if not eir_records.empty:
            eir_scores = [rec["extra"].get("eir") for rec in eir_records.to_dict(orient="records") if rec["extra"].get("eir") is not None]
            if eir_scores:
                st.line_chart(pd.Series(eir_scores, name="EIR Trend"))

        warnings = df[df["event"]=="FatigueWarning"]
        if not warnings.empty:
            st.error(f"⚠️ Compassion Fatigue Signals: {len(warnings)} instances detected.")

        conflicts = df[df["event"]=="PluralityConflict"]
        if not conflicts.empty:
            st.warning(f"🌀 Plurality Conflicts awaiting A-Team review: {len(conflicts)}")

        new_events = df["event"].isin(["ArchetypalHarmony", "ShadowEcho", "IndividuationVelocity", "EthicalScalability", "TrustBreachNeutralizer", "BylawReceiptDropper", "MultiLensValidator"])
        if new_events.sum() > 0:
            st.success(f"🆕 New/Backfilled Filters Active: {new_events.sum()} events logged.")

    if not auto_refresh:
        break
    time.sleep(refresh_rate)
    st.rerun()
