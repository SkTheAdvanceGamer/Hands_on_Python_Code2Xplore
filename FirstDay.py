name = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
age = int(input("Enter your age: "))

valid = True

if name.count(" ") < 1 or name.startswith(" ") or name.endswith(" "):
    valid = False

if email.count(" ") > 0 or email.count("@") != 1 or email.count(".") < 1:
    valid = False

if len(phone) != 10 or not phone.isdigit() or phone.startswith("0"):
    valid = False

if age < 18 or age > 60:
    valid = False

if valid:
    print("User profile is valid.")
else:
    print("User profile is invalid.")
