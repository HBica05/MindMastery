inputted = input('type your name please: ').strip().lower()

while inputted == '':
    inputted = input(
        'You didnt type anything! Please input your name please: ').strip(
        ).lower()
print(f'Welcome to the Mind Master game {inputted} !')

