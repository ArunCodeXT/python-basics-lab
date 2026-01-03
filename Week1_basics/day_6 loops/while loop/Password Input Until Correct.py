password = "python123"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")
    if user_input != password:
        print("❌ Wrong password, try again!")
print("✅ Access granted!")
