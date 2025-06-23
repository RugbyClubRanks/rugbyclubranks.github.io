---  
layout: page  
title: Maro Itoje
date: 2022-09-14 03:05:00 18:00:00 -0500  
categories: England Saracens
---
# Maro Itoje
Lock, Flanker
Current elo: 113.18 
Current Percentile: 88.0

## Elo history plot

What things should be on a player's page?
Matches by club
    Win Rate by club
Matches by Opponent

Average Stats per Match, if available
    Stats per minute?

Impact to Team
    Average elo contribution, compared to 1/15.
        Higher == better than the team, on average, while lower means worse
    Team success with v. without
        elo of replacement?
        elo v league average?
        elo v team average?


```{Python}
player_df = player_elo[player_elo.Full_Name == 'Maro Itoje'].copy()
player_df['opponent'] = np.where(player_df.Team == player_df['Home Team'], player_df['Away Team'], player_df['Home Team'])
player_df['win'] = np.where(
    (player_df['Home Score'] > player_df['Away Score']) & (player_df.Team == player_df['Home Team']) | 
    (player_df['Home Score'] < player_df['Away Score']) & (player_df.Team == player_df['Away Team']), 1, 0)
player_df.loc[player_df['Home Score'] == player_df['Away Score'], 'win'] = 0.5
player_history_plot(player_df)


name = player_df.Full_Name.iloc[0]
current_elo = player_df.end_elo.iloc[-1]
current_percentile = player_df.merge(make_current_percentile(starters, player_df.Date.iloc[-1])).percentile[0]
positions = player_df[player_df.Position != 'R'].Position.value_counts(normalize=True).loc[lambda x : x > 0.1].keys().tolist()[0:2]
print(name, positions, np.round(current_elo, 2), current_percentile)

player_history_plot(player_df, percentile_df)
```