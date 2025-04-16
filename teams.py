TEAMS = {
      "1": {"name": "Arizona Diamondbacks", "url": "https://www.mlb.com/dbacks/feeds/news/rss.xml"},
      "2": {"name": "Atlanta Braves", "url": "https://www.mlb.com/braves/feeds/news/rss.xml"},
      "3": {"name": "Baltimore Orioles", "url": "https://www.mlb.com/orioles/feeds/news/rss.xml"},
      "4": {"name": "Boston Red Sox", "url": "https://www.mlb.com/redsox/feeds/news/rss.xml"},
      "5": {"name": "Chicago White Sox", "url": "https://www.mlb.com/whitesox/feeds/news/rss.xml"},
      "6": {"name": "Chicago Cubs", "url": "https://www.mlb.com/cubs/feeds/news/rss.xml"},
      "7": {"name": "Cincinnati Reds", "url": "https://www.mlb.com/reds/feeds/news/rss.xml"},
      "8": {"name": "Cleveland Guardians", "url": "https://www.mlb.com/guardians/feeds/news/rss.xml"},
      "9": {"name": "Colorado Rockies", "url": "https://www.mlb.com/rockies/feeds/news/rss.xml"},
      "10": {"name": "Detroit Tigers", "url": "https://www.mlb.com/tigers/feeds/news/rss.xml"},
      "11": {"name": "Houston Astros", "url": "https://www.mlb.com/astros/feeds/news/rss.xml"},
      "12": {"name": "Kansas City Royals", "url": "https://www.mlb.com/royals/feeds/news/rss.xml"},
      "13": {"name": "Los Angeles Angels", "url": "https://www.mlb.com/angels/feeds/news/rss.xml"},
      "14": {"name": "Los Angeles Dodgers", "url": "https://www.mlb.com/dodgers/feeds/news/rss.xml"},
      "15": {"name": "Miami Marlins", "url": "https://www.mlb.com/marlins/feeds/news/rss.xml"},
      "16": {"name": "Milwaukee Brewers", "url": "https://www.mlb.com/brewers/feeds/news/rss.xml"},
      "17": {"name": "Minnesota Twins", "url": "https://www.mlb.com/twins/feeds/news/rss.xml"},
      "18": {"name": "New York Yankees", "url": "https://www.mlb.com/yankees/feeds/news/rss.xml"},
      "19": {"name": "New York Mets", "url": "https://www.mlb.com/mets/feeds/news/rss.xml"},
      "20": {"name": "Oakland Athletics", "url": "https://www.mlb.com/athletics/feeds/news/rss.xml"},
      "21": {"name": "Philadelphia Phillies", "url": "https://www.mlb.com/phillies/feeds/news/rss.xml"},
      "22": {"name": "Pittsburgh Pirates", "url": "https://www.mlb.com/pirates/feeds/news/rss.xml"},
      "23": {"name": "San Diego Padres", "url": "https://www.mlb.com/padres/feeds/news/rss.xml"},
      "24": {"name": "San Francisco Giants", "url": "https://www.mlb.com/giants/feeds/news/rss.xml"},
      "25": {"name": "Seattle Mariners", "url": "https://www.mlb.com/mariners/feeds/news/rss.xml"},
      "26": {"name": "St. Louis Cardinals", "url": "https://www.mlb.com/cardinals/feeds/news/rss.xml"},
      "27": {"name": "Tampa Bay Rays", "url": "https://www.mlb.com/rays/feeds/news/rss.xml"},
      "28": {"name": "Texas Rangers", "url": "https://www.mlb.com/rangers/feeds/news/rss.xml"},
      "29": {"name": "Toronto Blue Jays", "url": "https://www.mlb.com/bluejays/feeds/news/rss.xml"},
      "30": {"name": "Washington Nationals", "url": "https://www.mlb.com/nationals/feeds/news/rss.xml"},
}

def select_teams():
      print("Select your favorite teams (use comma to seperate multiple numbers)")
      for number, team in TEAMS.items():
            print(f"{number}: {team["name"]}")
      
      selection = input("> ").split(",")
      selected_teams = []

      for choice_num in selection:
            choice_num = choice_num.strip()
            if choice_num in TEAMS:
                  selected_teams.append(TEAMS[choice_num])
                  
      return selected_teams 