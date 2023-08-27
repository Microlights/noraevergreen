# 冗长的代码重复
print("Welcome to the program!")
print("Please enter your username:")
username = input()
print("Please enter your password:")
password = input()
print("Please confirm your password:")
confirm_password = input()
print("Please enter your email address:")
email = input()
print("Creating user profile...")
# 以下是更多的重复代码...

# 优化后的代码使用函数
def get_input(prompt):
    print(prompt)
    return input()

def create_user_profile():
    username = get_input("Please enter your username:")
    password = get_input("Please enter your password:")
    confirm_password = get_input("Please confirm your password:")
    email = get_input("Please enter your email address:")
    print("Creating user profile...")
    # 以下是更多的代码...

# 调用函数
print("Welcome to the program!")
create_user_profile()
