import pandas as pd

# Load the WAR data
war_data = pd.read_csv("mlb_team_war_2015_2025.csv")

# Load the wins/losses data
wins_data = pd.read_csv("mlb_team_wins_2015_2025.csv")

# Rename the wins/losses columns
wins_data.columns = ["Team", "Year", "Wins", "Losses"]

# Standardize the Angels' team name
wins_data["Team"] = wins_data["Team"].replace(
    "Los Angeles Angels of Anaheim",
    "Los Angeles Angels"
)

war_data["Team"] = war_data["Team"].replace(
    "Los Angeles Angels of Anaheim",
    "Los Angeles Angels"
)

# Combine the two datasets using Team and Year
combined_data = pd.merge(
    war_data,
    wins_data,
    on=["Team", "Year"],
    how="inner"
)

# Print the combined data
print(combined_data)

# Save the combined dataset
combined_data.to_csv("mlb_war_and_wins_2015_2025.csv", index=False)

print("Combined data saved successfully!")

# Find WAR records that did not match the wins data
missing_wins = war_data.merge(
    wins_data,
    on=["Team", "Year"],
    how="left",
    indicator=True
)

missing_wins = missing_wins[missing_wins["_merge"] == "left_only"]

print("\nMissing matches:")
print(missing_wins[["Team", "Year", "Total_WAR"]])