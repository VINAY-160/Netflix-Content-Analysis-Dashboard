import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from src.api_handler import get_movie_rating

# ================= CONFIG =================
st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    layout="wide",
    page_icon="🎬"
)

# ---------- COLORS ----------
NETFLIX_RED = "#E50914"
ORANGE = "#F5A623"
GRAY = "#333333"

sns.set_theme(style="whitegrid")

# ---------- TAB CSS ----------
st.markdown(
    """
    <style>
    button[data-baseweb="tab"] {
        font-size: 18px;
        padding: 12px 22px;
        min-height: 55px;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        border-bottom: 4px solid #E50914;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================= DATA =================
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "processed" / "netflix_cleaned.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# ================= HEADER =================
st.title("🎬 Netflix Content Analysis Dashboard")
st.caption("Python • Pandas • NumPy • Seaborn • Streamlit")

# ================= SIDEBAR =================
st.sidebar.header("🔍 Filters")

content_type = st.sidebar.radio(
    "Content Type",
    ["All", "Movie", "TV Show"]
)

year_range = st.sidebar.slider(
    "Year Added",
    int(df["year_added"].min()),
    int(df["year_added"].max()),
    (2015, int(df["year_added"].max()))
)

# ================= FILTERING =================
filtered_df = df.copy()

if content_type != "All":
    filtered_df = filtered_df[filtered_df["type"] == content_type]

filtered_df = filtered_df[
    (filtered_df["year_added"] >= year_range[0]) &
    (filtered_df["year_added"] <= year_range[1])
]

# ================= TABS (CORRECT PLACE) =================
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "📊 Dashboard",
        "🎭 Genres",
        "🌍 Countries",
        "🔎 Search Netflix",
        "⭐ IMDb Search"
    ]
)

# ================= TAB 1: DASHBOARD =================
with tab1:
    st.subheader("📊 Dashboard Overview")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🎬 Total Titles", len(filtered_df))
    c2.metric("🎥 Movies", (filtered_df["type"] == "Movie").sum())
    c3.metric("📺 TV Shows", (filtered_df["type"] == "TV Show").sum())
    c4.metric("📅 Years Covered", filtered_df["year_added"].nunique())

    st.divider()

    fig, ax = plt.subplots()
    sns.countplot(
        x="type",
        data=filtered_df,
        hue="type",
        palette={"Movie": NETFLIX_RED, "TV Show": ORANGE},
        legend=False,
        ax=ax
    )
    ax.set_title("Movies vs TV Shows", color=GRAY)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    filtered_df.groupby("year_added").size().plot(
        kind="line",
        color=NETFLIX_RED,
        linewidth=3,
        marker="o",
        ax=ax
    )
    ax.set_title("Content Growth Over Years", color=GRAY)
    st.pyplot(fig)

# ================= TAB 2: GENRES =================
with tab2:
    genres = filtered_df["listed_in"].str.split(", ").explode()
    top_genres = genres.value_counts().head(10)

    fig, ax = plt.subplots()
    sns.barplot(
        x=top_genres.values,
        y=top_genres.index,
        palette="Blues_r",
        ax=ax
    )
    ax.set_title("Top 10 Genres", color=GRAY)
    st.pyplot(fig)

# ================= TAB 3: COUNTRIES =================
with tab3:
    countries = filtered_df["country"].str.split(", ").explode()
    top_countries = countries.value_counts().head(10)

    fig, ax = plt.subplots()
    sns.barplot(
        x=top_countries.values,
        y=top_countries.index,
        palette="Oranges_r",
        ax=ax
    )
    ax.set_title("Top 10 Content Producing Countries", color=GRAY)
    st.pyplot(fig)

# ================= TAB 4: DATASET SEARCH =================
with tab4:
    query = st.text_input(
        "Search Netflix title",
        placeholder="e.g. Dark, Money, Avengers"
    )

    if query:
        results = filtered_df[
            filtered_df["title"].str.contains(query, case=False, na=False)
        ]

        st.write(f"🔍 Found {len(results)} titles")
        st.dataframe(
            results[
                ["title", "type", "release_year", "rating", "country"]
            ]
            .sort_values(by="release_year", ascending=False)
            .head(20)
        )

# ================= TAB 5: IMDb SEARCH =================
with tab5:
    movie = st.text_input(
        "Enter exact movie title",
        placeholder="e.g. Inception"
    )

    @st.cache_data(show_spinner=False)
    def fetch_imdb(title):
        return get_movie_rating(title)

    if movie:
        with st.spinner("Fetching IMDb data..."):
            data = fetch_imdb(movie)

        if data:
            c1, c2, c3 = st.columns(3)
            c1.metric("⭐ Rating", data["imdb_rating"])
            c2.metric("🗳 Votes", data["imdb_votes"])
            c3.metric("⏱ Runtime", data["runtime"])
        else:
            st.warning("Movie not found or API limit reached.")

# ================= FOOTER =================
st.divider()
st.caption("📌 Project by Vinay Mishra | Netflix Data Analytics Dashboard")
