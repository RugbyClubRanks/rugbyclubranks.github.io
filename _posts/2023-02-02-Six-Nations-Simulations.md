---
title:  "Six Nations Simulations"
date:   2023-02-02 18:00:00 -0500
categories: projection
---

# Method
Now that I can generate expected performances for any given team, I figured I could test out what I can do by trying to simulate an entire competition, and the Six Nations came around at the perfect time. I simulated each match in the competition and updated team rankings using the simulated result before simulating the next week's matches, arriving at a simulated tournament result. I did this 10,000 times, giving us a large number of potential tournament outcomes to work with. Unfortunately, I don't currently predict if a team scores at least four tries - just the win, loss, and a loss within 7 points. So for now, any tournament point projections may be a bit off and I'll try to keep that front of mind. Here's how some of the simulations break down.

# Overall Projections
Averaging the results for each of my 10,000 tournaments, here's my projected table

| Team | Average Wins | Average Point Differential | Average Competition Points (Without 4 Try Bonus) |
| ---- | ------------ | -------------------------- | ------------------------------------------------ |
| Ireland     | 4.83 | 61.10  | 19.46 |
| France      | 3.46 | 34.26  | 14.70 |
| England     | 3.31 | 26.61  | 14.07 |
| Scotland    | 1.74 | -16.77 | 7.82  |
| Wales       | 1.60 | -19.26 | 7.82  |
| Italy       | 0.06 | -85.9  | 0.7   |

That puts Ireland as the strong favorites hoping for a Grand Slam, France and England competing for second, Scotland and Wales competing for fourth, and Italy hoping for a close loss. Seems pretty sane, with Ireland having what should be their toughest matches at home. Again, this doesn't award any bonus points for scoring four tries - last year Ireland did that in four of their five matches, France did it twice, and both England and Scotland did it once. So those bonus points shouldn't change the standings much. Another thing that's not accounted for, technically, is the coaching changes for England and Wales. There's already some uncertainty added into the projections as none of these teams have played in a couple months, but if we add a bit more uncertainty to account for coaching changes we'd expect England to do just a bit worse, and Wales just a bit better.

# Some Fun Results
* Ireland achieves a Grand Slam in 82% of simulations
* France achieves a second Grand Slam in only 3.2% of simulations 
* Italy fails to score any competition points in 52% of simulations, but does beat both Wales and _France_ in the only simulation where they win more than one match

# Match Overviews

## Weekend 1

None of the matches opening weekend look to be particularly close, but are great places for Wales, Scotland, and Italy to get some losing bonus points. My model doesn't think the Calcutta Cup will be very close, but it's also the first match for England's new coach, and the Scottish team that has been announced looks a good deal different than previous teams (My player model has Scotland winning by 6). It's a rivalry with interesting wrinkles, a good underdog story, and plenty of new faces. Perfect recipe for a great watch.

### Wales v Ireland

Simulations have Ireland winning by 9.69 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Ireland Victory | 65.62% |
| Ireland Victory, Losing Bonus Point | 29.63% |
| Wales Victory, Losing Bonus Point | 3.08% |
| Tie | 1.59% |
| Wales Victory | 0.08% 

### England v Scotland

Simulations have England winning by 10.29 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| England Victory | 69.83% |
| England Victory, Losing Bonus Point | 26.5% |
| Scotland Victory, Losing Bonus Point | 2.16% |
| Tie | 1.48% |
| Scotland Victory | 0.03% |

### Italy v France

Simulations have France winning by 17.72 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| France Victory | 95.72% |
| France Victory, Losing Bonus Point | 4.1% |
| Italy Victory, Losing Bonus Point | 0.09% |
| Tie | 0.09% |

## Weekend 2

Ireland v France is an early test for each team, with the winner likely to win  the competition. In simulations where France wins the match, they go on to win the competition 78.5% of the time; when Ireland wins the match, they go on to win the competition 95% of the time. Elsewhere, Scotland v Wales ought to be a close game and Italy likely hosts a relatively green England team. The prediction leans heavily to England, but it may be a much closer game, especially in the first 60 minutes before reserves impact the game.

### Ireland v France

Simulations have Ireland winning by 7.66 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Ireland Victory | 51.1% |
| Ireland Victory, Losing Bonus Point | 38.94% |
| France Victory, Losing Bonus Point | 6.7% |
| Tie | 2.91% |
| France Victory | 0.35% |

### Scotland v Wales

Simulations have Scotland winning by 2.64 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Scotland Victory, Losing Bonus Point | 47.22% |
| Wales Victory, Losing Bonus Point | 25.29% |
| Scotland Victory | 18.24% |
| Tie | 6.63% |
| Wales Victory | 2.62% |

