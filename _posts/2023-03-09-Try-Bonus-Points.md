---
title:  "Model for Try Bonus Points"
date:   2023-03-09 18:00:00 -0500
categories: model update
---

## The Problem: Try Bonus Points
Most rugby competitions are scored using competition points rather than just wins and losses to try and make matches more interesting. The usual system awards 4 points for a win, 2 for a draw, 0 for losing, and then two ways to get a bonus point: 1 point is awarded for losing by seven or fewer points, and one is awarded for scoring at least four tries. This last one was a bit more challenging for my predictions. I've been predicting just margins of victories, not final point totals, and definitely not how those points are scored. So the losing bonus point was simple, whereas the try bonus point needed an entirely separate system. Which I now have in a basic binary predictor model.

## The Solution
Since we do have a record of scoring for a bunch of played games, we have an idea of where try bonus points have been scored in the past. So I can predict when they'll be scored in the future. This first pass solution considers the ratings and names of both clubs, the location, the competition, and the projected outcome to then predict if each of the teams score four tries or more. It's reasonably accurate, but I have erred on the side of caution - its a bit less likely to award the bonus points than they're seen in actual matches. We'll see how much this affects the competition projections over time. 
Overall we have an accuracy of about 75%, but a precision of 80% and recall of just 55% for the positive case (awarding the bonus point). This should make the bonus points less likely to swing projections too much, but they'll be in their own column for a while to make things more transparent.

And yes, I know France and SANZAAR have their own slightly different systems. But this should cover most competitions.

We'll see them in the Six Nations Prediction tomorrow.