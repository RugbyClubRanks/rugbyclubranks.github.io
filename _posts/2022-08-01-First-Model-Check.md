---
title:  "First Model Check"
date:   2022-08-01 18:00:00 -0500
categories: model update
mathjax: true
---
There are a lot of moving parts in an elo calculation. For each match, we have as elo score for each team (elo<sub>t</sub>) that is calculated using elo scores for each of the players (elo<sub>i</sub>) on the teamsheet. The exact computation of this team score will be changed later, but currently its a contribution system, with each player contributing to the team's elo proportionally to their time on the field - if a player is on the field for the entire game, their elo score will contribute more than that of a player who was only active for the last ten minutes of the match. Essentially, 

{% raw %}
$$elo_{t} = \sum_{i} elo_{i} * minutes_{i}$$
{% endraw %}

To assess our model, we just compare the predictions made to the observed outcomes. We have a binary prediction for the winner, and a numeric prediction for the expected margin of victory. That allows us to use two types of metrics - a Brier score for the binary model and a root mean squared error for the margin of victory. Overall, this first pass of the model has a Brier of 0.23052 and a RMSE of 11.68. These are definitely numbers, but alone don't provide much insight into how good the model may be. To get some idea of model usefulness, we can compare these metrics to what we would get from a naïve model that predicts the home team will win each game by whatever the home parameter is set to (which was 5 for this first pass, an unconverted try). This naïve model gives a Brier score of 0.3667 and a RMSE of 19.04.

| Model | Brier Score | RMSE|
|-----|------|-----|
|naïve | 0.36677 | 19.04 |
|elo | 0.23052 | 11.68 |

Our model beats the naïve model for both of these metrics, so there's at least some predictive value here. Or I've chosen a poor naïve model. Either way, next steps would be to see what types of games the model is particularly good or bad at predicting, what model parameters result in the most accurate predictions, and what other naïve models may be accurate. And probably some other things as well. We'll see.