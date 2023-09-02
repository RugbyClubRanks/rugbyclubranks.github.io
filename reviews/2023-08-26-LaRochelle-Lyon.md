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
## Prediction with Player Minutes: Lyon by 0.2


Lyon by 4.2 on a neutral field
## Prediction without Player Minutes: La Rochelle by 1.0


Lyon by 3.0 on a neutral pitch


## Scores over Time


![In Match Scores](plots/recap_scores_2023-08-26-LaRochelle-Lyon.png)
## Win Probability over Time


![In Match Predictions](plots/recap_prob_2023-08-26-LaRochelle-Lyon.png)

There were 5 large changes in win probability in this match

|   Away Minutes | Away Player           |   Away elo |   Away Percentile |   Number |   Home Percentile |   Home elo | Home Player               |   Home Minutes |
|---------------:|:----------------------|-----------:|------------------:|---------:|------------------:|-----------:|:--------------------------|---------------:|
|             49 | Jerome Rey            |      83.4  |       1.02029e+06 |        1 |       1.01739e+06 |      91.17 | Georges-Henri Colombe     |             36 |
|             49 | Yanis Charcosset      |      82.56 |       1.0203e+06  |        2 |       1.02068e+06 |      79.72 | Billy Pollard             |             40 |
|             49 | Demba Bamba           |      95.86 |       1.01679e+06 |        3 |       1.01697e+06 |      81.48 | Archer Holz               |             40 |
|             80 | Killian Geraci        |      86.08 |       1.02028e+06 |        4 |       1.01741e+06 |      82.8  | Thomas Lavault            |             69 |
|             46 | Loann Goujon          |      85.56 |       1.02028e+06 |        5 |       1.02052e+06 |      76.46 | Rémi Picquette            |             80 |
|             46 | Pierre-Samuel Pacheco |      75.26 |  993107           |        6 |       1.01741e+06 |      79.4  | Ultan Dillane             |             80 |
|             80 | Joel Kpoku            |      84.9  |       1.02029e+06 |        7 |       1.01669e+06 |      80    | Oscar Jegou               |             55 |
|             80 | Arno Botha            |      84.37 |       1.02031e+06 |        8 |       1.02052e+06 |      75.31 | Judicael Cancoriet        |             80 |
|             46 | Pierre Pagès          |      85.27 |       1.02026e+06 |        9 |       1.0174e+06  |      94.25 | Tawera Kerr-Barlow        |             49 |
|             50 | Fletcher Smith        |      84.15 |       1.0203e+06  |       10 |       1.01603e+06 |      89.54 | Hugo Reus                 |             49 |
|             80 | Vincent Rattez        |      84.57 |       1.02031e+06 |       11 |       1.01738e+06 |      94.46 | Dillyn Leyds              |             80 |
|             80 | Kyle Godwin           |      86.4  |       1.02028e+06 |       12 |       1.01742e+06 |      81.2  | Jules Favre               |             80 |
|             55 | Josiah Maraku         |      87.78 |       1.01687e+06 |       13 |       1.02053e+06 |      74.45 | Jack Nowell               |             80 |
|             80 | Xavier Mignot         |      84.78 |       1.0203e+06  |       14 |       1.02053e+06 |      74.65 | Teddy Thomas              |             64 |
|             80 | Toby Arnold           |      95.33 |       1.01679e+06 |       15 |       1.01739e+06 |     108    | Brice Dulin               |             80 |
|             34 | Mickael Guillard      |      90.77 |     nan           |       16 |       1.02051e+06 |      79.58 | Thierry Paiva             |             44 |
|             34 | Félix Lambey          |      90.51 |       1.01681e+06 |       17 |       1.01174e+06 |      74.1  | Aleksandre Kuntelia       |             40 |
|             34 | Paul Dumas            |      82.31 |     nan           |       18 |       1.01739e+06 |      85.71 | Quentin Lespiaucq-Brettes |             40 |
|             31 | Hamza Kaabeche        |      87.2  |       1.02026e+06 |       19 |     nan           |      84.93 | Teddy Iribaren            |             31 |
|             31 | Guillaume Marchand    |      92.04 |     nan           |       20 |       1.0205e+06  |      76.7  | Ihaia West                |             31 |
|             31 | Santiago Medrano      |      82.5  |     nan           |       21 |     nan           |      90.16 | Noé Della Schiava         |             25 |
|             30 | Paddy Jackson         |      84.84 |     nan           |       22 |     nan           |      84.2  | Nathan Bollengier         |             16 |
|             25 | Alfred Parisien       |      92.03 |     nan           |       23 |     nan           |      87.63 | Thomas Ployet             |             11 |


# Player Level Predictions - Version 2


Treating teams instead as an entity made up of the currently active players, I have ratings for each player in an altogether different system. These can be combined to form team ratings once teamsheets are announced, weighting starters a bit higher than the reserves. After the match is played, players can be weighted by their minutes on the field, allowing for an accurate measure of the team's composition. With these compiled team ratings, we can make predictions, measure inaccuracy, and update the individual player ratings.
## Prediction with Player Minutes: La Rochelle by 4.9


La Rochelle by 0.1 on a neutral field
## Prediction without Player Minutes: La Rochelle by 5.0


La Rochelle by 0.3 on a neutral pitch



|   Away Minutes | Away Player           |   Away elo |   Away variance |   Number |   Home variance |   Home elo | Home Player               |   Home Minutes |
|---------------:|:----------------------|-----------:|----------------:|---------:|----------------:|-----------:|:--------------------------|---------------:|
|             49 | Jerome Rey            |      46.65 |              50 |        1 |              50 |      46.65 | Georges-Henri Colombe     |             36 |
|             49 | Yanis Charcosset      |      46.65 |              50 |        2 |              50 |      46.65 | Billy Pollard             |             40 |
|             49 | Demba Bamba           |      46.65 |              50 |        3 |              50 |      46.65 | Archer Holz               |             40 |
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

