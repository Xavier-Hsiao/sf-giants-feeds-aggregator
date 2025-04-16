import feedparser
import certifi
import ssl
import urllib.request

def main():
      url = "https://www.mlb.com/giants/feeds/news/rss.xml"
      # create ssl contect with certifi
      ssl_context = ssl.create_default_context(cafile=certifi.where())

      # open the url in ssl context
      with urllib.request.urlopen(url, context=ssl_context) as response:
            data = response.read()
      
      d = feedparser.parse(data)

      if d.bozo:
            print("Error parsing feed:", d.bozo_exception)
      
      for feed in d.entries:
            print("Title:", feed.title)
            print("Link:", feed.link)
            print("Summary:", feed.title_detail.value)
            print("Publised At:", feed.published)
            print("-" * 40)

main()

