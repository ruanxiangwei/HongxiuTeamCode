import json

# def greet_user():
#     filename = 'username.txt'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("what is your name?")
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"我们会记得你回来的{username}")
#     else:
#         print("欢迎回来" + username)
#
# greet_user()

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_username()
    if username:
        print(f"欢迎回来{username}")
    else:
        username = get_new_username()
        print("我会记得你回来的" + username)

def get_new_username():
    username = input("你叫什么名字?")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)

greet_user()