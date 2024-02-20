---
title:  "Warmups and Friendlies"
date:   2024-02-21 06:00:00 -0500
categories: projection 
---

In the leadup to Super Rugby Pacific starting, there's been a bunch of pre-season games between the teams, and some cross competition matches as well. The question always is how 'real' were those matches? The Crusaders and Highlanders teams who played on the 16th likely won't be the same as the teams that take the field in round 1 - either due to different player selection, gameplans saved for the competition's start, or any number of other reasons. But at the same time, this is the best gauge of the teams we have since the finals last summer. And we get to compare these teams against some teams in Japan and Europe. So there is some value here, even if its hard to quantify.

Looking at a few of the matches, the team-sheets look solid, and individual players have no real reason to perform poorly in these matches - they would want to put on a good showing for the coaching staffs. There's a bit of load management, but that should be happening on both sides. So I think it may be best to consider these matches, but not as strongly as an in-season match. A dampening to about 70-80% impact would allow us to account for that fact that these games don't have full stakes while also still comparing teams that rarely play each other.

Getting data for these matches is another problem entirely. I can manually get the scores and times for each match, which is a fine starting point. But most of these matches don't have a record of when substitutes and scores occurred, which we need for the player model. 

So we'll use them for the club model, limit their importance to about 3/4ths of a usual game, and hope that that improves the model's accuracies. We can check back in a few weeks and see if we were right.