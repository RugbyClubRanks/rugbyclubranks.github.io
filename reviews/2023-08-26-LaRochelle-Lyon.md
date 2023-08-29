---  
layout: page  
title: Lyon at La Rochelle; 14-35  
date: 2023-08-26 18:00:00 -0500  
categories: match review  
---
# Lyon at La Rochelle; 14-35

# Club Level Predictions


The first set of predictions treats a club as the smallest object, as the club develops its members, organizes a gameplan, and deploys its players as needed for each match. This club model has a prediction of 0.733, which translates to predicting La Rochelle to win by 8.9.

Each club has a rating and a rating deviation (simiar to a Glicko system), and expected performances can be generated. This allows for simulated matches and spreads like the ones below.
## Projected Performances


![Projected Performances](plots/performances_2023-08-26-LaRochelle-Lyon.png)
## Projected Spreads


![Projected Spreads](plots/spreads_2023-08-26-LaRochelle-Lyon.png)
## Projected Results


![Projected Results](plots/resultbar_2023-08-26-LaRochelle-Lyon.png)
# Player Level Predictions - Version 1


Treating teams instead as an entity made up of the currently active players, I have ratings for each player in an altogether different system. These can be combined to form team ratings once teamsheets are announced, weighting starters a bit higher than the reserves. After the match is played, players can be weighted by their minutes on the field, allowing for an accurate measure of the team's composition. With these compiled team ratings, we can make predictions, measure inaccuracy, and update the individual player ratings.
## Prediction with Player Minutes: Lyon by 0.7


Lyon by 4.7 on a neutral field
## Prediction without Player Minutes: La Rochelle by 0.8


Lyon by 3.2 on a neutral pitch


## Scores over Time


![In Match Scores](plots/recap_scores_2023-08-26-LaRochelle-Lyon.png)
## Win Probability over Time


![In Match Predictions](plots/recap_prob_2023-08-26-LaRochelle-Lyon.png)

There were 5 large changes in win probability in this match

|   Away Minutes | Away Player           |   Away elo |   Away Percentile |   Number |   Home Percentile |   Home elo | Home Player               |   Home Minutes |
|---------------:|:----------------------|-----------:|------------------:|---------:|------------------:|-----------:|:--------------------------|---------------:|
|             49 | Jerome Rey            |      84.13 |       1.01971e+06 |        1 |       1.01759e+06 |      91.09 | Georges-Henri Colombe     |             36 |
|             49 | Yanis Charcosset      |      82.71 |       1.01974e+06 |        2 |       1.01999e+06 |      79.57 | Billy Pollard             |             40 |
|             49 | Demba Bamba           |      88.83 |       1.01737e+06 |        3 |  977432           |      79.39 | Archer Holz               |             40 |
|             80 | Killian Geraci        |      87.77 |       1.0197e+06  |        4 |       1.01761e+06 |      82.78 | Thomas Lavault            |             69 |
|             46 | Loann Goujon          |      87.03 |       1.0197e+06  |        5 |       1.01989e+06 |      75.92 | Rémi Picquette            |             80 |
|             46 | Pierre-Samuel Pacheco |      75.18 |  992629           |        6 |       1.01762e+06 |      78.64 | Ultan Dillane             |             80 |
|             80 | Joel Kpoku            |      86.44 |       1.0197e+06  |        7 |       1.01614e+06 |      79.99 | Oscar Jegou               |             55 |
|             80 | Arno Botha            |      86.97 |       1.01971e+06 |        8 |       1.01986e+06 |      76.02 | Judicael Cancoriet        |             80 |
|             46 | Pierre Pagès          |      83.66 |       1.01972e+06 |        9 |       1.0176e+06  |      94.23 | Tawera Kerr-Barlow        |             49 |
|             50 | Fletcher Smith        |      84.6  |       1.01972e+06 |       10 |       1.01548e+06 |      89.54 | Hugo Reus                 |             49 |
|             80 | Vincent Rattez        |      84.59 |       1.01975e+06 |       11 |       1.01759e+06 |      94.05 | Dillyn Leyds              |             80 |
|             80 | Kyle Godwin           |      88.78 |       1.01969e+06 |       12 |       1.01758e+06 |      83.99 | Jules Favre               |             80 |
|             55 | Josiah Maraku         |      88.72 |       1.01738e+06 |       13 |       1.01986e+06 |      76.31 | Jack Nowell               |             80 |
|             80 | Xavier Mignot         |      85.01 |       1.01974e+06 |       14 |       1.0199e+06  |      74.79 | Teddy Thomas              |             64 |
|             80 | Toby Arnold           |      93.85 |       1.01732e+06 |       15 |       1.01759e+06 |     108.65 | Brice Dulin               |             80 |
|             34 | Mickael Guillard      |      91.06 |     nan           |       16 |       1.0199e+06  |      78.08 | Thierry Paiva             |             44 |
|             34 | Félix Lambey          |      94.21 |       1.01732e+06 |       17 |       1.01122e+06 |      74.09 | Aleksandre Kuntelia       |             40 |
|             34 | Paul Dumas            |      82.69 |     nan           |       18 |       1.01762e+06 |      83.76 | Quentin Lespiaucq-Brettes |             40 |
|             31 | Hamza Kaabeche        |      85.23 |       1.01971e+06 |       19 |     nan           |      83.52 | Teddy Iribaren            |             31 |
|             31 | Guillaume Marchand    |      93.09 |     nan           |       20 |       1.01986e+06 |      76.63 | Ihaia West                |             31 |
|             31 | Santiago Medrano      |      82.51 |     nan           |       21 |     nan           |      90.16 | Noé Della Schiava         |             25 |
|             30 | Paddy Jackson         |      82.05 |     nan           |       22 |     nan           |      84.61 | Nathan Bollengier         |             16 |
|             25 | Alfred Parisien       |      94.08 |     nan           |       23 |     nan           |      86.5  | Thomas Ployet             |             11 |


