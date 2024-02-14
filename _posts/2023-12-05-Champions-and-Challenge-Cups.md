---
title:  "Champions and Challenge Cups"
date:   2023-12-05 06:00:00 -0500
categories: projection challenge champions
---

These are some of my favorite competitions, because it is so hard to predict what might happen. We toss together three separate leagues, add in some teams that rarely play anyone else in these competitions, and also have club managers trying to balance success here and in their own league, as the matches alternate through the spring (spring in the Northern Hemisphere, at least). Its a mess, and its fun.

Its also a great opportunity to gather some data for our predictions. We have some matches in these competitions, then some more matches in the usual component competitions, and can use all of them to update our predictions each week. We expect the club level models to be a bit off at the start of the competition, but within a few weeks we should learn a lot - seeing how leagues perform against the other teams gives us lots of new data points to adjust ratings appropriately, and we'd expect the predictions we make after one or two weeks of pool matches to be much more accurate than the ones we can make today.

We'd also expect our player models to perform a good bit better than the club models. Plenty of these players have just played with or against each other in the world cup, so we expect those ratings to be a bit better tuned. But it's very hard to make predictions far into the future with the player model, so we'll just be using the club model here. 

## Champions Cup

This year, we have four pools where teams ought to play the teams that are in their pool but not in their usual competition. Then the top four teams from each pool advance into the knockout stages, while the fifth best team in each pool will actually move into the knockouts of the Challenge Cup, getting an away match in the first knockout round. This does allow for the strange edge cases where a strong team performs poorly in their pool, then is highly favored to win the Challenge Cup. Which does happen to Leinster in one of our predictions.

|                      | Reach Round of Sixteen   | Reach Quarterfinals   | Reach Semifinals   | Reach Final   | Win Final   |
|:---------------------|:-------------------------|:----------------------|:-------------------|:--------------|:------------|
| Leinster             | 99.9 %                   | 97.9 %                | 93.1 %             | 85.3 %        | 77.7 %      |
| Munster              | 98.5 %                   | 77.4 %                | 52.0 %             | 27.3 %        | 8.7 %       |
| Stade Toulousain     | 98.1 %                   | 72.7 %                | 48.1 %             | 21.5 %        | 3.2 %       |
| Bulls                | 87.7 %                   | 61.8 %                | 29.1 %             | 12.3 %        | 2.5 %       |
| Saracens             | 93.8 %                   | 66.2 %                | 32.2 %             | 11.2 %        | 2.1 %       |
| La Rochelle          | 68.3 %                   | 36.0 %                | 12.3 %             | 3.9 %         | 1.4 %       |
| Glasgow Warriors     | 91.7 %                   | 54.6 %                | 26.4 %             | 9.2 %         | 1.1 %       |
| Stormers             | 77.4 %                   | 42.7 %                | 15.8 %             | 5.5 %         | 1.0 %       |
| Exeter Chiefs        | 85.9 %                   | 42.0 %                | 19.0 %             | 6.7 %         | 0.7 %       |
| Harlequins           | 84.7 %                   | 37.9 %                | 15.4 %             | 3.5 %         | 0.5 %       |
| Leicester Tigers     | 57.7 %                   | 20.8 %                | 5.4 %              | 1.5 %         | 0.5 %       |
| Ulster               | 56.8 %                   | 22.6 %                | 7.8 %              | 2.3 %         | 0.3 %       |
| Toulon               | 67.7 %                   | 25.4 %                | 9.6 %              | 3.3 %         | 0.1 %       |
| Racing 92            | 88.0 %                   | 40.5 %                | 13.8 %             | 3.2 %         | 0.1 %       |
| Sale Sharks          | 74.1 %                   | 20.4 %                | 5.2 %              | 1.3 %         | 0.1 %       |
| Bordeaux Begles      | 71.5 %                   | 26.3 %                | 5.4 %              | 0.7 %         | 0.0 %       |
| Bristol Rugby        | 46.1 %                   | 9.4 %                 | 1.6 %              | 0.5 %         | 0.0 %       |
| Bath Rugby           | 68.8 %                   | 19.0 %                | 3.9 %              | 0.3 %         | 0.0 %       |
| Connacht             | 46.7 %                   | 7.6 %                 | 1.0 %              | 0.3 %         | 0.0 %       |
| Lyon                 | 54.2 %                   | 12.6 %                | 2.0 %              | 0.1 %         | 0.0 %       |
| Northampton Saints   | 50.3 %                   | 5.7 %                 | 0.9 %              | 0.1 %         | 0.0 %       |
| Stade Francais Paris | 22.6 %                   | 0.3 %                 | 0.0 %              | 0.0 %         | 0.0 %       |
| Bayonne              | 5.9 %                    | 0.1 %                 | 0.0 %              | 0.0 %         | 0.0 %       |
| Cardiff Blues        | 3.6 %                    | 0.1 %                 | 0.0 %              | 0.0 %         | 0.0 %       |



