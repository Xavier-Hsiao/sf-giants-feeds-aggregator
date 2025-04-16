import feedparser
import certifi
import ssl
import urllib.request

from teams import select_teams

def main():
      teams = select_teams()

      # create ssl contect with certifi
      ssl_context = ssl.create_default_context(cafile=certifi.where())

      # open the url in ssl context
      for team in teams:
            print(f"\n====== News for {team["name"]} ======\n")     
            with urllib.request.urlopen(team["url"], context=ssl_context) as response:
                  data = response.read()
      
            d = feedparser.parse(data)

            if d.bozo:
                  print("Error parsing feed:", d.bozo_exception)
                  continue # skip to next team if there's an error
      
            for feed in d.entries:
                  print("Title:", feed.title)
                  print("Link:", feed.link)
                  print("Summary:", feed.title_detail.value)
                  print("Publised At:", feed.published)
                  print("-" * 40)

main()

