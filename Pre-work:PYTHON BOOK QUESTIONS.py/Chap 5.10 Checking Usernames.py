current_users = ['sonzera', 'tatymfb', 'soneca', 'tha', 'bobmarley']
new_users = ['sonzera', 'tatymfb', 'barao', 'redley', 'midnight']

for user in new_users:
    if user in current_users:
        print("\nHello " + user.upper() + ", you will need to type a new user name.")
    else:
        print("\nHello " +user.title()+ ", this user name is available.")
