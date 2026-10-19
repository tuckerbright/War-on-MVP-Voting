import pandas as pd

data = pd.read_csv("mvp_voting_1980_2025.csv")

# Exclude shortened 2020 season
data = data[data["Year"] != 2020].copy()

results = []

for (year, league), group in data.groupby(["Year", "League"]):

    # Find MVP winner
    winner = group[group["Rank"] == 1].iloc[0]

    # Highest WAR among MVP vote-getters
    highest_war = group["WAR"].max()

    # Player(s) with highest WAR
    war_leaders = group[group["WAR"] == highest_war]["Name"].tolist()

    # Difference between highest WAR and winner WAR
    war_gap = highest_war - winner["WAR"]

    results.append({
        "Year": year,
        "League": league,
        "MVP": winner["Name"],
        "MVP_WAR": winner["WAR"],
        "Highest_WAR": highest_war,
        "WAR_Leader": ", ".join(war_leaders),
        "WAR_Gap": war_gap,
        "MVP_Was_WAR_Leader": winner["WAR"] == highest_war
    })

gaps = pd.DataFrame(results)

# Assign eras
def assign_era(year):
    if year <= 2007:
        return "1980-2007"
    elif year <= 2012:
        return "2008-2012"
    else:
        return "2013-2025"

gaps["Era"] = gaps["Year"].apply(assign_era)

print("Average WAR gap by era:")
print(gaps.groupby("Era")["WAR_Gap"].mean().round(2))

print("\nPercent of MVP winners who had highest WAR among vote-getters:")
print(
    (gaps.groupby("Era")["MVP_Was_WAR_Leader"].mean() * 100).round(1)
)

print("\nLargest WAR gaps:")
print(
    gaps[
        ["Year", "League", "MVP", "MVP_WAR",
         "WAR_Leader", "Highest_WAR", "WAR_Gap"]
    ]
    .sort_values("WAR_Gap", ascending=False)
    .head(15)
)
