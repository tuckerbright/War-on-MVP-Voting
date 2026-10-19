import pandas as pd
import matplotlib.pyplot as plt

# Load our MVP voting dataset
data = pd.read_csv("mvp_voting_1980_2025.csv")

# Keep only MVP winners
winners = data[data["Rank"] == 1].copy()

print("Number of MVP winners:", len(winners))

print("\nFirst 10 MVP winners:")
print(winners[["Year", "League", "Name", "WAR"]].head(10))

print("\nAverage WAR of MVP winners:")
print(winners["WAR"].mean())

print("\nLowest-WAR MVP winners:")
print(
    winners[["Year", "League", "Name", "WAR"]]
    .sort_values("WAR")
    .head(15)
)# Exclude the shortened 2020 season
winners_no_2020 = winners[winners["Year"] != 2020].copy()

# Plot MVP winner WAR over time
plt.figure(figsize=(12, 6))

plt.scatter(
    winners_no_2020["Year"],
    winners_no_2020["WAR"],
    alpha=0.7
)

# Add a linear trend line
import numpy as np

x = winners_no_2020["Year"]
y = winners_no_2020["WAR"]

trend = np.polyfit(x, y, 1)
trend_line = np.poly1d(trend)

plt.plot(x, trend_line(x))

plt.xlabel("Year")
plt.ylabel("WAR")
plt.title("WAR of MLB MVP Winners, 1980–2025")

plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("mvp_winner_war_over_time.png", dpi=300)
plt.show()

# Correlation between year and winner WAR
correlation = x.corr(y)

print("\nCorrelation between Year and MVP Winner WAR:")
print(round(correlation, 3))
