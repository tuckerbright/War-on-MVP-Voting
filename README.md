# Has WAR Changed MLB MVP Voting?

### Analyzing the Relationship Between Wins Above Replacement and MLB MVP Voting (1980–2025)

**Independent Sports Analytics Project | Python | Pandas | Statistical Analysis**

## Project Overview

Over the past several decades, Major League Baseball has experienced a shift toward advanced analytics. Wins Above Replacement (WAR) has become a widely used metric for evaluating a player's overall contribution to their team.

This project investigates whether MLB Most Valuable Player (MVP) voting has become more closely aligned with WAR over time.

Using historical MVP voting data from 1980–2025, I analyzed relationships between player statistics and MVP vote share to evaluate how voting patterns have evolved.

## Research Question

**Has MLB MVP voting become more closely aligned with WAR over time?**

My hypothesis was that as WAR became more prominent in baseball analysis, MVP voting would become increasingly consistent with player WAR.

## Data and Methodology

I collected and analyzed historical MVP voting data from both the American League and National League between 1980 and 2025.

The analysis focused on five statistics:

- **WAR:** Wins Above Replacement
- **HR:** Home Runs
- **RBI:** Runs Batted In
- **BA:** Batting Average
- **OPS:** On-Base Plus Slugging

Using Python, I:

1. Organized historical MVP voting results into a player-level dataset.
2. Calculated correlations between each statistic and MVP vote share within individual league-season races.
3. Compared average correlations across three periods: 1980–2007, 2008–2012, and 2013–2025.
4. Examined how frequently MVP winners had the highest WAR among players receiving MVP votes.
5. Measured the WAR difference between MVP winners and the highest-WAR vote-getters.

The shortened 2020 MLB season was excluded from season-comparison analyses.

## Key Findings

### 1. WAR Has Become More Closely Associated With MVP Voting

The average correlation between WAR and MVP vote share increased substantially in the modern era.

| Statistic | 1980–2007 | 2008–2012 | 2013–2025 |
|---|---:|---:|---:|
| WAR | 0.441 | 0.452 | 0.681 |
| HR | 0.431 | 0.399 | 0.433 |
| RBI | 0.373 | 0.371 | 0.347 |
| BA | 0.263 | 0.251 | 0.294 |
| OPS | 0.395 | 0.312 | 0.479 |

**Key takeaway:** WAR experienced the largest increase in correlation with MVP vote share, while traditional statistics such as home runs, RBI, and batting average showed relatively little long-term change.

### 2. MVP Winners Are Increasingly Likely to Lead in WAR

The percentage of MVP winners who also had the highest WAR among players receiving MVP votes increased across the periods studied.

- **1980–2007:** 28.6%
- **2013–2025:** 58.3%

Additionally, the average gap between an MVP winner's WAR and the highest WAR among vote-getters decreased considerably.

| Period | Average WAR Gap |
|---|---:|
| 1980–2007 | 1.91 |
| 2008–2012 | 0.86 |
| 2013–2025 | 0.46 |

These findings suggest that modern MVP selections are more closely aligned with WAR than selections in earlier decades.

### 3. Historical MVP Races Illustrate the Shift

Several historical MVP races featured substantial differences between the winning player's WAR and that of another player receiving MVP votes.

| Season | MVP Winner | Winner WAR | Highest-WAR Vote-Getter | WAR | Gap |
|---|---|---:|---|---:|---:|
| 1996 AL | Juan González | 3.8 | Ken Griffey Jr. | 9.7 | 5.9 |
| 1987 NL | Andre Dawson | 4.0 | Tony Gwynn | 8.6 | 4.6 |
| 1998 AL | Juan González | 4.9 | Alex Rodriguez | 8.5 | 3.6 |
| 2012 AL | Miguel Cabrera | 7.1 | Mike Trout | 10.5 | 3.4 |

All 15 of the largest WAR gaps identified in this analysis occurred by 2012.

The 2012 American League MVP race is particularly noteworthy because Miguel Cabrera won the Triple Crown, demonstrating how historical achievements and traditional statistics may influence voting decisions.

## Conclusions

The results suggest that MLB MVP voting has become substantially more aligned with WAR, particularly since the early 2010s.

While traditional measures such as home runs, RBI, and batting average remain relevant, WAR appears to have become more closely associated with MVP voting outcomes.

However, **correlation does not establish causation**. This analysis demonstrates changing relationships between WAR and MVP voting, but it does not prove that increased awareness or use of WAR directly caused voters to change their decisions.

## Limitations and Future Research

Several opportunities exist to strengthen and expand this analysis:

- Repeat key analyses using only position players.
- Test whether differences between historical periods are statistically significant.
- Compare MVP winners against complete league WAR leaderboards rather than only players receiving MVP votes.
- Investigate the historical adoption of WAR in baseball media and award discussions.

## Tools and Technologies

- **Python:** Data collection and statistical analysis
- **Pandas:** Data cleaning, manipulation, and organization
- **Matplotlib:** Data visualization
- **Visual Studio Code:** Development environment

## Project Files

This repository contains Python scripts, historical MVP voting datasets, statistical comparisons, and visualizations supporting the analysis.

A full research presentation is also available with additional graphs, comparisons, and discussion of the findings.

## About the Author

**Tucker Bright**

Applied Statistics Student | Purdue University

Interested in sports analytics, statistical modeling, and using data to better understand decision-making and player performance.
