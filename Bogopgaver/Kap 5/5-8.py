"""Øvelse med if-statements og lists og for loops"""

users = ["admin", "user1", "user2", "user3", "user5"]

for user in users:
    if user == "admin":
        print("Hello " + user + ", would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")