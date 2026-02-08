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
        print("\nCommand Line Interface\n---------------"
              "\nWelcome to the CLI. Below are some commands you may input." \
              "\n1. Player Common Info" \
              "\n2. Career Player Stats")
        user_input = input("Enter your command here: ")
        if user_input == 1 or user_input == "1":
            player_name = input("Enter the name of the player: ")
            print("Looking up player...")
            playerID = get_player_id(player_name)
            print("Fetching player info...")
            print(na.get_player_career_stats(playerID))
        break
