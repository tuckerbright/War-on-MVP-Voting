import pandas as pd
import matplotlib.pyplot as plt

# Load our player dataset
data = pd.read_csv("mlb_players_2015_2025.csv")

# Exclude the shortened 2020 season
data = data[data["Year"] != 2020].copy()

print(f"Number of observations: {len(data)}")

# Calculate the correlation between OPS+ and MVP Rank
correlation = data["OPS+"].corr(data["MVP_Rank"])

print("\nCorrelation between OPS+ and MVP voting rank:")
print(correlation)

# Create the scatterplot
plt.scatter(data["OPS+"], data["MVP_Rank"])

# Invert the y-axis so better MVP finishes appear higher
plt.gca().invert_yaxis()

# Add labels and title
plt.xlabel("OPS+")
plt.ylabel("MVP Rank")
plt.title("OPS+ vs. MVP Voting Rank (2015–2019, 2021–2025)")

# Save the graph
plt.savefig(
    "graphs/ops_plus_vs_mvp_rank.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the graph
plt.show()
