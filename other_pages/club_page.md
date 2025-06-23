## Club page
Historical elo, with highs lows and average
Player info - most caps, minutes, NEED POINTS
Record, rivals?


```{Python}
club_name = 'South Africa'
club_match_names = [x['Match_Name'] for x in teamlist[club_name].history]
club_matches = match_df[match_df.name.isin(club_match_names)].copy()

is_home = club_matches.home_team_name == club_name
club_matches['Location'] = np.where(is_home, 'home', 'away')
club_matches['opponent'] = np.where(is_home, club_matches.away_team_name, club_matches.home_team_name)
club_matches['team'] = np.where(is_home, club_matches.home_team, club_matches.away_team)
club_matches['opponent_team'] = np.where(is_home, club_matches.away_team, club_matches.home_team)
club_matches['lineup_elo'] = np.where(is_home, club_matches.lineup_home_elo, club_matches.lineup_away_elo)
club_matches['opponent_lineup_elo'] = np.where(is_home, club_matches.lineup_away_elo, club_matches.lineup_home_elo)
club_matches['elo'] = np.where(is_home, club_matches.home_elo, club_matches.away_elo)
club_matches['opponent_elo'] = np.where(is_home, club_matches.away_elo, club_matches.home_elo)
club_matches['score'] = np.where(is_home, club_matches.home_score, club_matches.away_score)
club_matches['opponent_score'] = np.where(is_home, club_matches.away_score, club_matches.home_score)

for col in ['lineup_elo_diff', 'lineup_spread', 'lineup_prediction', 'elo_diff',
       'spread', 'point_diff', 'spread_weighted_diff', 'mov_mod',
       'elo_change']:
    club_matches[col] = np.where(is_home, club_matches[col], club_matches[col] * -1)

club_matches['prediction'] = np.where(is_home, club_matches['prediction'], 1 - club_matches['prediction'])
club_matches = club_matches[[x for x in club_matches.columns if "GLOBAL" not in x and "home" not in x and "away" not in x]]

# rough elo history
plt.plot(
        club_matches.date, 
        club_matches.elo,  
        color = team_color_dict[club_name][0],
        lw=2,
        path_effects=[pe.Stroke(linewidth=3, foreground=team_color_dict[club_name][1]), pe.Normal()]
    )

# Recent elo mean
club_matches.tail().elo.mean()

# Player appearances
player_names = []
player_minutes = []

for lineup in club_matches.team:
    for player in lineup:
        player_names.append(player[1])
        player_minutes.append(player[-6])

player_df = pd.DataFrame({'Player': player_names, 'Minutes': player_minutes})
player_appearances = player_df.groupby('Player').Minutes.agg(['count', 'sum']).reset_index()

```