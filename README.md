# NBA Stats Database

A simple command-line NBA statistics database built in Python using the nba_api package.
This project allows users to interact with historical NBA player data via a clean, interactive CLI — no web UI required.

## Features

- Career player statistics
- Season-by-season totals
- Player seasonal stats comparisaon

NBA-Stats-Database/
├── src/
│   ├── nbaAPI.py        # NBA API data fetching logic
│   ├── interface.py    # CLI navigation and user input
│   ├── display.py      # Output formatting and stat calculations
│   └── utils.py        # Helper utilities (timing, etc.)
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
└── README.md

## Requirements

- Python 3.7+
- various libraries

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ausmango/NBA-Stats-Database.git
   cd NBA-Stats-Database
2. Install dependencies

      pip install -r requirements.txt
