password = input("Enter a password: ")

length = len(password) >= 8
upper = any(c.isupper() for c in password)
number = any(c.isdigit() for c in password)
special = any(c in "!@#$%^&*" for c in password)

score = 0
if length:
    score = score + 1
if upper:
    score = score + 1
if number:
    score = score + 1
if special:
    score = score + 1

if score == 4:
    print("Strong password!")
elif score == 3:
    print("Medium password.")
else:
    print("Weak password!")

if not length:
    print("- Make it at least 8 characters")
if not upper:
    print("- Add uppercase letters")
if not number:
    print("- Add numbers")
if not special:
    print("- Add special characters like !@#$")