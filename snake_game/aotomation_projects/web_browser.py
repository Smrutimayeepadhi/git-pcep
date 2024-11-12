import sys
import webbrowser

urls = {
    "work": ["www.slack.com", "www.google.com"],
    "personal": ["https://www.netflix.com", "https://www.spotify.com" , "https://www.youtube.com"],
}

def open_webpages(urls):
    for url in urls:
        webbrowser.open(url)
open_webpages(urls["personal"][1])