### England v Italy

Simulations have England winning by 22.09 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| England Victory | 99.4% |
| England Victory, Losing Bonus Point | 0.58% |
| Italy Victory, Losing Bonus Point | 0.01% |
| Tie | 0.01% |

## Weekend 3

Italy ought to have a rough go in Ireland, while France should be mostly comfortable in Scotland. The best game ought to be Wales and England, where England and Borthwick may just overcome Wales and Gatland. Both coaches and their squads come in with a lot to prove (or re-prove), but the Welsh home field and familiarity may not be enough.

### Italy v Ireland

Simulations have Ireland winning by 22.05 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Ireland Victory | 99.33% |
| Ireland Victory, Losing Bonus Point | 0.67% |

### Wales v England

Simulations have England winning by 2.94 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| England Victory, Losing Bonus Point | 47.35% |
| Wales Victory, Losing Bonus Point | 23.45% |
| England Victory | 20.07% |
| Tie | 6.35% |
| Wales Victory | 2.78% |

### France v Scotland

Simulations have France winning by 12.71 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| France Victory | 83.2% |
| France Victory, Losing Bonus Point | 15.46% |
| Scotland Victory, Losing Bonus Point | 0.77% |
| Tie | 0.56% |
| Scotland Victory | 0.01% |

## Weekend 4

The last two weeks are Italy's best chance to get a win, and repeating against Wales seems the most likely. Not likely, but the most likely. If there weren't a week off after round 3, this would look like the perfect trap game, with Wales coming off of England and looking ahead to France. But both teams likely have had this circled for months. In another big match, England will need all the help Twickenham can give to win what should be a very close game. It looks like it will be a great day of matches. Then on Sunday, Ireland should beat Scotland.

### Italy v Wales

Simulations have Wales winning by 8.93 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Wales Victory | 59.91% |
| Wales Victory, Losing Bonus Point | 33.41% |
| Italy Victory, Losing Bonus Point | 4.67% |
| Tie | 1.84% |
| Italy Victory | 0.17% |

### England v France

Simulations have England winning by 1.43 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| England Victory, Losing Bonus Point | 43.55% |
| France Victory, Losing Bonus Point | 31.63% |
| England Victory | 13.13% |
| Tie | 6.77% |
| France Victory | 4.92% |

### Scotland v Ireland

Simulations have Ireland winning by 11.56 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Ireland Victory | 78.36% |
| Ireland Victory, Losing Bonus Point | 20.01% |
| Scotland Victory, Losing Bonus Point | 1.02% |
| Tie | 0.61% |

## Weekend 5

Going into the final weekend, the average simulated table looks like this:

| Team | Average Wins | Average Point Differential | Average Competition Points (Without 4 Try Bonus) |
| ---- | ------------ | -------------------------- | ------------------------------------------------ |
| Ireland     | 3.86 | 50.96  | 15.56 |
| England     | 3.28 | 36.75  | 13.68 |
| France      | 2.47 | 21.34  | 10.72 |
| Wales       | 1.59 | -6.35  | 7.64  |
| Scotland    | 0.74 | -31.92 |  3.84 |
| Italy       | 0.06 | -70.79 |  0.62 |

Missing the four try bonus points makes it hard to say too much, but the winner of the Ireland v England match may win the whole tournament - assuming they were both able to beat France when they hosted Les Bleus. If France was able to win either - or both - of those matches, they'd likely just have to beat Wales and hope for few bonus points in the late match. Either way, Ireland hosting England in Dublin the day after St. Patrick's Day should provide a great atmosphere.

As for Scotland and Italy... this is one Scotland ought to win, and likely needs to to avoid the wooden spoon. Both teams may be looking ahead to the fall and the World Cup, as success there can easily wash away all memory of a poor performance in the spring.

### Scotland v Italy
Simulations have Scotland winning by 15.15 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Scotland Victory | 91.8% |
| Scotland Victory, Losing Bonus Point | 7.71% |
| Italy Victory, Losing Bonus Point | 0.25% |
| Tie | 0.24% |

### France v Wales
Simulations have France winning by 12.91 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| France Victory | 84.51% |
| France Victory, Losing Bonus Point | 14.55% |
| Wales Victory, Losing Bonus Point | 0.61% |
| Tie | 0.32% |
| Wales Victory | 0.01% |

### Ireland v England
Simulations have Ireland winning by 10.14 points, on average.

| Outcomes | Occurrence in Simulation |
| -------- | ----------------------- |
| Ireland Victory | 68.82% |
| Ireland Victory, Losing Bonus Point | 27.56% |
| England Victory, Losing Bonus Point | 2.22% |
| Tie | 1.35% |
| England Victory | 0.05% |
