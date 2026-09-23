import pandas as pd

url = "https://raw.githubusercontent.com/cbwinslow/lahman-database-csv/main/data/Teams.csv"

teams_data = pd.read_csv(url)

recent_teams = teams_data[
    (teams_data["yearID"] >= 2015) &
    (teams_data["yearID"] <= 2025)
]

wins_data = recent_teams[["name", "yearID", "W", "L"]].copy()

wins_data.columns = ["Team", "Year", "Wins", "Losses"]

print(wins_data)
wins_data.to_csv("mlb_team_wins_2015_2025.csv", index=False)

print("Wins data saved successfully!")