---
layout: article
titles: About
key: page-about
---
## About This Site

As an amateur rugby union player and a less amateur statistician in the US, this is a project that has been in the back of my mind for a very long time. Coverage of our mainstream sports are littered with analytics that seek to capture player performance and potential. The few rugby broadcasts that we get are not, and the absence is glaring. Even more so for new viewers, who lack the context to know if an 60% scrum success rate is a good or bad thing. Since we have predictions like spreads and mid-match win probability in other sports, I figured that it wouldn't be too difficult to calculate some of these for rugby.

Turns out it's a bit complicated. I started pursuing this years ago, as a school project for logistic regression focused on just the Six Nations. Then moved to the Premiership, to try to use the increased number of matches to expand my dataset and attempt to create some spreads. Over time I've expanded it to most professional competitions and increased the predictive complexity to allow me to model individual clubs and individual players with a skill distribution model.

So now I have reviews of matches, with projected winners and spreads for future matches. There's a model that uses clubs as the smallest object, making the assumption that an individual player is nothing without the coaching, support system, and rest of the team on the field. And there's an entirely separate model that treats the athlete as the smallest object - which is predictably more complicated, but has the potential to more accurately capture the effects of player selection and movement across teams or competitions. And it could try to answer some of the impossible questions, like if Leinster would beat the Irish national team or if the Crusaders would win the European Champions Cup if they somehow were invited.

Both models are present on this site, but it should be clear which predictions are made by which model. The accuracies of both are still improving over time, as more matches are played and more work is done to improve the models. 

For the 2023 Six Nations, the club model was right for 12 of the 15 matches, while the player model only missed one - it predicted that Italy would beat Wales at home in week 4. We'll see how much we can improve, and how complicated it gets.

## About Me

This may get fleshed out later. For now, you can contact me via email at rugbyclubrankings@gmail.com. Feel free to leave any feedback, even if it's just that I got your favorite club's colors wrong.

[Also, check us out everywhere else](https://linktr.ee/rugbyclubranks)
