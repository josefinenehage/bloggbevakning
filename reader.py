import argparse
import feedparser
import notification
parser = argparse.ArgumentParser(description='Send in URLS you want notification from')
parser.add_argument('urls', nargs='+')
args = parser.parse_args()

# https://techcrunch.com/feed/
# https://geekwire.com/feed/

for url in args.urls:
    file_name = url
    if file_name.startswith("https://"):
        file_name = file_name.replace("https://", "")
    elif file_name.startswith("http://"):
        file_name = file_name.replace("http://", "")
    else:
        print("not valid URL")

    feed = feedparser.parse(url)
    try:
        entry = feed.entries[0]
    except IndexError:
        print("URL is not working")

    first_dot = file_name.find(".")
    file_name = file_name[:first_dot]

    try:
        file = open(f'{file_name}.txt', 'r+')
        saved = file.read()
        if saved != entry.published:
            notification.send_notification(file_name, f"Nytt inlägg: {entry.title}", entry.link)
    except FileNotFoundError:
        file = open(f'{file_name}.txt', 'w')

    file.seek(0)
    file.truncate()
    file.write(entry.published)
    file.close()