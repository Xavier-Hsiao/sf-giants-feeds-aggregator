# sf-giants-feeds-aggregator

A CLI tool to read SF Giants rss feeds in terminal

## Issue fixed

Python can't verifiy the SSL certificate because it doesn't have access to the system's CA bundles.

So we have to create a `ssl constext` manually with `certifi` package. Then using `urllib.request` library to fetch the feed manually and then pass the content to `feedparser.parse()`.
