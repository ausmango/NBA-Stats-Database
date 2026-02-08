import time
import questionary as qu
from rich.panel import Panel
from rich.console import Console
from rich.syntax import Syntax
from rich.progress import track
from nba_api.stats.static import players
from src import nbaAPI as na

console = Console()