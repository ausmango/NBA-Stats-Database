import time
import questionary as qu
from rich.panel import Panel
from rich.console import Console
from rich.syntax import Syntax
from rich.progress import track
from nba_api.stats.static import players
from src import nbaAPI as na
from src import interface as it

console = Console()

def handle_career_stats():
    player_name = qu.text("Enter player name: ").ask()
    playerID = it.get_player_id(player_name)

    if playerID is None:
        console.print("[red] Player not found.[/red]")
        return
    stats = na.get_player_career_stats(playerID)
    print(stats)

def handle_season_stats():
    player_name = qu.text("Enter player name: ").ask()
    playerID = it.get_player_id(player_name)

    if playerID is None:
        console.print("[red] Player not found.[/red]")
        return
    stats = na.get_player_season_stats(playerID)

    columns_show = ['GP', 'MIN', 'PTS', 'REB', 'AST',
                     'STL', 'BLK', 'FG_PCT', 'FG3_PCT', 'FT_PCT']
    filter_stats = stats[columns_show]
    print(filter_stats.to_string(index=False))


# def handle_team_metrics(): (WORK IN PROGRESS - ENDPOINT ISSUES)
#     team_name = qu.text("Enter team name: ").ask()
#     teamID = it.get_team_id(team_name)

#     if teamID is None:
#         console.print("[red] Team not found.[/red]")
#         return
#     metrics = na.get_team_metrics(teamID)
#     print(metrics)