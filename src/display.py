import questionary as qu
from rich.panel import Panel
from rich.console import Console
from rich.syntax import Syntax
from nba_api.stats.static import players
from src import nbaAPI as na
from src import interface as it
from src import utils

console = Console()

def handle_career_stats():
    player_name = qu.text("Enter player name: ").ask()
    utils.time_function()
    playerID = it.get_player_id(player_name)

    if playerID is None:
        console.print("[red] Player not found.[/red]")
        return
    stats = na.get_player_career_stats(playerID)
    print(stats)

def calculate_per_game(stats):
    gp = stats['GP'].values[0]

    per_game = {
        'GP': gp,
        'MPG': round(stats['MIN'].values[0] / gp, 1),
        'PPG': round(stats['PTS'].values[0] / gp, 1),
        'RPG': round(stats['REB'].values[0] / gp, 1),
        'APG': round(stats['AST'].values[0] / gp, 1),
        'SPG': round(stats['STL'].values[0] / gp, 1),
        'BPG': round(stats['BLK'].values[0] / gp, 1),
        'FG%': round(stats['FG_PCT'].values[0] * 100, 1),
        '3P%': round(stats['FG3_PCT'].values[0] * 100, 1),
        'FT%': round(stats['FT_PCT'].values[0] * 100, 1)
    }
    return per_game

def handle_season_stats():
    player_name = qu.text("Enter player name: ").ask()
    season = qu.text("Enter season (e.g., 2019-20): ").ask()
    playerID = it.get_player_id(player_name)

    if playerID is None:
        console.print("[red] Player not found.[/red]")
        return
    stats = na.get_player_season_stats(playerID, season)

    console.print(Panel(f"{player_name} - {season} PER GAME STATS", style="white"))
    for stat, value in calculate_per_game(stats).items():
        console.print(f"{stat}: {value}")

def handle_compare_players():
    player1_name = qu.text("Enter first player:").ask()
    player1_season = qu.text("Enter season (e.g., 2019-20): ").ask()
    
    player1_ID = it.get_player_id(player1_name)
    if player1_ID is None:
        console.print("[red] Player not found.[/red]")
        return

    player2_name = qu.text("Enter second player:").ask()
    player2_season = qu.text("Enter season (e.g., 2019-20): ").ask()
    
    player2_ID = it.get_player_id(player2_name)
    if player2_ID is None:
        console.print("[red] Player not found.[/red]")
        return
    
    stats1 = na.get_player_season_stats(player1_ID, player1_season)
    stats2 = na.get_player_season_stats(player2_ID, player2_season)
    if stats2.empty:
        console.print(f"[red]No stats found for {player2_name} in {player2_season}[/red]")
        return

    pg1 = calculate_per_game(stats1)
    pg2 = calculate_per_game(stats2)
    
    console.print(Panel(f"{player1_name} {player1_season} vs {player2_name} {player2_season}", style="cyan"))
    for stat in pg1.keys():
        val1 = pg1[stat]
        val2 = pg2[stat]
        
        if stat == 'GP':  # Don't color games played
            console.print(f"{stat}: {val1} vs {val2}")
        elif val1 > val2:
            console.print(f"{stat}: [green]{val1}[/green] vs {val2}")
        elif val2 > val1:
            console.print(f"{stat}: {val1} vs [green]{val2}[/green]")
        else:
            console.print(f"{stat}: {val1} vs {val2}")

