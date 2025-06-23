---
title:  "Six Nations After Round 1"
date:   2023-02-09 18:00:00 -0500
categories: projection review
---

# Current Table

| Team | Wins | Point Differential | Competition Points |
| ---- | ------------ | -------------------------- | ------------------------------------------------ |
| Ireland     | 1 | 24  | 5 |
| Scotland    | 1 | 6 | 5  |
| France      | 1 | 5  | 5 |
| Italy       | 0 | -5  | 1   |
| England     | 0 | -6  | 1 |
| Wales       | 0 | -24 | 0  |

Some surprises all around in the first weekend. Italy has already surpassed the projected number of competition points from last week - and against France too. Both new coaches had rough starts, Scotland looks like they could be a force to be reckoned with (or England has a lot of work to do. Or both.), and Ireland has set themself up well for this week.

# Model Review

Of the first three matches, the club level model is 2 of 3, and both player level models are 3 of 3. This does make a bit of sense, as we have new coaches and new players in most camps. But I was hoping for a bit more accuracy from the club models.
To note - the predictions here may be a little bit different from the one's in last week's post. All the underlying models are still in development, and have been tweaked a bit. Most notably by reworking the margin of victory consideration, so now matches like Ireland stomping Wales by more than expected should increase Ireland's rank and decrease Wales', while matches like Italy narrowly winning what was thought should be a blowout increases Italy's ranking and decreases France's.
All number are using the most recent models, and always predict a match using only data available before that match kicks off. Except for the Player Minutes model, of course, as we need the match to be played to see how long any player is on the field.

| Match | Club Level Prediction | Lineup Prediction | Minutes Prediction |
| ---- | ----- | ----- | ----- | 
| IRE @ WAL | IRE by 10.1 | IRE by 18.1 | IRE by 19.4 |
| SCO @ ENG | ENG by 6.3  | SCO by 7.1  | SCO by 4 |
| FRA @ ITA | FRA by 10.7 | FRA by 12.7 | FRA by 11 |
| - | - | - | - | 
| Average Errors | 10.6 | 5.0 | 4.2 | 

For a bit more depth, check out the match recaps in the [Recent Matches page](..//Recent_Matches.md)

# Week Two Projections

Club ratings have been updated from last week's outcomes, so we re-ran simulations and have new projections. For a bit more depth, check out the match predictions in the [Current Projections page](..//Current_Projections.md)

## Ireland v France

Club Model: Ireland by 8.7

Lineup Model: Ireland by 26.0

France did struggle in Rome, but it seems extreme to have Ireland by 26. The player models put Sheehan just ahead of Herring, so that change shouldn't hurt Ireland much, and France is bringing back the same lineup from last weekend. I would expect them to play better this week, so we'll likely fall somewhere in between these two predictions.  

Simulations now have Ireland winning by 8.2 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Ireland Victory | 55.2% |
| Ireland Victory, Losing Bonus Point | 31.6% |
| France Victory, Losing Bonus Point | 9.1% |
| Tie | 2.7% |
| France Victory | 1.4% |

## Scotland v Wales

Club Model: Scotland by 12.1

Lineup Model: Scotland by 27.7

This is a big improvement for Scotland's odds, which makes sense after their big win (upset even, according to the Club Model) and Wales' poor performance at home. Of course, being the Six Nations, this could still be a very close match.

Simulations now have Scotland winning by 11 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Scotland Victory | 70.7% |
| Scotland Victory, Losing Bonus Point | 23.8% |
| Wales Victory, Losing Bonus Point | 3.1% |
| Tie | 2.1% |
| Wales Victory | 0.3% |

## England v Italy

Teamsheets haven't been announced yet. May update this tomorrow. As is, A 5% chance for England to lose again at home sounds like it could be a perfect story for Italy.

Update: The club model has England by 12.4, but with teamsheets the player model only has England by 6.6. And 4 of that is from home field advantage. Could be a close match.

Simulations now have England winning by 11.4 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| England Victory | 69.9% |
| England Victory, Losing Bonus Point | 23.5% |
| Italy Victory, Losing Bonus Point | 5.1% |
| Tie | 1.4% |
| Italy Victory | 0.1% |


# Simulation for the Next Four Weeks

| Team | Average Wins | Average Point Differential | Average Competition Points (Without Future 4 Try Bonuses) |
| ---- | ------------ | -------------------------- | ------------------------------------------------ |
| Ireland     | 1 + 3.66 = 4.66 | 24  + 42.43  = 66.43 | 5 + 14.9  = 19.9   |
| France      | 1 + 2.65 = 3.65 | 5   + 17.71  = 22.71 | 5 + 11.26 = 16.26 |
| Scotland    | 1 + 2.24 = 3.24 | 6   + 10.07  = 16.07 | 5 + 9.75  = 10.85 |
| England     | 0 + 1.95 = 1.95 | -6  + -2.37  = -8.37 | 1 + 8.64  = 9.64  |
| Italy       | 0 + 0.7  = 0.7  | -5  + -37.02 = -42.02| 1 + 3.63  = 4.63  |
| Wales       | 0 + 0.81 = 0.81 | -24 + -30.82 = -54.92| 0 + 4.33  = 4.33  |

Another 10,000 simulations of the next four weeks, combined with the actual results from the first weekend, gives us the above table. England and Wales are off to a rough start with home losses, and the model is penalizing their future prospects in light of that poor showing. On the other side, Italy is being rewarded for their close match.

## Some Fun Results

* With the new model that better considers margin of victory, Ireland have a 67% chance to win a Grand Slam. 
* France's Grand Slam chances are at 6.7% and Scotland's are at 2.3%, but you never know. Maybe.
* Ireland has a 13.2% chance to fail to win at home against France, but a _20.6%_ chance to come up short in Scotland now in week 4.
* Italy now has a 59.4% chance to win a match, most of that coming from it's 56% chance to beat Wales again. But they also have a 5% chance to win this weekend at Twickenham - which would be their first victory against England.
* Wales' best chance for a win is against Italy, with a nearly 40% chance, followed closely by their home match against England, with a 32% chance.