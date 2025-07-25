# 5-10. Checking Usernames

# 1. Make a list of five or more usernames called current_users.
current_users = ['alisa', 'bob', 'charlie', 'diana', 'admin', 'eve']

# 2. Make another list of five usernames called new_users.
#    One or two of these should also be in the current_users list.
#    Note: 'alisa' is in different cases to test case-insensitivity.
new_users = ['frank', 'ALISA', 'grace', 'BOB', 'heidi']

print("--- Checking New Usernames ---")

# To ensure case-insensitive comparison, create a lowercase version of current_users.
# We'll convert every username in current_users to lowercase and store it in a new list.
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

# Now, loop through the new_users list to check each proposed username.
for new_user_candidate in new_users:
    # Convert the new username to lowercase for comparison.
    # This way, 'ALISA' will be compared to 'alisa' (both lowercase).
    if new_user_candidate.lower() in current_users_lower:
        # If the lowercase version of the new username is found in our lowercase existing users list.
        print(f"Sorry, '{new_user_candidate}' is already taken. Please enter a new username.")
    else:
        # If the lowercase version of the new username is not found.
        print(f"'{new_user_candidate}' is available!")