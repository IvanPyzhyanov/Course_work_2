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



# data = read_json("data\data.json")
# comments = read_json("data\comments.json")
# count_posts = 0
# count_com = []
# for a in data:
#     count = 0
#     for b in comments:
#         if b["post_id"] == a["pk"]:
#             count += 1
#     count_posts += 1
#     count_com.append({"post_id": count_posts, "comments_count": count})




