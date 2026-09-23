import pandas as pd
import re

all_data = []

for year in range(2015, 2026):

    print(f"Getting data for {year}...")

    url = f"https://www.baseball-reference.com/leagues/team_compare.cgi?lg=MLB&request=1&stat=WAR&year={year}"

    tables = pd.read_html(url)

    total_war = tables[0]["Total"]

    teams = []
    wars = []

    for value in total_war[:30]:

        match = re.match(r"(.+?)(-?\d+\.\d+)$", value)

        team_name = match.group(1)
        war = float(match.group(2))

        teams.append(team_name)
        wars.append(war)

    year_data = pd.DataFrame({
        "Team": teams,
        "Year": year,
        "Total_WAR": wars
    })

    all_data.append(year_data)


final_data = pd.concat(all_data, ignore_index=True)

print(final_data)

final_data.to_csv("mlb_team_war_2015_2025.csv", index=False)

print("All MLB WAR data saved successfully!")