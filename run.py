def get_user_name():
    """Prompt the user to create a name and ensure it is non-empty."""
    # Prompt the user to enter their name, stripping any leading/trailing whitespace
    name = input('Create a name for you:\n').strip()
    
    # Continue prompting until the user provides a non-empty name
    while not name:
        name = input('You did not type anything! Please input a name:\n').strip()
        
    return name

def display_topic_options():
    """Display a list of available quiz topics."""
    # print a list of available quiz topics for the user to choose from
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

# ensures selection of a topic option 
option_inputted = input('Select option 1 to 5:\n ').strip().lower()
available_options = ["1", "2", "3", "4", "5"]

# handles input validation
while option_inputted not in available_options:
    option_inputted = input('Please select option 1 to 5:\n ')

print(f'You selected {option_inputted}')    