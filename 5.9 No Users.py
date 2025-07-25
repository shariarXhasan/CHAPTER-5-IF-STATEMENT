

#Portion NO 1
username = ['jack', 'mack', 'rock', 'jhonny', 'admin']

print('____Gretting____')

for user in username:
    if user=='admin':
        print(f'Hello {user.title()}, would you want see a report?')
    else:
        print(f"Hello {user.title()}, welcome again for login")

else:
    print('We need more users...')

#Portion NO 2

print('\n___Gretting 2____')
username.clear()

for user in username:
    if user=='admin':
        print(f'Hello {user.title()}, would you want see a report?')
    else:
        print(f"Hello {user.title()}, welcome again for login")
else:
    print("We need more users..")