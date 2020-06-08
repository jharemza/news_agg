import feedparser
from flask import Flask, render_template
app = Flask(__name__)
FEED_URL="https://news.google.com/rss/search?q=market%20risk&hl=en-US&gl=US&ceid=US:en"
@app.route("/")
def print_news():
    feed = feedparser.parse(FEED_URL)
    return render_template("news.html", articles = feed['entries']) 

if __name__=="__main__":
    app.run(debug = True)