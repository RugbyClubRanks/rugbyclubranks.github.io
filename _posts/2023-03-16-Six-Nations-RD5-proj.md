---
title:  "Six Nations Round 5 Projections"
date:   2023-03-16 06:00:00 -0500
categories: projection
---

# Model Review

| Match                            |   Result |   Lineup Prediction |   Minutes Prediction |   Club Prediction |
|:---------------------------------|---------:|--------------------:|---------------------:|------------------:|
| Wales V Ireland on 2023/02/04    |      -24 |               -19.3 |                -21.1 |             -10.1 |
| England V Scotland on 2023/02/04 |       -6 |                -9.5 |                 -6.7 |               6.3 |
| Italy V France on 2023/02/05     |       -5 |               -15.7 |                -14.8 |             -10.7 |
| Ireland V France on 2023/02/11   |       13 |                27.3 |                 31.6 |               7.5 |
| Scotland V Wales on 2023/02/11   |       28 |                25.1 |                 27.4 |               9.5 |
| England V Italy on 2023/02/12    |       17 |                17.8 |                 18.9 |              14.9 |
| Italy V Ireland on 2023/02/25    |      -14 |               -12.3 |                -12.5 |             -13.7 |
| Wales V England on 2023/02/25    |      -10 |                -8.7 |                 -9.1 |              -2.4 |
| France V Scotland on 2023/02/26  |       11 |                 2.9 |                  4.6 |              11.1 |
| Italy V Wales on 2023/03/11      |      -12 |                11.2 |                 13.4 |               4   |
| England V France on 2023/03/11   |      -43 |                -7.3 |                 -5.8 |               0.4 |
| Scotland V Ireland on 2023/03/12 |      -15 |                -8.2 |                 -9.2 |              -4.5 |
| ------ | ------ | ------ | ------ | ------ |
| Average Error |       - | 9.5 | 9.3 | 11.3 |
| Correct Winner |       - | 91.7% | 91.7% | 75.0% |

This last week was not a good one for the model - Italy v Wales was a complete miss, and France's dismantling of England was a much bigger win than any projection had. In total, we have had 3 incorrect winners from the club model, and just one (Wales beating Italy) from the player level model. The average error is about 11 for the club model and just below 10 for the player model, with a lot of that coming from the 43 point France win. Without that game (which is unfair to completely drop but may be useful to focus on the less extreme matches sometimes) the club model has an average error of 8.4 and the player model has an average error of 6.9.

All numbers are using the most recent models, and always predict a match using only data available before that match kicks off. Except for the Player Minutes model, of course, as we need the match to be played to see how long any player is on the field. For a bit more depth, check out the match predictions in the [Current Projections page](../../../../Current_Projections). Or check out the [Six Nations Status page](/comp_files/Six_Nations_Championship_2022) for some plots.




# Week Five Projections

After the matches last week, the models don't think there'll be anything close this weekend. Which is unfortunate for a final round. The biggest bit of drama is whether or not Ireland could pull off the grand slam with all of their injuries - something that the club model does not take into account. But then the player model gives Ireland an even better chance to win. Looking for silver linings in the other two matches, it does give each team a chance to line up against relatively strong competition six months before the world cup. We could see some new ideas, and are seeing some new names and faces on the teamsheets across the competition.

## Scotland v Italy

Club Model: Scotland by 16.3

Lineup Model: Scotland by 7.5

Simulation Prediction: Scotland by 14.84

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Scotland Victory | 99% |
| Italy Victory | 0.6% |
| Tie | 0.4% |
| Scotland Losing Bonus Point | 0.6% |
| Italy Losing Bonus Point | 11.5% |
| Scotland 4 Try Bonus Point (BETA) | 71.5% |
| Italy 4 Try Bonus Point (BETA) | 6.7% |

## France v Wales

Club Model: France by 18.2

Lineup Model: France by 29

Simulation Prediction: France by 16.98

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| France Victory | 99.1% |
| Wales Victory | 0.4% |
| Tie | 0.5% |
| France Losing Bonus Point | 0.4% |
| Wales Losing Bonus Point | 7.1% |
| France 4 Try Bonus Point (BETA) | 65.1% |
| Wales 4 Try Bonus Point (BETA) | 1.8% |

## Ireland v England

Club Model: Ireland by 17.4

Lineup Model: Ireland by 25.9

Simulation Prediction:  Ireland by 16.4

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Ireland Victory | 99.4% |
| England Victory | 0.6% |
| Tie | 0% |
| Ireland Losing Bonus Point | 0.6% |
| England Losing Bonus Point | 7% |
| Ireland 4 Try Bonus Point (BETA) | 65.4% |
| England 4 Try Bonus Point (BETA) | 6.9% |


# Simulation for the Final Week

| Team | Average Wins | Average Point Differential | Average Competition Points (_NOW WITH_ Future 4 Try Bonuses) |
| ---- | ------------ | -------------------------- | ------------------------------------------------ |
| Ireland     | 4 + 0.99 = 4.99 | 66  + 16.4 = 82.4 | 19 + 4.64 = 23.64 |
| France      | 3 + 0.99 = 3.99 | 46  + 16.98 = 62.98 | 15 + 4.63 = 19.63 |
| Scotland    | 2 + 0.99 = 2.99 | 8   + 14.84 = 22.84 | 10 + 4.69 = 14.69 |
| England     | 2 + 0.01 = 2.01 | -22 + -16.4 = -38.4 | 10 + 0.16 = 10.16 |
| Wales       | 1 + 0.01 = 1.01 | -50 + -16.98 = -66.98 | 5  + 0.12 = 5.12 |
| Italy       | 0 + 0.01 = 0.01 | -48 + -16.4 = -64.4 | 1  + 0.21 = 1.21 |


At the beginning of this tournament, I had projected this table after week 4:
| Team | Average Wins | Average Point Differential | Average Competition Points (Without 4 Try Bonus) |
| ---- | ------------ | -------------------------- | ------------------------------------------------ |
| Ireland     | 3.86 | 50.96  | 15.56 |
| England     | 3.28 | 36.75  | 13.68 |
| France      | 2.47 | 21.34  | 10.72 |
| Wales       | 1.59 | -6.35  | 7.64  |
| Scotland    | 0.74 | -31.92 |  3.84 |
| Italy       | 0.06 | -70.79 |  0.62 |

I was a bit off on England and Wales and definitely off on Scotland. Perhaps I need to add some harsher consideration of new coaching teams, which would have penalized England and Wales a bit leading into week 1. 

However, I don't think the Scotland error is one that the club model could have caught in this current setup. Perhaps, after after the teamsheets were announced and the player model picked Scotland by 7 (13 points different than the club model) performing a deeper analysis of the simulations where Scotland beat England could have been useful. Maybe this will be in my competition retrospective in a week or two.