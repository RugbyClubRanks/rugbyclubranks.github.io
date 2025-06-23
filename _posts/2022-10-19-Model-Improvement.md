---
title:  "Model Improvement"
date:   2022-10-19 18:00:00 -0500
categories: model update
---

Model improvement was something I wanted to tackle much earlier, but some issues with data coverage became very apparent over the summer and became a higher priority. Now that I have most of the leagues I want, I can focus a bit more in the math. Before tinkering with the computation of a team's elo (because intuitively, a player should contribute proportionally to their time on the pitch, and I would like to have a version that is position agnostic before I generate something I disappointedly suspect will favor backs over forwards), I spent a bit of time running a basic search across the easy parameters of this elo calculation.

## Summary of Changes

* The home field advantage of 5 seemed to be sane, but it varies heavily across competitions and levels. For now, its kept at 5 but is a target for future improvement.
* Learning speed was increased a bit, by about 25%. My suspicion is that this allows for new players to reach stable elos quicker.
* Some of the interior parameters (margin of victory addition) was bumped down about 10%.
* 'New' players are now given a starting elo equal to 90% of the their team's pre-match average when they debut on a lineup.
* The floor for the starting elo score for new players is now 60.


This investigation also revealed a lack of stability in elo scores - the median value seemed to drop over time. As the priority, for now, is to accurately predict current matches and compare current players, this isn't too much of an issue. But the 'burn in' period was extended a bit through 2012, to include another world cup and the first bit of the next cycle. 

