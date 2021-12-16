import json

def read_json(data_file):
    '''making function which get data from json data file with posts'''
    with open(data_file, "r", encoding="UTF-8") as file:
        return json.load(file)


def count_comments(data_file, comments_file):
    '''making function which count comments by each post'''
    data = read_json(data_file)
    comments = read_json(comments_file)
    count_posts = 0
    count_com = []
    for a in data:
        count = 0
        for b in comments:
            if b["post_id"] == a["pk"]:
                count += 1
        count_posts += 1
        count_com.append({"post_id": count_posts, "comments_count": count})
    return count_com


def add_comment(comments_file, post_num, name, new_comment):
    '''making function which add new comment to post'''
    with open(comments_file, "r", encoding="UTF-8") as file:
        comments = json.load(file)
    with open(comments_file, "w", encoding="UTF-8") as file:
        comments.append({"post_id": post_num, "commenter_name": name, "comment": new_comment, "pk": (len(comments)+1)})
        json.dump(comments, file, ensure_ascii=False, indent=4)
    return "comment added"


def looking_by_word(data_file, s_words):
    '''making function which looking for post which include searching`s words'''
    post_by_word = [post for post in posts_include_tags(data_file) if s_words.lower() in post["content"].lower()]
    return post_by_word


def looking_by_username(data_file, username):
    '''making function which looking for post by username'''
    post_by_username = [post for post in posts_include_tags(data_file) if username in post["poster_name"]]
    return post_by_username


def making_tags(content):
    '''making function which find words started on symbol "#" and change their to link'''
    words = content.split(" ")
    for i, word in enumerate(words):
        if word.startswith("#"):
            tag = word.replace("#", "")
            tag = tag.replace("!", "")
            tag = tag.replace(",", "")
            tag = tag.replace(".", "")
            link = f"<a href='tag/{tag}'>{word}</a>"
            words[i] = link
    return " ".join(words)


def posts_include_tags(data_file):
    '''making function which change content on content which includes links to tags'''
    posts = read_json(data_file)
    for i, post in enumerate(posts):
        post["content"] = making_tags(post["content"])
    return posts


def looking_by_teg(data_file, tag):
    '''making function which looking for post by tag'''
    post_by_tag = [post for post in posts_include_tags(data_file) if tag in post["content"]]
    return post_by_tag


def add_bookmark(data_file, book_file, post_num):
    '''making function which add post to bookmarks page'''
    for post in read_json(data_file):
        if post_num == post["pk"]:
            with open(book_file, "r", encoding="UTF-8") as file:
                bookmarks = json.load(file)
            for book in bookmarks:
                if book["pk"]==post_num:
                    return "already added"
            with open(book_file, "w", encoding="UTF-8") as file:
                bookmarks.append(post)
                json.dump(bookmarks, file, ensure_ascii=False, indent=4)
    return "added"


def remove_bookmark(book_file, post_num):
    '''making function which remove post from bookmarks page'''
    for post in read_json(book_file):
        if post_num == post["pk"]:
            with open(book_file, "r", encoding="UTF-8") as file:
                bookmarks = json.load(file)
            with open(book_file, "w", encoding="UTF-8") as file:
                bookmarks.remove(post)
                json.dump(bookmarks, file, ensure_ascii=False, indent=4)
    return "removed"




