from flask import Flask, request, render_template, send_from_directory, json, redirect
import os
from pathlib import Path
from functions import read_json, count_comments, add_comment, looking_by_word, looking_by_username, making_tags, posts_include_tags, looking_by_teg, add_bookmark, remove_bookmark

app = Flask("Course work 2")

data_bookmarks = "data/bookmarks.json"
data_comments = "data/comments.json"
data = "data/data.json"

@app.route("/")
def main_page():
    return render_template("index.html", data=posts_include_tags(data), comments_cnt=count_comments(data, data_comments), num=len(read_json(data_bookmarks)))


@app.route("/posts/<int:post_id>")
def post_page(post_id):
    if post_id:
        for post in posts_include_tags(data):
            if post["pk"] == post_id:
                comments_by_post = [comment for comment in read_json(data_comments) if post_id == comment["post_id"]]
                return render_template("post.html", post=post, comments_cnt=count_comments(data, data_comments), comments=comments_by_post)
    else:
        return "", 400


@app.route("/posts/<int:post_num>", methods=["POST"])
def new_comment(post_num):
    if post_num:
        if request.method == "POST":
            text = request.form.get("new_comment")
            user = request.form.get("username")
            if text and user:
                add_comment(data_comments, post_num, user, text)
    return redirect(f"/posts/{post_num}", code = 302)


@app.route("/search/", methods=["GET"])
def search_page():
    s = request.args.get("words")
    if s:
        return render_template("search.html", data=looking_by_word(data, s)[0:10], search_count=len(looking_by_word(data, s)), comments_cnt=count_comments(data, data_comments))
    return render_template("search.html")


@app.route("/users/<username>")
def user_page(username):
    if username:
        return render_template("user-feed.html", data=looking_by_username(data, username), search_count=len(looking_by_username(data, username)), comments_cnt=count_comments(data, data_comments), username=username)
    else:
        return "", 400


@app.route("/tag/<tag>")
def tags_page(tag):
    if tag:
        return render_template("tag.html", data=looking_by_teg(data, tag), tag=tag, comments_cnt=count_comments(data, data_comments))


@app.route("/bookmarks/add/<int:post_id>")
def add_to_bookmarks(post_id):
    if post_id:
        add_bookmark(data, data_bookmarks, post_id)
    return redirect("/", code = 302)


@app.route("/bookmarks/remove/<int:post_id>")
def remove_from_bookmarks(post_id):
    if post_id:
        remove_bookmark(data_bookmarks, post_id)
    return redirect("/bookmarks", code = 302)


@app.route("/bookmarks")
def bookmarks_page():
    return render_template("bookmarks.html", data=posts_include_tags(data_bookmarks), comments_cnt=count_comments(data_bookmarks, data_comments))


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run(debug=True)