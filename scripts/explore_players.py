import pandas as pd

# Load data
data = pd.read_csv("mlb_players_2015_2025.csv")

# Keep MVP vote recipients
mvp_players = data[
    data["Awards"].fillna("").str.contains("MVP-", na=False)
].copy()

# Extract MVP rank
mvp_players["MVP_Rank"] = (
    mvp_players["Awards"]
    .str.extract(r"MVP-(\d+)")[0]
    .astype(int)
)

# Keep top 10
top_mvp = mvp_players[mvp_players["MVP_Rank"] <= 10].copy()


# Primary position function
def get_primary_position(pos):
    if pd.isna(pos):
        return "Unknown"

    pos = str(pos)

    if "*" in pos:
        primary = pos.split("*")[1][0]
    else:
        primary = pos[0]

    position_map = {
        "1": "P",
        "2": "C",
        "3": "1B",
        "4": "2B",
        "5": "3B",
        "6": "SS",
        "7": "LF",
        "8": "CF",
        "9": "RF",
        "D": "DH"
    }

    return position_map.get(primary, "Other")


top_mvp["Primary_Position"] = top_mvp["Pos"].apply(
    get_primary_position
)


# Sort by MVP rank, then show the most important columns
result = top_mvp[
    [
        "Player",
        "Year",
        "MVP_Rank",
        "WAR",
        "OPS+",
        "PA",
        "Primary_Position"
    ]
].sort_values(["MVP_Rank", "WAR"])

print("Top 10 MVP finishers with WAR and OPS+:")
print(result.to_string(index=False))
