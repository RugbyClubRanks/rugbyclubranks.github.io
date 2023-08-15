---  
layout: page  
title: Wales at England; 17.0-19.0  
date: 2023-08-11 18:00:00 -0500  
categories: match review  
---
# Wales at England; 17.0-19.0

# Club Level Predictions


The first set of predictions treats a club as the smallest object, as the club develops its members, organizes a gameplan, and deploys its players as needed for each match. This club model has a prediction of 0.743, which translates to predicting England to win by 9.7.

Each club has a rating and a rating deviation (simiar to a Glicko system), and expected performances can be generated. This allows for simulated matches and spreads like the ones below.
## Projected Performances


![Projected Performances](plots/performances_2023-08-11-England-Wales.png)
## Projected Spreads


![Projected Spreads](plots/spreads_2023-08-11-England-Wales.png)
## Projected Results


![Projected Results](plots/resultbar_2023-08-11-England-Wales.png)
# Player Level Predictions - Version 1


Treating teams instead as an entity made up of the currently active players, I have ratings for each player in an altogether different system. These can be combined to form team ratings once teamsheets are announced, weighting starters a bit higher than the reserves. After the match is played, players can be weighted by their minutes on the field, allowing for an accurate measure of the team's composition. With these compiled team ratings, we can make predictions, measure inaccuracy, and update the individual player ratings.
## Prediction with Player Minutes: England by 2.7


Wales by 1.3 on a neutral field
## Prediction without Player Minutes: England by 1.3


Wales by 2.7 on a neutral pitch


## Scores over Time


![In Match Scores](plots/recap_scores_2023-08-11-England-Wales.png)
## Win Probability over Time


![In Match Predictions](plots/recap_prob_2023-08-11-England-Wales.png)

There were 13 large changes in win probability in this match

|   Away Minutes | Away Player     |   Away elo |   Away Percentile |   Number |   Home Percentile |   Home elo | Home Player         |   Home Minutes |
|---------------:|:----------------|-----------:|------------------:|---------:|------------------:|-----------:|:--------------------|---------------:|
|             50 | Gareth Thomas   |      95.39 |                85 |        1 |                70 |      91.36 | Joe Marler          |             54 |
|             27 | Dewi Lake       |      95.67 |                81 |        2 |                98 |     134.43 | Jamie George        |             80 |
|             50 | Tomas Francis   |      95.97 |                86 |        3 |                17 |      65.04 | Will Stuart         |             57 |
|             66 | Rhys Davies     |      94.64 |                78 |        4 |                76 |      98.42 | Maro Itoje          |             80 |
|             80 | Adam Beard      |     100.24 |                86 |        5 |                56 |      86.96 | George Martin       |             80 |
|             80 | Dan Lydiate     |      98.91 |                87 |        6 |                70 |      92.08 | Courtney Lawes      |             80 |
|             80 | Tommy Reffell   |      96.64 |                84 |        7 |                86 |     104.5  | Ben Earl            |             80 |
|             48 | Taine Plumtree  |      85.19 |                61 |        8 |                66 |      91.83 | Billy Vunipola      |             62 |
|             72 | Tomos Williams  |     105.3  |                90 |        9 |                83 |     102.64 | Jack van Poortvliet |             32 |
|             50 | Owen Williams   |      95.13 |                75 |       10 |                98 |     135.4  | Owen Farrell        |             80 |
|             80 | Tom Rogers      |      94.88 |                79 |       11 |                82 |     102.96 | Elliot Daly         |             80 |
|             60 | Nick Tompkins   |     144.02 |                99 |       12 |                64 |      91.14 | Ollie Lawrence      |             72 |
|             80 | Joe Roberts     |      99.53 |                83 |       13 |                60 |      89.11 | Joe Marchant        |             80 |
|             80 | Josh Adams      |      94.2  |                78 |       14 |                65 |      90.93 | Henry Arundell      |             57 |
|             80 | Liam Williams   |      94.42 |                76 |       15 |                76 |     100.09 | Freddie Steward     |             80 |
|             53 | Sam Parry       |      97.01 |               nan |       16 |                68 |      87.25 | Theo Dan            |              0 |
|             30 | Kemsley Mathias |      97.42 |               nan |       17 |                58 |      84.07 | Ellis Genge         |             26 |
|             30 | Dillon Lewis    |      97.86 |               nan |       18 |               nan |      92.64 | Dan Cole            |             23 |
|             30 | Christ Tshiunza |      83.13 |                59 |       19 |                62 |      84.67 | Jonny Hill          |              0 |
|             16 | Taine Basham    |      98.36 |               nan |       20 |               nan |      91.58 | Jack Willis         |             18 |
|              8 | Gareth Davies   |      79.27 |                48 |       21 |               nan |      92.35 | Ben Youngs          |             48 |
|             30 | Dan Biggar      |     136.21 |                99 |       22 |                93 |     112.48 | George Ford         |             23 |
|             20 | Keiran Williams |      96.3  |               nan |       23 |                39 |      74.76 | Max Malins          |              8 |