# Player Level Predictions - Version 2


Treating teams instead as an entity made up of the currently active players, I have ratings for each player in an altogether different system. These can be combined to form team ratings once teamsheets are announced, weighting starters a bit higher than the reserves. After the match is played, players can be weighted by their minutes on the field, allowing for an accurate measure of the team's composition. With these compiled team ratings, we can make predictions, measure inaccuracy, and update the individual player ratings.
## Prediction with Player Minutes: La Rochelle by 4.7


Lyon by 0.0 on a neutral field
## Prediction without Player Minutes: La Rochelle by 4.7


Lyon by 0.0 on a neutral pitch



|   Away Minutes | Away Player           |   Away elo |   Away variance |   Number |   Home variance |   Home elo | Home Player               |   Home Minutes |
|---------------:|:----------------------|-----------:|----------------:|---------:|----------------:|-----------:|:--------------------------|---------------:|
|             49 | Jerome Rey            |      46.65 |              50 |        1 |              50 |      46.65 | Georges-Henri Colombe     |             36 |
|             49 | Yanis Charcosset      |      46.65 |              50 |        2 |              50 |      46.65 | Billy Pollard             |             40 |
|             49 | Demba Bamba           |      46.65 |              50 |        3 |              50 |      39.05 | Archer Holz               |             40 |
|             80 | Killian Geraci        |      46.65 |              50 |        4 |              50 |      46.65 | Thomas Lavault            |             69 |
|             46 | Loann Goujon          |      46.65 |              50 |        5 |              50 |      46.65 | Rémi Picquette            |             80 |
|             46 | Pierre-Samuel Pacheco |      42.2  |              50 |        6 |              50 |      46.65 | Ultan Dillane             |             80 |
|             80 | Joel Kpoku            |      46.65 |              50 |        7 |              50 |      47    | Oscar Jegou               |             55 |
|             80 | Arno Botha            |      46.65 |              50 |        8 |              50 |      46.65 | Judicael Cancoriet        |             80 |
|             46 | Pierre Pagès          |      46.65 |              50 |        9 |              50 |      46.65 | Tawera Kerr-Barlow        |             49 |
|             50 | Fletcher Smith        |      46.65 |              50 |       10 |              50 |      49.86 | Hugo Reus                 |             49 |
|             80 | Vincent Rattez        |      46.65 |              50 |       11 |              50 |      46.65 | Dillyn Leyds              |             80 |
|             80 | Kyle Godwin           |      46.65 |              50 |       12 |              50 |      46.65 | Jules Favre               |             80 |
|             55 | Josiah Maraku         |      46.65 |              50 |       13 |              50 |      46.65 | Jack Nowell               |             80 |
|             80 | Xavier Mignot         |      46.65 |              50 |       14 |              50 |      46.65 | Teddy Thomas              |             64 |
|             80 | Toby Arnold           |      46.65 |              50 |       15 |              50 |      46.65 | Brice Dulin               |             80 |
|             34 | Mickael Guillard      |      46.65 |              50 |       16 |              50 |      46.65 | Thierry Paiva             |             44 |
|             34 | Félix Lambey          |      46.65 |              50 |       17 |              50 |      43.52 | Aleksandre Kuntelia       |             40 |
|             34 | Paul Dumas            |      46.65 |              50 |       18 |              50 |      46.65 | Quentin Lespiaucq-Brettes |             40 |
|             31 | Hamza Kaabeche        |      46.65 |              50 |       19 |              50 |      46.65 | Teddy Iribaren            |             31 |
|             31 | Guillaume Marchand    |      46.65 |              50 |       20 |              50 |      46.65 | Ihaia West                |             31 |
|             31 | Santiago Medrano      |      46.65 |              50 |       21 |              50 |      46.67 | Noé Della Schiava         |             25 |
|             30 | Paddy Jackson         |      46.65 |              50 |       22 |              50 |      46.65 | Nathan Bollengier         |             16 |
|             25 | Alfred Parisien       |      46.65 |              50 |       23 |              50 |      46.65 | Thomas Ployet             |             11 |

