available_toopings = ['mashroom', 'mutton', 'ghee', 'beef', 'chocolate']

requested_toopings = ['mashroom', 'green chilli',  'beef']

for requested_toopings in requested_toopings:
    if requested_toopings in available_toopings:
        print(f"Adding {requested_toopings}")
    else:
        print(f'Sorry we are out of {requested_toopings}')

print('\n Your pizza is ready')