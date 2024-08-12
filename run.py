def get_user_name():
    """Prompt the user to create a name and ensure it is non-empty."""
    name = input('Create a name for you:\n').strip()
    while not name:
        name = input('You did not type anything! Please input a name:\n').strip()
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
    valid_options = {"1", "2", "3", "4", "5"}
    selection = input('Select one of the options 1 to 5:\n').strip()
    while selection not in valid_options:
        selection = input('Invalid selection! Please select from 1 to 5:\n').strip()
    return selection




def ask_multiple_questions(topic):
    """Ask a question based on the selected topic and validate the answer."""
    questions = {
        "1": [
            {"question": "What is the capital of France?", "answer": "paris"},
            {"question": "What is the largest city in France?", "answer": "paris"}
        ],
        "2": [
            {"question": "What is the chemical symbol for water?", "answer": "h2o"},
            {"question": "What element has the symbol 'O'?", "answer": "oxygen"}
        ],
        "3": [
            {"question": "Which sport is known as 'the beautiful game'?", "answer": "soccer"},
            {"question": "How many players are there in a soccer team?", "answer": "11"}
        ],
        "4": [
            {"question": "What is the largest ocean on Earth?", "answer": "pacific"},
            {"question": "Which continent is the Sahara Desert located on?", "answer": "africa"}
        ],
        "5": [
            {"question": "What is the square root of 64?", "answer": "8"},
            {"question": "What is the value of pi (π) rounded to two decimal places?", "answer": "3.14"}
        ]
    }
    score = 0
    # Question asking and answer validation
    for q in questions.get(topic, []):
        user_answer = input(q["question"] + "\n").strip().lower()
        if user_answer == q["answer"]:
            print("Correct!")
            score +=1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")  
    print(f'Your score for this topic is {score}/{len(questions.get(topic, []))}.')


def main():
    """Main function to run the quiz setup and track score"""
    # Get the user's name and welcome them to the game
    user_name = get_user_name()
    print(f'Welcome to the Mind Master game, {user_name}!\n')
    
    # Display the list of available quiz topics
    display_topic_options()
    
    # Get and validate the user's topic selection
    selected_option = get_topic_selection()
    print(f'You selected option {selected_option}')

    # Ask a question based on the selected option and track the score
    ask_multiple_questions(selected_option)


if __name__ == "__main__":
    main()