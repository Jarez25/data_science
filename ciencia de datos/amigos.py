# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:34:53 2024

@author: jarez
"""

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
    {"id": 9, "name": "Klein"},
]

friendship_pairs = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

friendship = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendship[i].append(j)
    friendship[j].append(i)

def number_of_friends(user):
    user_id = user["id"]
    friend_ids = friendship[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)
numb_user = len(users)
avg_connection = total_connections / numb_user

num_friends_by_id = [
    (user["id"], number_of_friends(user))
    for user in users
]
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse=True
)

def foaf_ids_bad(user):
    return [
        foaf_id
        for friend_id in friendship[user["id"]]
        for foaf_id in friendship[friend_id]
    ]

print(friendship[0])  
print(friendship[1])  
print(friendship[9])  


def friend_of_friends(user):
    user_id = user['id']
    return Counter(
        foaf_id
        for friend_id in friendship[user_id]
        for foaf_id in friendship[friend_id]
        if foaf_id != user_id
        and foaf_id not in
        friendship[user_id]
        )

print(friend_of_friends(users[3]))  

