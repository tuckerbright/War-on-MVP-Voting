import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load MVP voting data
data = pd.read_csv("mvp_voting_1980_2025.csv")

# Exclude shortened 2020 season
data = data[data["Year"] != 2020].copy()

# Convert Share from strings like "79%" to numbers like 0.79
data["Share"] = (
    data["Share"]
    .astype(str)
    .str.replace("%", "", regex=False)
    .astype(float)
    / 100
)

# Calculate WAR-vote share correlation for each league in each year
correlations = (
    data.groupby(["Year", "League"])
    .apply(lambda x: x["WAR"].corr(x["Share"]), include_groups=False)
    .reset_index(name="WAR_Vote_Correlation")
)

print(correlations.head(20))

print("\nAverage correlation:")
print(round(correlations["WAR_Vote_Correlation"].mean(), 3))

# Plot correlations over time
plt.figure(figsize=(12, 6))

plt.scatter(
    correlations["Year"],
    correlations["WAR_Vote_Correlation"],
    alpha=0.6
)

# Trend line
x = correlations["Year"]
y = correlations["WAR_Vote_Correlation"]

trend = np.polyfit(x, y, 1)
trend_line = np.poly1d(trend)

plt.plot(x, trend_line(x))

plt.axhline(0, linewidth=1)

plt.xlabel("Year")
plt.ylabel("Correlation between WAR and MVP Vote Share")
plt.title("Relationship Between WAR and MLB MVP Voting, 1980–2025")

plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("war_vote_correlation_over_time.png", dpi=300)
plt.show()

# Does the WAR-voting correlation itself increase over time?
year_correlation = correlations["Year"].corr(
    correlations["WAR_Vote_Correlation"]
)

print("\nCorrelation between Year and WAR-Vote Relationship:")
print(round(year_correlation, 3))