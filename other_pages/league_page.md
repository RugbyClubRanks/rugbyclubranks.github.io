## League page

Comparison of all teams, record, table
    include elo - average given all observed lineups, and most recent + next match, if announced
    Link to all recent + projected matches

League compared to other leagues?
    average team, position, player elos


```{Python}
import sys
import yaml
with open('secrets.yml', 'r') as file:
    secrets = yaml.safe_load(file)
sys.path.append(secrets['elo_proj_path'])

from player_club_classes import team_elo, Player, Club, Match
import pandas as pd
import numpy as np
import pickle

from support_files.team_colors import team_color_dict
team_colors = pd.DataFrame(team_color_dict).T
team_colors.columns = ['Primary', 'Secondary']
team_colors = team_colors.rename_axis('Team').reset_index()

with open('../Rugby_ELO/processed_data/playerbase.pickle', 'rb') as handle:
    playerbase = pickle.load(handle)
with open('../Rugby_ELO/processed_data/matchlist.pickle', 'rb') as handle:
    matchlist = pickle.load(handle)
with open('../Rugby_ELO/processed_data/teamlist.pickle', 'rb') as handle:
    teamlist = pickle.load(handle)

## LOAD DATA
match_list = []
for _, match in matchlist.items():
    match_list.append({key:val for key, val in vars(match).items()})

player_elo_list = []
for player_name, player in playerbase.items():
    player_elo = pd.DataFrame(player.elo_list, columns = [
        'Number', 'Full_Name', 'Team', 'Player', 'Position', 'Tries',
        'Try Assists', 'Conversion Goals', 'Penalty Goals',
        'Drop Goals Converted', 'Points', 'Passes', 'Runs', 'Meters Run',
        'Clean Breaks', 'Defenders Beaten', 'Offload', 'Turnovers Conceded',
        'Tackles', 'Missed Tackles', 'Lineouts Won', 'Penalties Conceded',
        'Yellow Cards', 'Red Cards', 'espn_id_num', 'Competition', 'Date',
        'Home Team', 'Home Score', 'Away Team', 'Away Score', 'Minutes',
        'Position_Number', 'gameid', 'Unicode_ID', 'comp_level', 'start_elo', 'end_elo'
       ])
    player_elo['Full Name'] = player_name[0]
    player_elo['Unicode_ID'] = player_name[1]
    player_elo_list.append(player_elo)

player_elo = pd.concat(player_elo_list).reset_index(drop=True)
player_elo = pd.merge(player_elo, team_colors, on = 'Team', how = 'left')
player_elo['elo_change'] = player_elo.end_elo - player_elo.start_elo
player_elo.Date = pd.to_datetime(player_elo.Date)

comp = "Gallagher Premiership 2022"
comp_matches = [match for match in match_list if match["competition"] == comp]
comp_matches = pd.DataFrame(comp_matches)

league_teams = pd.unique(comp_matches[['home_team_name', 'away_team_name']].values.ravel('K'))
club_histories = [pd.DataFrame([x for x in teamlist[team].history if x['Competition'] == comp]) for team in league_teams]

fig, ax = plt.subplots()
labels = []
for team_name, history in zip(league_teams, club_histories):
    ax.plot(
        history.Date, 
        history.elo,  
        color = team_color_dict[team_name][0],
        lw=2,
        path_effects=[pe.Stroke(linewidth=3, foreground=team_color_dict[team_name][1]), pe.Normal()]
    )

    point = mlines.Line2D([0], [0], marker='o', color=team_color_dict[team_name][1], label=team_name,
                      markerfacecolor=team_color_dict[team_name][0], markersize=10, ls = '')
    labels.append(point)
plt.legend(handles=labels)
```