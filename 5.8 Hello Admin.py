username = ['jack', 'mack', 'rock', 'jhonny', 'admin']



print('____Gretting____')



for user in username:

    if user=='admin':

      print(f'Hello {user.title()}, would you want see a report?')

    else:


     print(f"Hello {user.title()}, welcome again for login")