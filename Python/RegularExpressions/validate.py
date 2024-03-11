email = input("Enter E-mail : ").strip()
user_name, domain = email.split("@")
if user_name and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")