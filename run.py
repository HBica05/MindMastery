inputted = input('type your name please:\n ').strip()

while inputted == '':
    inputted = input(
        'You didnt type anything! Please input your name please:\n ').strip(
        ).lower()
print(f'Welcome to the Mind Master game {inputted} !')

print(
    """
Topics:
1. General Knowledge
2. Science
3. Sports
4. Geography
5. Mathematics
    """
)

option_inputted = input('Select option 1 to 5:\n ').strip().lower()
available_options = ["1", "2", "3", "4", "5"]
