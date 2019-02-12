"""Øvelse med liste, if-statements, loops og tjek af brugernavne"""

#DET VIRKER SLET IKKE LIGE NU

current_users = ["admin", "user1", "user2", "user3", "User4"]
new_users = ["user5", "user6", "user7", "User3", "user4"]

#denne del gør at current_users sættes som lower case, hvor det efterfølgende check bliver case insensitive
current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower)

print(current_users_lower)


#sammenligning af brugernavne
for user in new_users:
    if user.lower() in current_users_lower:
        print("Username already in use. Pick another.")
    else:
        print("Username available.")