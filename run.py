from questions import ask_multiple_questions

def get_user_name():
    """Prompt the user to create a name and ensure it is non-empty."""
    try:
        name = input('Create a name for you:\n').strip()
        while not name:
            name = input('You did not type anything! Please input a name:\n').strip()
        return name
    except Exception as e:
        print(f"An error occurred while getting your name: {e}")
        return None

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
    while True:
        try:
            selection = input('Select one of the options 1 to 5:\n').strip()
            if selection in valid_options:
                return selection
            else:
                print('Invalid selection! Please select from 1 to 5:\n')
        except Exception as e:
            print(f"An error occurred while selecting a topic: {e}")

def provide_feedback(score, total_questions):
    """Provide feedback based on the user's score."""
    try:
        if total_questions == 0:
            return "No questions were asked. Cannot provide feedback."
        if score == total_questions:
            return "\nYou are a GENIUS!"
        elif score >= total_questions * 0.8:
            return "\nExcellent work!"
        elif score >= total_questions * 0.5:
            return "\nGood job!"
        else:
            return "\nKeep trying, you can do better!"
    except Exception as e:
        print(f"An error occurred while providing feedback: {e}")
        return "Error in feedback."

def end_of_quiz_prompt():
    """Prompt the user to decide whether to return to the home page or exit the game."""
    while True:
        try:
            choice = input("Would you like to return to the home page or exit the game? (home/exit)\n").strip().lower()
            if choice == "home":
                return True
            elif choice == "exit":
                return False
            else:
                print("Invalid choice. Please enter 'home' or 'exit'.")
        except Exception as e:
            print(f"An error occurred while processing your choice: {e}")

def main():
    """Main function to run the quiz setup and track score."""
    try:
        user_name = get_user_name()
        if user_name is None:
            print("Unable to proceed without a valid user name.")
            return

        print("------------------------------------------------")
        print(f'Welcome to the MIND MASTER game, {user_name}!\n')
        print("------------------------------------------------")

        while True:
            # Display available topics and get user's selection
            print("To play the game, select one of the topics below.")
            display_topic_options()

            selected_option = get_topic_selection()
            print(f'You selected option {selected_option}')

            # Prompt for difficulty level
            difficulty_level = input("Select difficulty level (easy/medium/hard):\n").strip().lower()
            valid_difficulties = ["easy", "medium", "hard"]

            while difficulty_level not in valid_difficulties:
                difficulty_level = input("Invalid selection. Options are easy, medium, or hard. Enter again:\n").strip().lower()

            # Ask questions based on the selected option and difficulty level, and track the score
            try:
                score, total_questions = ask_multiple_questions(selected_option, difficulty_level)
                feedback = provide_feedback(score, total_questions)
                print("------------------------------------------------------------------------")
                print(f'Your score for this category is {score}:{total_questions}. {feedback}')
                print("------------------------------------------------------------------------")
            except Exception as e:
                print(f"An error occurred while asking questions: {e}")

            # Ask user if they want to return to the home page or exit the game
            if not end_of_quiz_prompt():
                print("THANK YOU FOR PLAYING! GOODBYE!")
                break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
