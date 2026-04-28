# Data

This folder is intended for project datasets used in the Open Data Syracuse 2024 vacant properties analysis.

The project used:

1. Open Data Syracuse vacant properties data for Syracuse, New York.
2. U.S. Census ACS 5-year data for block-group-level demographic and income indicators in Onondaga County, New York.

Large raw datasets are not included here by default. If data files are added later, keep raw files in `data/raw/` and cleaned files in `data/processed/`.

Recommended structure:

```text
raw/          Original downloaded files
processed/    Cleaned CSV files used for mapping and analysis
```

The Census data preparation script creates a processed file called:

```text
data/processed/income_race.csv
```
