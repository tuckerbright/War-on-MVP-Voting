import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load our combined dataset
data = pd.read_csv("mlb_war_and_wins_2015_2025.csv")

# Exclude the shortened 2020 season
data = data[data["Year"] != 2020].copy()

print(f"Number of observations: {len(data)}")

# Calculate winning percentage
data["Winning_Percentage"] = data["Wins"] / (data["Wins"] + data["Losses"])

# Show the first 10 rows
print("\nFirst 10 rows:")
print(data.head(10))

# Calculate the correlation between Total WAR and Wins
correlation = data["Total_WAR"].corr(data["Wins"])

print("\nCorrelation between Total WAR and Wins:")
print(correlation)

# Calculate the regression line
slope, intercept = np.polyfit(data["Total_WAR"], data["Wins"], 1)

# Create predicted wins for each WAR value
predicted_wins = slope * data["Total_WAR"] + intercept

# Create the scatterplot
plt.scatter(data["Total_WAR"], data["Wins"])

# Add the regression line
plt.plot(data["Total_WAR"], predicted_wins)

# Add labels and title
plt.xlabel("Total WAR")
plt.ylabel("Wins")
plt.title("MLB Team WAR vs. Wins (2015–2019, 2021–2025)")

# Save the graph
plt.savefig(
    "graphs/war_vs_wins_regression.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the graph
plt.show()

# Print the regression equation
print("\nRegression results:")
print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"Equation: Wins = {intercept:.4f} + {slope:.4f} × WAR")
# Calculate R-squared
r_squared = correlation ** 2

print("\nR-squared:")
print(f"{r_squared:.4f}")