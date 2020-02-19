import feedparser
import notification

feed = feedparser.parse("https://sandrabeijer.elle.se/feed/")

entry = feed.entries[0]

try:
    file = open("sandrabeijer.txt", "r+")
    saved = file.read()
    if saved != entry.published:
        notification.send_notification("Sandra Beijer", entry.title, entry.link)

except FileNotFoundError:
    file = open("sandrabeijer.txt", "w")

file.seek(0)
file.truncate()
file.write(entry.published)
file.close()

"""
kolla om nytt blogginlägg publicerats
hämta datum från rss feed och jämföra med sparat datum. Om dessa inte matchar skicka notis. 
När script är klart, uppdatera lokal fil med senaste inläggets datum
"""
