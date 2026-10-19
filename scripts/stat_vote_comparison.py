import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("mvp_voting_1980_2025.csv")

# Exclude shortened 2020 season
data = data[data["Year"] != 2020].copy()

# Convert vote share to decimal
data["Share"] = (
    data["Share"]
    .astype(str)
    .str.replace("%", "", regex=False)
    .astype(float)
    / 100
)

stats = ["WAR", "HR", "RBI", "BA", "OPS"]

results = []

# Calculate correlation between each statistic and MVP vote share
# separately for every league-season
for (year, league), group in data.groupby(["Year", "League"]):

    row = {
        "Year": year,
        "League": league
    }

    for stat in stats:
        row[stat] = group[stat].corr(group["Share"])

    results.append(row)

correlations = pd.DataFrame(results)

# Show average correlation for each statistic
print("Average correlation with MVP vote share:")
for stat in stats:
    print(f"{stat}: {correlations[stat].mean():.3f}")

print("\nChange over time:")
for stat in stats:
    trend = correlations["Year"].corr(correlations[stat])
    print(f"{stat}: {trend:.3f}")

# Average AL and NL together for each year
yearly = correlations.groupby("Year")[stats].mean()

# Plot trends
plt.figure(figsize=(12, 7))

for stat in stats:
    # Use a rolling average to make long-term trends easier to see
    rolling = yearly[stat].rolling(
        window=5,
        center=True,
        min_periods=3
    ).mean()

    plt.plot(
        yearly.index,
        rolling,
        label=stat,
        linewidth=2
    )

plt.xlabel("Year")
plt.ylabel("Correlation with MVP Vote Share")
plt.title("Statistics Associated with MLB MVP Voting Over Time")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("stat_vote_comparison.png", dpi=300)
plt.show()
# Create voting eras
def assign_era(year):
    if year <= 2007:
        return "1980-2007"
    elif year <= 2012:
        return "2008-2012"
    else:
        return "2013-2025"

correlations["Era"] = correlations["Year"].apply(assign_era)

# Calculate average correlation with MVP vote share by era
era_results = correlations.groupby("Era")[stats].mean()

print("\nAverage correlation with MVP vote share by era:")
print(era_results.round(3))
