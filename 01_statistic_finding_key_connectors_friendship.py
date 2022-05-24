from __future__ import division
from collections import Counter

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# add fiends list to each user
for user in users:
    user["friends"] = []

# fill fiends list
for i, j in friendships:
    # this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j])    # add i as a friend of j
    users[j]["friends"].append(users[i])    # add j as a friend of i


def number_of_friends(user):
    """how many friends does_user_have?"""
    return len(user["friends"])     # lenght of friends_ids list

# get total connections
total_connections = sum(number_of_friends(user) for user in users)      # 24

num_users = len(users)      # length of the users list
avg_connections = total_connections/num_users   # 2.4

# create a list (user_ id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

sorted(num_friends_by_id,   # get it sorted
       key=lambda x: x[1],  # by num_friends
       reverse=True)        # largest to smallest


print([friend["id"] for friend in users[0]["friends"]])     # [1, 2]
print([friend["id"] for friend in users[1]["friends"]])     # [0, 2, 3]
print([friend["id"] for friend in users[2]["friends"]])     # [0, 1, 3]


def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, he's not_the_same as all the people in user["friends']"""
    return all(not_the_same(friend, other_user) for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]    # for each of my friends
                   for foaf in friend["friends"]    # count *their* friends
                   if not_the_same(user, foaf)      # who aren't me
                   and not_friends(user, foaf))     # and aren't my friends

print(friends_of_friend_ids(users[3]))              # Counter({0: 2, 5: 1})