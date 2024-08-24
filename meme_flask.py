#!/bin/python3

from flask import Flask, render_template
import requests
import json
"""
render_template allows us to reference and
use an external HTML code
"""

app = Flask(__name__)

def get_meme():
    """
    Uncomment these two lines and comment out the other
    url if you want to use a separate sr
    """
    url = "https://meme-api.com/gimme/Catmemes"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    # we'll pass two variables meme_pic and subreddit into meme_index.html
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

app.run(host="0.0.0.0", port=80)
