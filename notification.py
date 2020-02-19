import http.client, urllib


def send_notification(title, message, url):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": REDACTED,
                     "user": REDACTED,
                     "message": message,
                     "device": "josefin",
                     "title": title,
                     "url": url
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()
