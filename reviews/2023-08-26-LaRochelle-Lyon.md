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
## Prediction with Player Minutes: La Rochelle by 0.5


Lyon by 3.5 on a neutral field
## Prediction without Player Minutes: La Rochelle by 2.2


Lyon by 1.8 on a neutral pitch


## Scores over Time


![In Match Scores](plots/recap_scores_2023-08-26-LaRochelle-Lyon.png)
## Win Probability over Time


![In Match Predictions](plots/recap_prob_2023-08-26-LaRochelle-Lyon.png)

There were 6 large changes in win probability in this match

|   Away Minutes | Away Player           |   Away elo |   Away Percentile |   Number |   Home Percentile |   Home elo | Home Player               |   Home Minutes |
|---------------:|:----------------------|-----------:|------------------:|---------:|------------------:|-----------:|:--------------------------|---------------:|
|             49 | Jerome Rey            |      82.07 |       1.01978e+06 |        1 |       1.01755e+06 |      91.43 | Georges-Henri Colombe     |             36 |
|             49 | Yanis Charcosset      |      82.57 |       1.01977e+06 |        2 |       1.01616e+06 |      89.51 | Billy Pollard             |             40 |
|             49 | Demba Bamba           |      93.91 |       1.01729e+06 |        3 |  977431           |      80.03 | Archer Holz               |             40 |
|             80 | Killian Geraci        |      87.55 |       1.01974e+06 |        4 |       1.01758e+06 |      82.34 | Thomas Lavault            |             69 |
|             46 | Loann Goujon          |      84.9  |       1.01976e+06 |        5 |       1.0199e+06  |      76.65 | Rémi Picquette            |             80 |
|             46 | Pierre-Samuel Pacheco |      75.2  |  992624           |        6 |       1.01759e+06 |      78.85 | Ultan Dillane             |             80 |
|             80 | Joel Kpoku            |      83.48 |       1.01978e+06 |        7 |       1.01613e+06 |      80    | Oscar Jegou               |             55 |
|             80 | Arno Botha            |      88.02 |       1.01973e+06 |        8 |       1.01992e+06 |      75.01 | Judicael Cancoriet        |             80 |
|             46 | Pierre Pagès          |      82.3  |       1.01978e+06 |        9 |       1.01757e+06 |      93.74 | Tawera Kerr-Barlow        |             49 |
|             50 | Fletcher Smith        |      86.03 |       1.01974e+06 |       10 |       1.01547e+06 |      89.54 | Hugo Reus                 |             49 |
|             80 | Vincent Rattez        |      86.4  |       1.01975e+06 |       11 |       1.01756e+06 |      93.75 | Dillyn Leyds              |             80 |
|             80 | Kyle Godwin           |      84.79 |       1.01978e+06 |       12 |       1.01755e+06 |      84.01 | Jules Favre               |             80 |
|             55 | Josiah Maraku         |      89.7  |       1.01731e+06 |       13 |       1.01992e+06 |      74.79 | Jack Nowell               |             80 |
|             80 | Xavier Mignot         |      85.25 |       1.01977e+06 |       14 |       1.01989e+06 |      76.31 | Teddy Thomas              |             64 |
|             80 | Toby Arnold           |      91.07 |       1.0173e+06  |       15 |       1.01754e+06 |     109.28 | Brice Dulin               |             80 |
|             34 | Mickael Guillard      |      90.57 |     nan           |       16 |       1.0199e+06  |      79.51 | Thierry Paiva             |             44 |
|             34 | Félix Lambey          |      90.18 |       1.0173e+06  |       17 |       1.01121e+06 |      74.1  | Aleksandre Kuntelia       |             40 |
|             34 | Paul Dumas            |      82.37 |     nan           |       18 |       1.01756e+06 |      84.76 | Quentin Lespiaucq-Brettes |             40 |
|             31 | Hamza Kaabeche        |      85.4  |       1.01975e+06 |       19 |     nan           |      85.74 | Teddy Iribaren            |             31 |
|             31 | Guillaume Marchand    |      97.38 |     nan           |       20 |       1.01993e+06 |      74.58 | Ihaia West                |             31 |
|             31 | Santiago Medrano      |      82.56 |     nan           |       21 |     nan           |      90.16 | Noé Della Schiava         |             25 |
|             30 | Paddy Jackson         |      83.51 |     nan           |       22 |     nan           |      84.6  | Nathan Bollengier         |             16 |
|             25 | Alfred Parisien       |      94.77 |     nan           |       23 |     nan           |      86.48 | Thomas Ployet             |             11 |


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

