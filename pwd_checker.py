def check_pass(pass1):
    l1 = ["!", "@", "#", "$", "%", "^"]
    l2 = ["@", "."]
    if len(pass1) < 10 or len(pass1) > 15:
        return "Password length should be between 10 and 15"
    elif not any(i.isupper() for i in pass1):
        return "Password should contain at least one uppercase letter"
    elif not any(i.islower() for i in pass1):
        return "Password should contain at least one lowercase letter"
    elif not any(i.isdigit() for i in pass1):
        return "Password should contain at least one digit"
    elif not any(i in l1 for i in pass1):
        return "Password should contain at least one special character"
    elif any(i == pass1[len(pass1)-1] for i in l2):
        return "Password should not end with . or @"
    elif any(i == " " for i in pass1):
        return "Password should not contain whitespaces"
    else:
        return "Good password"


pwd = input("Enter your password:")
print(check_pass(pwd))
