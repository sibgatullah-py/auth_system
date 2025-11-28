from services.auth_service import AuthService

auth = AuthService()

print("1. Signup")
print("2. Login")

choice = input("Choose an option: ")

if choice == "1":
    email = input("Enter email: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    success, message = auth.signup(email, username, password)
    print(message)

elif choice == "2":
    email = input("Enter email: ")
    password = input("Enter password: ")

    success, message = auth.login(email, password)
    print(message)

else:
    print("Invalid choice")