## Challenge Cup
In the challenge cup, the top four teams from each pool will also advance, then be joined by the 5th place teams from the champions cup. This gives us a ton of possible permutations, before we even consider the invitational sides. The Cheetahs have not played many matches outside of these competitions, and Black Lion have not played any of these teams yet - both have some very wide variances and our model has some predictions where they do very well, and some where they do very poorly. It'll be fun to see how they do, especially as they don't have another competition to balance their player management with (Yeah, the Black Lion is wrapping up the Rugby Europe Super Cup, but there's just a match remaining there).


|                      | Reach Round of Sixteen   | Reach Quarterfinals   | Reach Semifinals   | Reach Final   | Win Final   |
|:---------------------|:-------------------------|:----------------------|:-------------------|:--------------|:------------|
| Lions                | 98.9 %                   | 75.9 %                | 49.0 %             | 30.1 %        | 14.9 %      |
| Black Lion           | 75.6 %                   | 51.1 %                | 31.9 %             | 21.0 %        | 12.8 %      |
| Clermont Auvergne    | 90.1 %                   | 61.7 %                | 38.5 %             | 21.7 %        | 11.9 %      |
| Edinburgh            | 87.6 %                   | 58.0 %                | 35.7 %             | 18.8 %        | 9.2 %       |
| La Rochelle          | 25.1 %                   | 19.2 %                | 11.5 %             | 7.8 %         | 6.9 %       |
| Castres Olympique    | 83.8 %                   | 51.7 %                | 27.4 %             | 13.1 %        | 6.7 %       |
| Pau                  | 99.7 %                   | 62.0 %                | 34.0 %             | 15.4 %        | 5.0 %       |
| Benetton Treviso     | 95.7 %                   | 59.9 %                | 31.3 %             | 14.9 %        | 4.9 %       |
| Leicester Tigers     | 23.5 %                   | 15.3 %                | 8.2 %              | 4.2 %         | 3.4 %       |
| Toulon               | 26.7 %                   | 16.8 %                | 7.7 %              | 4.0 %         | 2.7 %       |
| Sale Sharks          | 19.3 %                   | 11.9 %                | 6.1 %              | 3.2 %         | 2.7 %       |
| Sharks               | 94.4 %                   | 46.2 %                | 17.8 %             | 7.4 %         | 2.3 %       |
| Montpellier Herault  | 88.8 %                   | 46.7 %                | 18.9 %             | 6.8 %         | 1.9 %       |
| Stormers             | 12.8 %                   | 8.2 %                 | 4.3 %              | 1.8 %         | 1.5 %       |
| Exeter Chiefs        | 10.5 %                   | 6.1 %                 | 3.1 %              | 1.7 %         | 1.4 %       |
| Cheetahs             | 68.1 %                   | 18.5 %                | 5.8 %              | 2.9 %         | 1.2 %       |
| Saracens             | 4.8 %                    | 3.1 %                 | 2.2 %              | 1.5 %         | 1.2 %       |
| Oyonnax              | 98.5 %                   | 46.2 %                | 20.0 %             | 7.4 %         | 1.1 %       |
| Ulster               | 37.7 %                   | 19.3 %                | 6.6 %              | 1.9 %         | 1.1 %       |
| Bulls                | 8.2 %                    | 4.9 %                 | 2.8 %              | 1.8 %         | 1.1 %       |
| Stade Toulousain     | 1.9 %                    | 1.6 %                 | 1.1 %              | 0.8 %         | 0.8 %       |
| Gloucester Rugby     | 46.1 %                   | 17.2 %                | 7.4 %              | 3.1 %         | 0.7 %       |
| Harlequins           | 12.7 %                   | 6.6 %                 | 2.9 %              | 0.9 %         | 0.7 %       |
| Munster              | 1.5 %                    | 1.2 %                 | 1.1 %              | 0.9 %         | 0.7 %       |
| Racing 92            | 11.3 %                   | 5.9 %                 | 2.7 %              | 1.0 %         | 0.6 %       |
| Glasgow Warriors     | 6.4 %                    | 3.8 %                 | 1.8 %              | 0.8 %         | 0.5 %       |
| Northampton Saints   | 41.3 %                   | 15.0 %                | 3.6 %              | 0.9 %         | 0.4 %       |
| Bath Rugby           | 24.5 %                   | 8.6 %                 | 2.6 %              | 0.8 %         | 0.3 %       |
| Connacht             | 21.5 %                   | 6.7 %                 | 2.1 %              | 0.6 %         | 0.3 %       |
| Ospreys              | 60.6 %                   | 10.1 %                | 2.5 %              | 0.5 %         | 0.3 %       |
| Lyon                 | 22.9 %                   | 8.9 %                 | 2.5 %              | 0.7 %         | 0.2 %       |
| Bordeaux Begles      | 17.1 %                   | 6.8 %                 | 2.2 %              | 0.5 %         | 0.2 %       |
| Stade Francais Paris | 19.2 %                   | 6.4 %                 | 1.2 %              | 0.3 %         | 0.2 %       |
| Bristol Rugby        | 25.5 %                   | 7.2 %                 | 1.8 %              | 0.4 %         | 0.1 %       |
| Leinster             | 0.1 %                    | 0.1 %                 | 0.1 %              | 0.1 %         | 0.1 %       |
| Perpignan            | 35.5 %                   | 3.1 %                 | 0.2 %              | 0.2 %         | 0.0 %       |
| Scarlets             | 16.8 %                   | 3.4 %                 | 0.8 %              | 0.1 %         | 0.0 %       |
| Bayonne              | 13.6 %                   | 1.7 %                 | 0.3 %              | 0.0 %         | 0.0 %       |
| Newcastle Falcons    | 20.5 %                   | 1.6 %                 | 0.2 %              | 0.0 %         | 0.0 %       |
| Cardiff Blues        | 11.9 %                   | 1.3 %                 | 0.1 %              | 0.0 %         | 0.0 %       |
| Dragons              | 23.6 %                   | 0.1 %                 | 0.0 %              | 0.0 %         | 0.0 %       |
| Zebre                | 15.7 %                   | 0.0 %                 | 0.0 %              | 0.0 %         | 0.0 %       |