# Player Level Predictions - Version 2


Treating teams instead as an entity made up of the currently active players, I have ratings for each player in an altogether different system. These can be combined to form team ratings once teamsheets are announced, weighting starters a bit higher than the reserves. After the match is played, players can be weighted by their minutes on the field, allowing for an accurate measure of the team's composition. With these compiled team ratings, we can make predictions, measure inaccuracy, and update the individual player ratings.
## Prediction with Player Minutes: England by 16.7


England by 13.0 on a neutral field
## Prediction without Player Minutes: England by 14.9


England by 11.2 on a neutral pitch



|   Away Minutes | Away Player     |   Away elo |   Away variance |   Number |   Home variance |   Home elo | Home Player         |   Home Minutes |
|---------------:|:----------------|-----------:|----------------:|---------:|----------------:|-----------:|:--------------------|---------------:|
|             50 | Gareth Thomas   |      46.65 |              50 |        1 |           50    |      46.65 | Joe Marler          |             54 |
|             27 | Dewi Lake       |      46.65 |              50 |        2 |           50    |     115.23 | Jamie George        |             80 |
|             50 | Tomas Francis   |      46.65 |              50 |        3 |           50    |      38.48 | Will Stuart         |             57 |
|             66 | Rhys Davies     |      46.65 |              50 |        4 |           50    |     114.52 | Maro Itoje          |             80 |
|             80 | Adam Beard      |      46.65 |              50 |        5 |           50    |      83.37 | George Martin       |             80 |
|             80 | Dan Lydiate     |      46.65 |              50 |        6 |           50    |      46.65 | Courtney Lawes      |             80 |
|             80 | Tommy Reffell   |      46.65 |              50 |        7 |           50    |      95.95 | Ben Earl            |             80 |
|             48 | Taine Plumtree  |      61.29 |              50 |        8 |           50    |      46.65 | Billy Vunipola      |             62 |
|             72 | Tomos Williams  |      74.76 |              50 |        9 |           50    |      58.54 | Jack van Poortvliet |             32 |
|             50 | Owen Williams   |      46.65 |              50 |       10 |           50    |     141.24 | Owen Farrell        |             80 |
|             80 | Tom Rogers      |      46.65 |              50 |       11 |           50    |      63.83 | Elliot Daly         |             80 |
|             60 | Nick Tompkins   |     101.98 |              50 |       12 |           50    |      46.65 | Ollie Lawrence      |             72 |
|             80 | Joe Roberts     |      46.65 |              50 |       13 |           50    |      93.18 | Joe Marchant        |             80 |
|             80 | Josh Adams      |      46.65 |              50 |       14 |           50    |      46.65 | Henry Arundell      |             57 |
|             80 | Liam Williams   |      46.65 |              50 |       15 |           49.59 |      63.33 | Freddie Steward     |             80 |
|             53 | Sam Parry       |      46.65 |              50 |       16 |           50    |      50.11 | Theo Dan            |              0 |
|             30 | Kemsley Mathias |      46.65 |              50 |       17 |           50    |      51.82 | Ellis Genge         |             26 |
|             30 | Dillon Lewis    |      46.65 |              50 |       18 |           50    |      46.65 | Dan Cole            |             23 |
|             30 | Christ Tshiunza |      38.82 |              50 |       19 |           50    |      45.75 | Jonny Hill          |              0 |
|             16 | Taine Basham    |      46.65 |              50 |       20 |           50    |      46.65 | Jack Willis         |             18 |
|              8 | Gareth Davies   |      34.79 |              50 |       21 |           50    |      46.65 | Ben Youngs          |             48 |
|             30 | Dan Biggar      |     122.8  |              50 |       22 |           50    |     101.37 | George Ford         |             23 |
|             20 | Keiran Williams |      46.65 |              50 |       23 |           50    |      64.89 | Max Malins          |              8 |

