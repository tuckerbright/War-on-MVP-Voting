import pandas as pd
import re

url = "https://www.baseball-reference.com/leagues/team_compare.cgi?lg=MLB&request=1&stat=WAR&year=2024"

print("Getting 2024 Baseball-Reference WAR data...")

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

war_data = pd.DataFrame({
    "Team": teams,
    "Year": 2024,
    "Total_WAR": wars
})

print(war_data)
war_data.to_csv("2024_team_war.csv", index=False)

print("CSV file created successfully!")