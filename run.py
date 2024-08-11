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

def get_topic_selection():
    """Prompt the user to select a valid topic option."""
    # Define the set of valid options for topic selection
    available_options = {"1", "2", "3", "4", "5"}
    
    # Prompt the user to select an option, stripping whitespace and converting to lowercase
    selection = input('Select option 1 to 5:\n').strip().lower()
    
    # Continue prompting until the user provides a valid option
    while selection not in available_options:
        selection = input('Invalid selection. Please select option 1 to 5:\n').strip().lower()
    
    return selection