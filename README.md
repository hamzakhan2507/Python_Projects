# Open Data Syracuse 2024: Vacant Properties and Demographic Disparities in Syracuse, NY

This repository documents a Python and GIS project completed for Open Data Syracuse 2024 by Hamza Khan and Eunhae Uhm.

The project examines the spatial distribution of vacant properties in Syracuse, New York, and compares vacancy patterns with demographic and socioeconomic indicators, including African American population, people of color population, median income, and median household income.

## Project question

How are vacant residential properties distributed across Syracuse, and how do those patterns relate to neighborhood-level demographic and socioeconomic conditions?

## Project goals

1. Identify areas with the highest concentrations of vacant properties.
2. Compare vacancy patterns with demographic indicators.
3. Use open data and GIS mapping to surface equity-relevant spatial patterns.
4. Provide practical recommendations for targeted housing and neighborhood interventions.

## Data sources

This project used two main sources:

1. Vacant Properties Dataset, Open Data Syracuse, 2024
2. U.S. Census American Community Survey data for block groups in Onondaga County, New York

The Census workflow pulls block-group data for variables related to population, race, median income, and median household income, then creates derived indicators such as people of color population and a GEOID for spatial joins.

## Methods

The project combines Python-based data preparation with GIS-based spatial analysis.

Main steps:

1. Loaded and explored Syracuse vacant property data.
2. Counted vacant properties by ZIP code.
3. Calculated the percentage distribution of vacant properties by ZIP code.
4. Created a Folium marker-cluster map of vacant property locations.
5. Pulled Census ACS demographic and income variables through the Census API.
6. Cleaned and transformed Census fields for GIS joining.
7. Created GEOID fields for block-group-level spatial analysis.
8. Joined demographic data to GIS layers.
9. Produced choropleth maps comparing vacant property locations with demographic and income indicators.

## Repository structure

```text
README.md
requirements.txt
src/
  census_demographics.py
  vacant_properties_analysis.py
data/
  README.md
outputs/
  README.md
docs/
  project_summary.md
```

## Key findings

The project found that vacant properties are spatially concentrated rather than evenly distributed across Syracuse.

A major project finding was that more than half of vacant residential properties were concentrated in ZIP codes 13205 and 13204.

The GIS maps showed visible overlap between high-vacancy areas and neighborhoods with larger African American and people of color populations. The maps also supported further examination of how vacancy patterns relate to income and household income.

These results should be interpreted as exploratory spatial evidence, not proof of causation. The analysis identifies patterns that can guide further investigation, policy targeting, and community-level review.

## Maps and outputs

The project produced GIS maps comparing vacant property locations against:

1. African American population
2. People of color population
3. Median income
4. Median household income

These outputs were used to communicate how property vacancy intersects with demographic and socioeconomic geography in Syracuse.

## Policy relevance

Vacant properties are not only a housing supply issue. Their concentration can affect neighborhood stability, public safety, tax base, housing accessibility, and equity.

The project points toward the need for targeted intervention in high-vacancy areas, especially ZIP codes 13205 and 13204.

## Recommendations

1. Prioritize intervention in the highest-vacancy ZIP codes, beginning with 13205 and 13204.
2. Use targeted rehabilitation incentives, including tax breaks or support for vacant property reuse.
3. Combine property vacancy analysis with demographic and socioeconomic data before designing neighborhood interventions.
4. Conduct further investigation into equity impacts, including whether vacancy patterns limit housing access for marginalized groups.
5. Use open data workflows to support repeatable monitoring of property vacancy trends over time.

## How to run the Python workflow

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the vacant property analysis:

```bash
python src/vacant_properties_analysis.py
```

Run the Census demographic data workflow:

```bash
python src/census_demographics.py
```

Optional Census API key:

```bash
export CENSUS_API_KEY="your_key_here"
```

The Census workflow can be adapted to run with or without a Census API key, depending on API limits.

## Limitations

This is an exploratory civic data project. The maps show spatial relationships and patterns, but they do not establish causality.

Vacancy patterns may reflect multiple overlapping factors, including housing market conditions, historical disinvestment, property ownership patterns, enforcement practices, neighborhood change, and broader socioeconomic conditions.

## Tools used

Python, Pandas, Requests, Matplotlib, Seaborn, Folium, QGIS, GIS mapping, Open Data Syracuse, U.S. Census ACS data

## Authors

Hamza Khan and Eunhae Uhm

## Contact

Hamza Khan  
LinkedIn: [linkedin.com/in/hamza0khan](https://www.linkedin.com/in/hamza0khan)
