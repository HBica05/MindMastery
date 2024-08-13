from questions import ask_multiple_questions

def get_user_name():
    """Prompt the user to create a name and ensure it is non-empty."""
    name = input('Create a name for you:\n').strip()
    while not name:
        name = input(
            'You did not type anything! Please input a name:\n').strip()
    return name


def display_topic_options():
    """Display a list of available quiz topics."""
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
    valid_options = ["1", "2", "3", "4", "5"]
    selection = input('Select one of the options 1 to 5:\n').strip()
    while selection not in valid_options:
        selection = input(
            'Invalid selection! Please select from 1 to 5:\n').strip()
    return selection

    
def main():
    """Main function to run the quiz setup and track score"""
    user_name = get_user_name()
    print(f'Welcome to the Mind Master game, {user_name}!\n')
    print("To play the game, select one of the topics below.")

    display_topic_options()

    selected_option = get_topic_selection()
    print(f'You selected option {selected_option}')

    # Ask a question based option and difficulty, and track the score
    score = ask_multiple_questions(selected_option)

    # You can choose to save or display the score here if needed
    print(f'Your final score is {score}.')


if __name__ == "__main__":
    main()