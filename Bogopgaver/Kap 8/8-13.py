"""8-13. User Profile
Copy code from page. 153. Then call it to build a user profile about  yourself."""
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("emil", "bøye", sex="male", age=31)

print(user_profile)