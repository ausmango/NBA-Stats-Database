import pandas as pd
import requests
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
from src import interface as IT

headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

def get_player_info(playerID):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id = playerID, headers=headers, timeout=100)
    dataFrame = player_info.common_player_info.get_data_frame()
    return dataFrame

def get_player_career_stats(playerID):
    career = playercareerstats.PlayerCareerStats(player_id=playerID)
    dataFrame =career.get_data_frames()[0]
    return dataFrame
