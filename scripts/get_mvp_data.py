import pandas as pd
import time

all_mvp_data = []

columns_to_keep = [
    "Rank",
    "Name",
    "Tm",
    "Vote Pts",
    "1st Place",
    "Share",
    "WAR",
    "AB",
    "R",
    "HR",
    "RBI",
    "SB",
    "BA",
    "OBP",
    "SLG",
    "OPS"
]

for year in range(1980, 2026):

    print(f"Getting {year}...")

    url = f"https://www.baseball-reference.com/awards/awards_{year}.shtml"

    try:
        tables = pd.read_html(url)

        # Table 0 = AL MVP
        # Table 1 = NL MVP
        al = tables[0]
        nl = tables[1]

        # Flatten column names
        al.columns = al.columns.get_level_values(1)
        nl.columns = nl.columns.get_level_values(1)

        # Keep only the columns we need
        al = al[columns_to_keep].copy()
        nl = nl[columns_to_keep].copy()

        # Add year and league
        al["Year"] = year
        al["League"] = "AL"

        nl["Year"] = year
        nl["League"] = "NL"

        # Add both leagues to our master list
        all_mvp_data.append(al)
        all_mvp_data.append(nl)

    except Exception as e:
        print(f"Problem with {year}: {e}")

    # Be respectful to Baseball-Reference's server
    time.sleep(3)

# Combine every season
mvp_data = pd.concat(all_mvp_data, ignore_index=True)

# Put Year and League first
column_order = [
    "Year",
    "League",
    "Rank",
    "Name",
    "Tm",
    "Vote Pts",
    "1st Place",
    "Share",
    "WAR",
    "AB",
    "R",
    "HR",
    "RBI",
    "SB",
    "BA",
    "OBP",
    "SLG",
    "OPS"
]

mvp_data = mvp_data[column_order]

# Save dataset
mvp_data.to_csv("mvp_voting_1980_2025.csv", index=False)

print("\nFinished!")
print("Number of rows:", len(mvp_data))
print("\nFirst 10 rows:")
print(mvp_data.head(10))
