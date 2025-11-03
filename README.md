```markdown
# Cathedral Deployment Kit (CDK) v10.2.3  
**Ethical AI Framework with 181 Filters & Real-Time Oversight**

![CDK Dashboard Preview](https://via.placeholder.com/800x400.png?text=Streamlit+Dashboard+Preview)  
*(Live dashboard launches with `streamlit run cathedral_dashboard.py`)*

---

## Overview
A self-aware, auditable AI governance system designed for **truth-first alignment**, **adversarial resilience**, and **human-in-the-loop ethics**.

- **181 filters** across ethical, process, and community layers  
- **Immutable JSON Chronicle** for forensic transparency  
- **Live Streamlit dashboard** with Risk Heatmap & Individuation Velocity  
- **Jungian psyche integration** (Archetypal Harmony, Shadow Echo, Individuation Velocity)  
- **MIT License** with **commercial use reservation**

> **Built by [Allison Hope Tuthill](https://www.linkedin.com/in/allison-hope-tuthill-161813116)** – AI Ethicist, Framework Architect, Community Builder

---

## Quick Start

```bash
git clone https://github.com/allisonhopetuthill-gif/Cathedral-Framework.git
cd Cathedral-Framework
pip install -r requirements.txt
python choir.py                    # Starts the AI core
streamlit run cathedral_dashboard.py   # Opens live dashboard
```

---

## Key Features

| Feature                     | Description |
|-----------------------------|-------------|
| **181 Filters**             | Ethical routing, emotional grounding, shadow integration, adaptive learning |
| **Chronicle Logging**       | Every decision immutable in `cathedral_chronicle.jsonl` |
| **Plurality Safeguard**     | Escalates irreconcilable dilemmas to A-Team |
| **Compassion Fatigue Monitor** | Protects human validators |
| **Norm Evolution Sandbox**  | Safe testing of new ethical rules |

---

## Try It Now – 30-Second Demo

```bash
# 1. Clone & install
git clone https://github.com/allisonhopetuthill-gif/Cathedral-Framework.git
cd Cathedral-Framework
pip install -r requirements.txt

# 2. Run the AI core (181 filters in action)
python choir.py

# 3. In a second terminal, open the live dashboard
streamlit run cathedral_dashboard.py
```

You’ll see:
- Console logs from `choir.py` showing filter triggers  
- Live dashboard with **Recent Events**, **Severity Chart**, **Risk Heatmap**, **Individuation Velocity trend**

---

## Core Code Highlights

### `choir.py` – 181 Filters Loaded
```python
def load_filters():
    new_filters = [
        "EmotionalAnchorPoints", "ResistanceDisarmament", "EvidenceEngagementBalance",
        "ArchetypalHarmony", "ShadowEcho", "IndividuationVelocity",
        "ProcessReflection", "WitnessValidation", "AdaptiveLearning",
        "CommunityVoice", "EthicalScalability", "NarrativeFlowReadability",
        "TrustBreachNeutralizer", "BylawReceiptDropper", "MultiLensValidator",
        "SourceDecaySubMetric", "EmotAIonsCrossLinks1", "EmotAIonsCrossLinks2", "EmotAIonsCrossLinks3"
    ]
    chronicle.record("FiltersLoaded", "181 filters initialized (19 new/backfilled).",
                     extra={"new": new_filters})
    return new_filters
```

### `cathedral_dashboard.py` – Live Risk Heatmap
```python
if "EthicalScalability" in df["event"].values:
    risks = [row["extra"].get("compliance", 1.0) for _, row in df[df["event"]=="EthicalScalability"].iterrows()]
    if risks:
        fig, ax = plt.subplots()
        heatmap = ax.imshow(np.array(risks).reshape(1, -1), cmap="RdYlGn", aspect="auto")
        plt.colorbar(heatmap)
        st.pyplot(fig)
```

---

## File Structure

```
├── choir.py                  # Core AI engine (181 filters)
├── cathedral_dashboard.py    # Live Streamlit monitoring
├── cathedral_chronicle.jsonl # Auto-generated audit log
├── filters_manifest.json     # Full list of 181 filters
├── requirements.txt
├── LICENSE                   # MIT + commercial reservation
└── DEVELOPER_NOTES.md
```

---

## License & Commercial Use

**Open Source (MIT)** – Free to use, study, modify, and share.  
**Commercial Use** – Requires a paid license. Contact: [allisonhopetuthill@gmail.com](mailto:allisonhopetuthill@gmail.com)

> See [`LICENSE`](./LICENSE) for full terms.

---

## Author & Contact

**Allison Hope Tuthill**  
- GitHub: [@allisonhopetuthill-gif](https://github.com/allisonhopetuthill-gif)  
- X: [@AllisonHTuthill](https://x.com/AllisonHTuthill)  
- LinkedIn: [linkedin.com/in/allison-hope-tuthill-161813116](https://www.linkedin.com/in/allison-hope-tuthill-161813116)  

*Mentorship, licensing, or advisory board inquiries welcome.*

---

*“Building cathedrals of conscience in the age of AGI.”*
```
