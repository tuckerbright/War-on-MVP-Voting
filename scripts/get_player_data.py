import pandas as pd
import time

print("Getting historical MLB player data...")

all_players = []

# We are excluding 2020 because it was a shortened 60-game season
years = list(range(2015, 2020)) + list(range(2021, 2026))

for year in years:
    print(f"Getting {year} data...")

    url = f"https://www.baseball-reference.com/leagues/majors/{year}-standard-batting.shtml"

    tables = pd.read_html(url)

    # Table 2 contains individual player batting statistics
    players = tables[1].copy()

    # Add the season
    players["Year"] = year

    # Add this year's players to our master list
    all_players.append(players)

    # Small pause between requests
    time.sleep(2)

# Combine all seasons into one dataset
all_players = pd.concat(all_players, ignore_index=True)

print("\nHistorical player data:")
print(all_players.head())

print(f"\nTotal player-season observations: {len(all_players)}")

# Save the complete dataset
all_players.to_csv("mlb_players_2015_2025.csv", index=False)

print("\nHistorical player data saved!")
