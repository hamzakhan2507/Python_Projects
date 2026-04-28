"""
Prepare Census ACS demographic and income data for the Open Data Syracuse 2024 project.

This script downloads block-group-level data for Onondaga County, New York,
cleans demographic and income fields, creates derived indicators, and exports a
CSV for GIS analysis.

Do not hard-code a Census API key in this file. If needed, set it as an
environment variable named CENSUS_API_KEY.
"""

import os
from pathlib import Path

import pandas as pd
import requests


ACS_URL = "https://api.census.gov/data/2022/acs/acs5"
OUTPUT_FILE = Path("data/processed/income_race.csv")

VARIABLES = [
    "NAME",
    "B20002_001E",
    "B02001_001E",
    "B02001_002E",
    "B02001_003E",
    "B19013_001E",
]

COLUMN_NAMES = {
    "B20002_001E": "median_income",
    "B02001_001E": "total_population",
    "B02001_002E": "white_population",
    "B02001_003E": "black_population",
    "B19013_001E": "median_household_income",
}


def download_data():
    """Download ACS block-group-level data for Onondaga County, NY."""
    params = {
        "get": ",".join(VARIABLES),
        "for": "block group:*",
        "in": "state:36 county:067 tract:*",
    }

    census_api_key = os.getenv("CENSUS_API_KEY")
    if census_api_key:
        params["key"] = census_api_key

    response = requests.get(ACS_URL, params=params, timeout=30)
    response.raise_for_status()

    rows = response.json()
    return pd.DataFrame(rows[1:], columns=rows[0])


def clean_data(df):
    """Clean Census fields and create derived indicators."""
    df = df.rename(columns=COLUMN_NAMES).copy()

    numeric_cols = [
        "median_income",
        "total_population",
        "white_population",
        "black_population",
        "median_household_income",
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["people_of_color_population"] = df["total_population"] - df["white_population"]
    df["people_of_color_share"] = df["people_of_color_population"] / df["total_population"]
    df["black_population_share"] = df["black_population"] / df["total_population"]

    df["GEOID"] = (
        df["state"].astype(str)
        + df["county"].astype(str)
        + df["tract"].astype(str)
        + df["block group"].astype(str)
    )

    return df


def main():
    """Run the Census demographic workflow."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    raw_data = download_data()
    cleaned_data = clean_data(raw_data)

    cleaned_data.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
