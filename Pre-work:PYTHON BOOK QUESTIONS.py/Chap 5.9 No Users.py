user_names = []

if user_names:
    for user in user_names:
        if user == 'admin':
            print("\nHello "+ user.upper() +", would like to see the status report?")
        else:
            print("\nHello " + user.title() +", thanks for logging in.")
print("We need to find some users!")    