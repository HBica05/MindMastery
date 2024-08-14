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
        selection = input('Invalid selection! Please select from 1 to 5:\n').strip()
    return selection


def provide_feedback(score, total_questions):
    """Provide feedback based on the user's score."""
    if score == total_questions:
        return "You are a GENIUS!"
    elif score >= total_questions * 0.8:
        return "Excellent work!"
    elif score >= total_questions * 0.5:
        return "Good job!"
    else:
        return "Keep trying, you can do better!"



def end_of_quiz_prompt():
    """Prompt the user to decide whether to return to the home page or exit the game."""
    while True:
        choice = input("Would you like to return to the home page or exit the game? (home/exit)\n").strip().lower()
        if choice == "home":
            return True
        elif choice == "exit":
            return False
        else:
            print("Invalid choice. Please enter 'home' or 'exit'.")


def main():
    """Main function to run the quiz setup and track score"""
    user_name = get_user_name()
    print("------------------------------------------------")
    print(f'Welcome to the MIND MASTER game, {user_name}!\n')
    print("------------------------------------------------")

    while True:
        print("To play the game, select one of the topics below.")
        display_topic_options()

        selected_option = get_topic_selection()
        print(f'You selected option {selected_option}')

        # Ask a question based option and difficulty, and track the score
        score = ask_multiple_questions(selected_option)
        total_questions = len([q for q in ask_multiple_questions(selected_option)])

        # Provide feedback based on the score
        feedback = provide_feedback(score, total_questions)
        print(f'Your final score is {score}/{total_questions}. {feedback}')

        # Ask user if they want to return to the home page or exit the game
        if not end_of_quiz_prompt():
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()