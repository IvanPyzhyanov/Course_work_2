from flask import Flask, request, render_template, send_from_directory, json
import os
from pathlib import Path
from functions import read_json, count_comments

app = Flask("Course work 2")

data_bookmarks = "data/bookmarks.json"
data_comments = "data/comments.json"
data = "data/data.json"

@app.route("/")
def main_page():
    return render_template("index.html", data=read_json(data), comments=count_comments(data, data_comments))


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run(debug=True)