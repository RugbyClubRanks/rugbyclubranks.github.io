---
title:  "Rugby World Cup - 2 Week Update"
date:   2023-09-19 06:00:00 -0500
categories: projection
---

# Model Review

Now that we're nearly two weeks into the competition, we can evaluate our predictions for the first couple weekends and see what may lie ahead. Overall, predictions have been great. 

The club based model only had two incorrect picks, calling Argentina over England by 3 and Fiji over Wales by 7. Not too mad about both of those - Argentina and England look like very different teams now that the tournament has started, and Fiji was that close to the win. Not sure you'd want to have anyone other than Radradra on the edge there (he was out second highest rated player on the field, just after Nayacalevu).

The player model was as good, just missing two as well. Wales and Fiji again, of course - the player model only had Fiji by 3 pregame and 4 when accounting for how long each player was on the pitch - but it also missed Australia and Georgia, favoring Georgia by 6 prematch and 7 with playing time. So we may be overvaluing Georgia or overvaluing Australia, but we're guessing it was a bit of both, as we had Fiji beating Australia by 12 instead of just 7 last weekend too. Keeping a close eye on the model for pool C for now. 

That gives us this table - good at picking winners, not so great at spreads. But a lot of that was from underestimating margins like what New Zealand had over Namibia or South Africa had over Romania.

| Model | Percent Correct Predictions | Spread Error |
| ------ | ------ | ------ |
| Club Level | 87.5% | 17.9 |
| Player Level: Lineup | 87.5% | 20.0 |
| Player Level: Minutes | 87.5% | 19.9 |

# Changes to Future Predictions

As things stand now, here's our predictions of the knockout stages.

|              | Reach Quarterfinals   | Reach Semifinals   | Reach Bronze Final   | Win Bronze   | Reach Final   | Win Final   |
|:-------------|:----------------------|:-------------------|:---------------------|:-------------|:--------------|:------------|
| South Africa | 97.9 %                | 70.3 %             | 0.8 %                | 0.8 %        | 69.5 %        | 45.2 %      |
| Ireland      | 91.0 %                | 63.0 %             | 1.0 %                | 0.9 %        | 62.0 %        | 32.2 %      |
| France       | 95.3 %                | 47.0 %             | 1.4 %                | 1.4 %        | 45.6 %        | 18.4 %      |
| New Zealand  | 95.3 %                | 18.6 %             | 0.8 %                | 0.7 %        | 17.8 %        | 4.1 %       |
| Fiji         | 66.9 %                | 43.1 %             | 41.2 %               | 24.7 %       | 1.9 %         | 0.1 %       |
| Australia    | 74.9 %                | 49.9 %             | 48.9 %               | 28.5 %       | 1.0 %         | 0.0 %       |
| Scotland     | 11.0 %                | 1.1 %              | 0.2 %                | 0.2 %        | 0.9 %         | 0.0 %       |
| England      | 93.5 %                | 42.2 %             | 41.6 %               | 18.2 %       | 0.6 %         | 0.0 %       |
| Samoa        | 78.2 %                | 30.8 %             | 30.3 %               | 11.8 %       | 0.5 %         | 0.0 %       |
| Wales        | 51.7 %                | 23.9 %             | 23.7 %               | 9.1 %        | 0.2 %         | 0.0 %       |
| Argentina    | 28.2 %                | 8.4 %              | 8.4 %                | 3.3 %        | 0.0 %         | 0.0 %       |
| Georgia      | 6.4 %                 | 1.7 %              | 1.7 %                | 0.4 %        | 0.0 %         | 0.0 %       |
| Italy        | 9.4 %                 | 0.0 %              | 0.0 %                | 0.0 %        | 0.0 %         | 0.0 %       |
| Japan        | 0.1 %                 | 0.0 %              | 0.0 %                | 0.0 %        | 0.0 %         | 0.0 %       |
| Portugal     | 0.1 %                 | 0.0 %              | 0.0 %                | 0.0 %        | 0.0 %         | 0.0 %       |
| Tonga        | 0.1 %                 | 0.0 %              | 0.0 %                | 0.0 %        | 0.0 %         | 0.0 %       |

And more interestingly, here's the change (in percentage points) to the predictions since the tournament started.

|             |   ReachQuarterfinals |   ReachSemifinals |   ReachFinal |   WinFinal |   ReachBronzeFinal |   WinBronze |
|:------------|---------------------:|------------------:|-------------:|-----------:|-------------------:|------------:|
| South Africa|                 +9.5 |             +11   |        +13.3 |       +9.8 |               -2.3 |        -2.2 |
| Ireland     |                 +7.6 |              +9.4 |        +12.6 |       +3.9 |               -3.3 |        -3.2 |
| France      |                 +2.3 |             +10.3 |        +13.6 |       +3.7 |               -3.3 |        -3   |
| England     |                +66.1 |             +37.1 |         +0.5 |       +0   |              +36.6 |       +17.1 |
| Wales       |                +40.4 |             +20.3 |         +0.2 |       +0   |              +20.1 |        +8.5 |
| Australia   |                +17.9 |             +19.7 |         +0.2 |       +0   |              +19.6 |       +20.3 |
| Italy       |                 +1.6 |              -0.1 |         +0   |       +0   |               -0.1 |        +0   |
| Japan       |                 -1.7 |              -0.1 |         +0   |       +0   |               -0.1 |        +0   |
| Portugal    |                 -2.8 |              -0.4 |         +0   |       +0   |               -0.4 |        +0   |
| Georgia     |                -27.8 |             -10.2 |         -0.2 |       +0   |              -10   |        -1.6 |
| Argentina   |                -61.8 |             -31.2 |         -1.3 |       +0   |              -29.8 |        -9.7 |
| Samoa       |                 -2.7 |               1.2 |         -0.7 |       -0.1 |                1.9 |         3.9 |
| Scotland    |                -17.2 |              -4.6 |         -3.4 |       -0.7 |               -1.2 |        -0.8 |
| Fiji        |                -27.8 |             -36.6 |        -11.3 |       -2.8 |              -25.3 |       -27.1 |
| New Zealand |                 -3.9 |             -26   |        -23.5 |      -13.8 |               -2.4 |        -2.1 |


South Africa has benefitted most - they've beaten Scotland, and while New Zealand's loss to France makes their win in Twickenham less impressive, they still benefit when another team looks like less of a contender than was once assumed. Ireland and France also saw their winning chances increase but still have plenty to prove before the final, while Australia, Wales, and England have started to make a case for themselves and seem poised to escape the pools. Georgia and Argentina suffer most from these teams' wins so far

Fiji and New Zealand are the worst off. We had them likely to succeed this year, but just one loss can make the path much more difficult. Fiji's loss to Wales greatly decreases the chance to get out of the pool as it may go to tiebreakers. Which we didn't think were enough of a priority to include properly in these projections, so pool C remains tricky. But we still have Fiji as nearly favorites for the bronze, just behind Australia who have a better chance to advance as they haven't yet played Wales, and could win. New Zealand should still get out of the pool, but may struggle more than we thought they would in the Quarterfinal against what will likely be either South Africa or Ireland. And Scotland's loss to South Africa has unfortunately likely relegated them to third in the pool unless they can pull off a great upset against Ireland