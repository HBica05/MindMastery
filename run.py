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
    # Print a formatted list of available quiz topics for the user to choose from
    print("""
Topics:
1. General Knowledge
2. Science
3. Sports
4. Geography
5. Mathematics
    """)

def get_topic_selection():
    """Prompt the user to select a valid topic option."""
    # Define the set of valid options for topic selection
    available_options = {"1", "2", "3", "4", "5"}
    
    # Prompt the user to select an option, stripping whitespace and converting to lowercase
    selection = input('Select one of the options 1 to 5:\n').strip().lower()
    
    # Continue prompting until the user provides a valid option
    while selection not in available_options:
        selection = input('Invalid selection. Please select option 1 to 5:\n').strip().lower()
    
    return selection

def main():
    """Main function to run the quiz setup."""
    # Get the user's name and welcome them to the game
    user_name = get_user_name()
    print(f'Welcome to the Mind Master game, {user_name}!\n')
    
    # Display the list of available quiz topics
    display_topic_options()
    
    # Get and validate the user's topic selection
    selected_option = get_topic_selection()
    print(f'You selected option {selected_option}')

# Entry point of the script
if __name__ == "__main__":
    main()


def ask_question(topic):
    """Ask a question based on the selected topic and validate the answer."""
    questions = {
        "1": {"question": "What is the capital of France?", "answer": "paris"},
        "2": {"question": "What is the chemical symbol for water?", "answer": "h2o"},
        "3": {"question": "Which sport is known as 'the beautiful game'?", "answer": "soccer"},
        "4": {"question": "What is the largest ocean on Earth?", "answer": "pacific"},
        "5": {"question": "What is the square root of 64?", "answer": "8"}
    }