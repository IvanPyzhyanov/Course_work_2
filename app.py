from flask import Flask, request, render_template, send_from_directory, json
import os
from pathlib import Path
from functions import read_json, count_comments, looking_by_word

app = Flask("Course work 2")

data_bookmarks = "data/bookmarks.json"
data_comments = "data/comments.json"
data = "data/data.json"

@app.route("/")
def main_page():
    posts_num = 0
    for post in read_json(data):
        if posts_num < post["pk"]:
            posts_num = post["pk"]
    return render_template("index.html", data=read_json(data), comments_cnt=count_comments(data, data_comments), num=posts_num)


@app.route("/posts/<int:post_id>")
def post_page(post_id):
    if post_id:
        for post in read_json(data):
            if post["pk"] == post_id:
                comments_by_post = [comment for comment in read_json(data_comments) if post_id == comment["post_id"]]
                return render_template("post.html", post=post, comments_cnt=count_comments(data, data_comments), comments=comments_by_post)
            # else:
            #     return "incorrect id", 400
    else:
        return "", 400


@app.route("/search/")
def search_page():
    s = request.args.get("words")
    if s:
        return render_template("search.html", data=looking_by_word(data, s)[0:10], search_count=len(looking_by_word(data, s)), comments_cnt=count_comments(data, data_comments))
    return render_template("search.html")


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run(debug=True)