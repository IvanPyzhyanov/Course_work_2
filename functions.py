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


def looking_by_word(data_file, s_words):
    '''making function which looking for post which include searching`s words'''
    post_by_word = [post for post in posts_include_tags(data_file) if s_words.lower() in post["content"].lower()]
    return post_by_word


def looking_by_username(data_file, username):
    '''making function which looking for post by username'''
    post_by_username = [post for post in posts_include_tags(data_file) if username in post["poster_name"]]
    return post_by_username


def making_tags(content):
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
    posts = read_json(data_file)
    for i, post in enumerate(posts):
        post["content"] = making_tags(post["content"])
    return posts


def looking_by_teg(data_file, tag):
    post_by_tag = [post for post in posts_include_tags(data_file) if tag in post["content"]]
    return post_by_tag

# data = "data/data.json"
# posts = read_json(data)
# for i, post in enumerate(posts):
#     print(i)
#     print(post)
#     post["content"] = making_tags(post["content"])
# print(posts)

# print(include_tags())






