---
title:  "Six Nations Round 4 Projections"
date:   2023-03-10 06:00:00 -0500
categories: projection
---

# Model Review

| Match                            |   Result |   Lineup Prediction |   Minutes Prediction |   Club Prediction |
|:---------------------------------|---------:|--------------------:|---------------------:|------------------:|
| Wales V Ireland on 2023/02/04    |      -24 |               -19.8 |                -21.5 |             -10.1 |
| England V Scotland on 2023/02/04 |       -6 |                -9.1 |                 -6.4 |               6.3 |
| Italy V France on 2023/02/05     |       -5 |               -15.7 |                -14.8 |             -10.7 |
| Ireland V France on 2023/02/11   |       13 |                28.2 |                 32.3 |               7.5 |
| Scotland V Wales on 2023/02/11   |       28 |                25   |                 27.1 |               9.5 |
| England V Italy on 2023/02/12    |       17 |                17.8 |                 18.9 |              14.9 |
| Italy V Ireland on 2023/02/25    |      -14 |               -12.5 |                -12.6 |             -13.7 |
| Wales V England on 2023/02/25    |      -10 |                -8.3 |                 -8.6 |              -2.4 |
| France V Scotland on 2023/02/26  |       11 |                 3.2 |                  5.1 |              11.1 |
| ------ | ------ | ------ | ------ | ------ |
| Average Error |       - | 5.3 | 4.8 | 7.3 |
| Correct Winner |       - | 100.0% | 100.0% | 88.9% |

So far so good. All the models were 3 of 3 in week 3, with the player level predictions being a bit better than the club predictions again. Except for France v Scotland, which did have two red cards and was 25-21 France until the 80th minute, so the player model was still pretty good.

All numbers are using the most recent models, and always predict a match using only data available before that match kicks off. Except for the Player Minutes model, of course, as we need the match to be played to see how long any player is on the field. For a bit more depth, check out the match predictions in the [Current Projections page](../../../../Current_Projections). Or check out the [Six Nations Status page](/comp_files/Six_Nations_Championship_2022) for some plots.




# Week Four Projections


## Italy v Wales

Club Model: Italy by 4

Lineup Model: Italy by 10.7

The player predictions feel too bullish for Italy and too bearish for Wales at the same time. The Welsh team is good, but is struggling to mesh and their ratings have reflected that. But once things gel, they may be right back to competing (hopefully in time for the world cup). Italy has been solid, but has also suffered some injuries and is playing some players out of position. So far they've been excellent at home, so I fully expect them to win this match. But I do think it'll be closer to by 6 points or so.

Simulation Prediction: Italy by 3.11

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Italy Victory | 66% |
| Wales Victory | 29.5% |
| Tie | 4.5% |
| Italy Losing Bonus Point | 22.5% |
| Wales Losing Bonus Point | 39.1% |
| Italy 4 Try Bonus Point (BETA) | 5.8% |
| Wales 4 Try Bonus Point (BETA) | 0.7% |


## England v France

Club Model: England by 0.3

Lineup Model: France by 6.4

This one looks close, and its only the second time that the player and club models have disagreed: last time the player model had Scotland by 9 and was much more accurate than the club prediction of England by 6. This may be a case of Borthwick's selections being different than Eddie Jones', but no matter the case I'd trust the player model more for this one.

Simulation Prediction: France by 0.89

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| France Victory | 52.5% |
| England Victory | 41.6% |
| Tie | 5.9% |
| France Losing Bonus Point | 29.9% |
| England Losing Bonus Point | 34.7% |
| France 4 Try Bonus Point (BETA) | 3.3% |
| England 4 Try Bonus Point (BETA) | 5.5% |


## Scotland v Ireland

Club Model: Ireland by 4.3

Lineup Model: Recent lineups suggest Ireland by 3


Teamsheets haven't been announced yet. May update this tomorrow.


Simulation Prediction: Ireland by 5.5

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Ireland Victory | 77.3% |
| Scotland Victory | 17.6% |
| Tie | 5.1% |
| Ireland Losing Bonus Point | 15.1% |
| Scotland Losing Bonus Point | 39.2% |
| Ireland 4 Try Bonus Point (BETA) | 16.1% |
| Scotland 4 Try Bonus Point (BETA) | 2.8% |

EDIT (3/11)
Lineup model is saying Ireland by 8.5, which makes sense as it's been liking Ireland. Rightly. So maybe a strong Ireland win without a Scotland bonus point, which would pretty much determine the final outcomes.

# Simulation for the Next Two Weeks

| Team | Average Wins | Average Point Differential | Average Competition Points (_NOW WITH_ Future 4 Try Bonuses) |
| ---- | ------------ | -------------------------- | ------------------------------------------------ |
| Ireland     | 3 + 1.76 = 4.76 | 51  + 18.2 = 69.2 | 15 + 7.8 = 22.8 |
| France      | 2 + 1.54 = 3.54 | 3   + 17.2 = 20.2 | 10 + 7.1 = 17.1 |
| Scotland    | 2 + 1.17 = 3.17 | 23  + 8.1 =  31.1 | 10 + 5.6 = 15.6 |
| England     | 2 + 0.48 = 2.48 | 21  + -13.6 = 7.4 | 10 + 2.6 = 12.6 |
| Italy       | 0 + 0.71 = 0.71 | -36 + -10.5 = -46.5 | 1  + 3.3 = 4.3 |
| Wales       | 0 + 0.33 = 0.33 | -62 + -19.4 = -81.4 | 0  + 1.8 = 1.8 |

Simulations now include an estimate of 4 try bonus points, but it's a conservative estimate that is rarely given except to teams that are pretty strong favorites and/or tend to score four or more tries each match. That addition, and last week's results, seem to have put Ireland firmly in charge, with France, Scotland, and England chasing second place. This weekend should decide most of the final table.