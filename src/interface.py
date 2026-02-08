import questionary as qu
from rich.panel import Panel
from rich.console import Console
from nba_api.stats.static import players
from src import nbaAPI as na

def get_player_id(player_name):
    player_list = players.find_players_by_full_name(player_name)
    if player_list:
        return player_list[0]['id']
    else:
        None


def CLI():
    while True:
        action = qu.select(
            "\n-- NBA STATS DATABASE --",
            choices=[
                "Career Player Stats",
                "Exit"
            ]
        ).ask()

        if action == "Exit":
            print("DATABASE EXITING...")
            break
        elif action == "Career Player Stats":
            player_name = qu.text("Enter player name: ").ask()
            print("SEARCHING...")
            playerID = get_player_id(player_name)
            print("FETCHING...")
            stats = (na.get_player_career_stats(playerID))
            print(stats)