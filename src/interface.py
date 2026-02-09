import time
import questionary as qu
from rich.panel import Panel
from rich.console import Console
from rich.syntax import Syntax
from rich.progress import track
from nba_api.stats.static import players
from nba_api.stats.static import teams
from src import nbaAPI as na
from src import display

console = Console()

def get_player_id(player_name):
    player_list = players.find_players_by_full_name(player_name)
    if player_list:
        return player_list[0]['id']
    else:
        None

# def get_team_id(team_name): (WORK IN PROGRESS - ENDPOINT ISSUES)
#     team_list = teams.find_teams_by_full_name(team_name)
#     if team_list:
#         return team_list[0]['id']
#     else: 
#         return None



def CLI():
    while True:
        action = qu.select(
            "\n-- NBA STATS DATABASE --",
            choices=[
                "Career Player Stats",
                "Season Player Stats",
                "Compare Player Season Stats",
                "Exit"
            ]
        ).ask()
        if action == "Exit":
            print("DATABASE EXITING...")
            break
        elif action == "Career Player Stats":
            display.handle_career_stats()
        elif action == "Season Player Stats":
            display.handle_season_stats()
        elif action == "Compare Player Season Stats":
            display.handle_compare_players()
