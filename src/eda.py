import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ---------------- THEME & COLORS ----------------
sns.set_theme(style="whitegrid")

NETFLIX_RED = "#E50914"
ORANGE = "#F5A623"
GRAY = "#333333"

# ---------------- PATHS ----------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "netflix_cleaned.csv"
ASSETS_DIR = BASE_DIR / "assets"
ASSETS_DIR.mkdir(exist_ok=True)

# ---------------- LOAD DATA ----------------
df = pd.read_csv(DATA_PATH)

# ---------------- MOVIES vs TV SHOWS ----------------
plt.figure(figsize=(6,4))
sns.countplot(
    x="type",
    data=df,
    hue="type",
    palette={
        "Movie": NETFLIX_RED,
        "TV Show": ORANGE
    },
    legend=False
)
plt.title("Movies vs TV Shows on Netflix", color=GRAY)
plt.tight_layout()
plt.savefig(ASSETS_DIR / "movies_vs_tv.png")
plt.show()

# ---------------- CONTENT GROWTH ----------------
yearly_content = df.groupby("year_added").size()

plt.figure(figsize=(8,4))
yearly_content.plot(
    kind="line",
    color=NETFLIX_RED,
    marker="o",
    linewidth=3
)
plt.title("Content Added Over Years", color=GRAY)
plt.tight_layout()
plt.savefig(ASSETS_DIR / "content_growth.png")
plt.show()

# ---------------- TOP GENRES ----------------
genres = df["listed_in"].str.split(", ").explode()
top_genres = genres.value_counts().head(10)

plt.figure(figsize=(8,4))
sns.barplot(
    x=top_genres.values,
    y=top_genres.index,
    palette="Blues_r"
)
plt.title("Top 10 Genres on Netflix", color=GRAY)
plt.tight_layout()
plt.savefig(ASSETS_DIR / "top_genres.png")
plt.show()

# ---------------- TOP COUNTRIES ----------------
countries = df["country"].str.split(", ").explode()
top_countries = countries.value_counts().head(10)

plt.figure(figsize=(8,4))
sns.barplot(
    x=top_countries.values,
    y=top_countries.index,
    palette="Oranges_r"
)
plt.title("Top 10 Content Producing Countries", color=GRAY)
plt.tight_layout()
plt.savefig(ASSETS_DIR / "top_countries.png")
plt.show()

# ---------------- RATING DISTRIBUTION ----------------
plt.figure(figsize=(6,4))
sns.countplot(
    y="rating",
    data=df,
    order=df["rating"].value_counts().index,
    palette="dark:red"
)
plt.title("Content Rating Distribution", color=GRAY)
plt.tight_layout()
plt.savefig(ASSETS_DIR / "ratings_distribution.png")
plt.show()
