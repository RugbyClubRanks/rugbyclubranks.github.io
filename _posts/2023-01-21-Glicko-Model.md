---
title:  "Glicko Model"
date:   2023-01-21 18:00:00 -0500
categories: model update
---

Now that I've finally filled the holes in my dataset and have some decent predictions, I was able to start on version two - a glicko model. The ability to generate predictions with uncertainty and work with distributions should allow for more nuanced and useful predictions. But its a big change to make, so I'm implementing it in parts. To be _Agile_. This first pass ignores players, and has scores for each club to drastically reduce the number of objects to create and juggle. 

In this first pass, without any home advantages or consideration of margin of victory, I was able to slightly exceed the accuracy I achieved with elo scores for each club. Which is promising as those two things seem to be more difficult to implement in a glicko system. They'll be future improvements, but for now I am able to generate some expected performances (in this example for the Sharks/Quinns game I was watching as I started this):

![Glicko Performance Example](/assets/glicko_performance_example.png)

## Player Level Comparison

My first pass at predictions was only able to create one prediction and one spread, and doesn't capture the space of possibilities. For the same match, I predicted the Sharks to win by 0.1 once lineups were announced and the Harlequins to win by 2.3 when weighting with player minutes (which is sort of a retrospective prediction, but that's why I make a few types). Before lineups were announced and added to my calculations, I had to average recent team elos, and had predicted the Sharks by about 4, even after a 4 point home advantage to the Harlequins. The Sharks ended up losing by 10, and it felt worse than that. So there's still some work to do with accuracy.
