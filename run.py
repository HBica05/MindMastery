inputted = input('type your name please: ').strip().lower()

while inputted == '':
    inputted = input(
        'You didnt type anything! Please input your name please: ').strip(
        ).lower()
print(f'Welcome to the Mind Master game {inputted} !')

print(
    """
Please enter your preferred Topic:
1. General Knowledge
2. Science
3. Sports
4. Geography
5. Mathematics
    """
)