"""
Vacant property analysis for Open Data Syracuse 2024.

This script analyzes Syracuse vacant property records by ZIP code and creates
basic outputs that support the project README and GIS analysis.

Expected input:
    data/raw/Vacant_Properties.csv

Expected columns:
    Zip, Latitude, Longitude
"""

from pathlib import Path

import folium
import pandas as pd
from folium.plugins import MarkerCluster


RAW_DATA = Path("data/raw/Vacant_Properties.csv")
PROCESSED_DIR = Path("data/processed")
OUTPUT_DIR = Path("outputs")


def load_vacant_properties(path=RAW_DATA):
    """Load vacant property records."""
    if not path.exists():
        raise FileNotFoundError(
            f"Missing input file: {path}. Add the Open Data Syracuse vacant properties CSV to data/raw/."
        )
    return pd.read_csv(path)


def summarize_by_zip(vacant):
    """Create count and percentage summaries by ZIP code."""
    zip_counts = vacant["Zip"].value_counts().reset_index()
    zip_counts.columns = ["Zip", "count"]

    zip_percentages = vacant["Zip"].value_counts(normalize=True).reset_index()
    zip_percentages.columns = ["Zip", "proportion"]
    zip_percentages["percentage"] = (zip_percentages["proportion"] * 100).round(2)

    return zip_counts, zip_percentages


def create_marker_cluster_map(vacant):
    """Create an interactive Folium marker-cluster map of vacant properties."""
    mapped = vacant.dropna(subset=["Latitude", "Longitude"]).copy()

    syracuse_map = folium.Map(
        location=[43.03987633329929, -76.15437376017098],
        zoom_start=12,
    )

    marker_cluster = MarkerCluster()

    for _, row in mapped.iterrows():
        location = [row["Latitude"], row["Longitude"]]
        folium.Marker(location=location).add_to(marker_cluster)

    marker_cluster.add_to(syracuse_map)
    return syracuse_map


def main():
    """Run the vacant property workflow."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    vacant = load_vacant_properties()
    zip_counts, zip_percentages = summarize_by_zip(vacant)

    zip_counts.to_csv(PROCESSED_DIR / "vacant_properties_by_zip_count.csv", index=False)
    zip_percentages.to_csv(PROCESSED_DIR / "vacant_properties_by_zip_percentage.csv", index=False)

    marker_map = create_marker_cluster_map(vacant)
    marker_map.save(OUTPUT_DIR / "vacant_properties_marker_cluster.html")

    print("Analysis complete.")
    print(f"Wrote: {PROCESSED_DIR / 'vacant_properties_by_zip_count.csv'}")
    print(f"Wrote: {PROCESSED_DIR / 'vacant_properties_by_zip_percentage.csv'}")
    print(f"Wrote: {OUTPUT_DIR / 'vacant_properties_marker_cluster.html'}")


if __name__ == "__main__":
    main()
