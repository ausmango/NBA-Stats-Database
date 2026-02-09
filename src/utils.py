import time
from rich.progress import track
from rich.console import Console

console = Console()

def time_function():
    for i in track(range(10), description="FETCHING..."):
        time.sleep(0.05)
