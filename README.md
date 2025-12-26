# 🎬 Netflix Insights: End-to-End Content Analytics Dashboard

An interactive, high-performance data analytics dashboard designed to decode Netflix's content strategy. This project transforms raw CSV data into actionable insights through a modular Python backend and a sleek Streamlit frontend, featuring real-time IMDb integration via the OMDb API.

---

## 🚀 Project Overview

This isn't just a visualization tool; it’s a full data pipeline. The project analyzes Netflix’s global catalog to uncover shift-trends in streaming behavior, genre dominance, and production hotspots.

**The Challenge:** Handling missing data in large catalogs and providing real-time metadata (IMDb ratings) that isn't available in the static dataset.

---

## ✨ Key Features

### 📊 Intelligent Analytics

* **Dynamic KPIs:** Instant snapshots of total titles, content distribution (Movies vs. TV), and temporal coverage.
* **Trend Mapping:** Longitudinal analysis of content growth and genre evolution using Seaborn/Matplotlib.
* **Geospatial Insights:** Identification of top-producing nations and regional content preferences.

### 🔍 Advanced Search & Integration

* **Smart Querying:** Case-insensitive, partial-match search engine for the Netflix catalog.
* **Live API Enrichment:** Real-time data fetching from **OMDb API** to provide live IMDb ratings, voter sentiment, and exact runtimes.

### 🛠️ Professional Architecture

* **Modular Design:** Separated concerns (Cleaning, EDA, API handling) for scalability.
* **Clean UI/UX:** A multi-tab interface designed for clarity and ease of navigation.

---

## 🧰 Tech Stack

| Category | Tools |
| --- | --- |
| **Language** | Python 3.9+ |
| **Data Engineering** | Pandas, NumPy |
| **Visualization** | Seaborn, Matplotlib |
| **Interface** | Streamlit |
| **External API** | OMDb (RESTful API) |

---

## 📦 Libraries & Purpose

| Library      | Why it’s Used |
|-------------|---------------|
| **pandas** | Data loading, cleaning, filtering, and transformation |
| **numpy** | Numerical computations such as percentages and statistics |
| **matplotlib** | Base plotting library for charts |
| **seaborn** | Advanced and styled data visualizations |
| **streamlit** | Building the interactive web dashboard |
| **requests** | Fetching IMDb data using the OMDb API |

---

## 📂 Architecture & Structure

```text
netflix-dashboard/
├── app.py                # Main Entry Point (Streamlit UI)
├── src/
│   ├── data_cleaning.py  # Script for handling nulls and type casting
│   ├── eda.py            # Core statistical analysis logic
│   ├── api_handler.py    # Robust OMDb API wrapper & error handling
│   └── utils.py          # Helper functions for UI/Formatting
├── data/
│   ├── raw/              # Immutable raw dataset
│   └── processed/        # Cleaned CSV for production use
├── requirements.txt      # Reproducible environment dependencies
└── README.md

```

---

## ⚙️ Installation & Setup

1. **Clone & Navigate**
```bash
git clone https://github.com/your-username/netflix-dashboard.git
cd netflix-dashboard

```


2. **Environment Configuration**
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

```


3. **API Configuration**
* Get a free key at [OMDbAPI.com](https://www.omdbapi.com/).
* Create a `.env` file or update `src/api_handler.py` with your `API_KEY`.


4. **Launch Application**
```bash
streamlit run app.py

```



---

## 🎯 Technical Achievements

* **Data Integrity:** Implemented a cleaning pipeline that handled ~30% missing values in "Director" and "Cast" columns without losing significant data points.
* **Performance:** Optimized Streamlit caching (`@st.cache_data`) to ensure sub-second page loads.
* **Extensibility:** Built the API handler to be rate-limit aware, preventing app crashes during high-frequency searching.

---

## 👤 Author

**Vinay Mishra** *MCA (Integrated) | Data Analytics & Python Specialist*

