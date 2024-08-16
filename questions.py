def get_questions():
    """Return the dictionary of quiz questions by topic."""
    return {
        "1": [
            {"question": "1. What is the capital of France?",
             "answer": "paris",
             "hint": "It's also known as the City of Lights.",
             "difficulty": "easy"},
            {"question": "2. What is the largest city in France?",
             "answer": "paris",
             "hint": "It's the same as the capital of France.",
             "difficulty": "easy"},
            {"question": "1. Which planet is known as the Red Planet?",
             "answer": "mars",
             "hint": "Named after the Roman god of war.",
             "difficulty": "medium"},
            {"question": "2. What is the chemical symbol for gold?",
             "answer": "au",
             "hint": "It comes from the Latin word for gold.",
             "difficulty": "medium"},
            {"question": "1. Who wrote 'To Kill a Mockingbird'?",
             "answer": "harper lee",
             "hint": "Her first name is Harper.",
             "difficulty": "hard"},
            {"question": "2. What is the name of the first artificial satellite launched into space?",
             "answer": "sputnik 1",
             "hint": "It was named after a famous Russian scientist.",
             "difficulty": "hard"},
        ],
        "2": [
            {"question": "1. What is the chemical symbol for water?",
             "answer": "h2o",
             "hint": "It's made up of two hydrogen atoms and one oxygen atom.",
             "difficulty": "easy"},
            {"question": "2. What element has the symbol 'O'?",
             "answer": "oxygen",
             "hint": "It's essential for respiration.",
             "difficulty": "easy"},
            {"question": "1. What is the atomic number of carbon?",
             "answer": "6",
             "hint": "It's the number of protons in a carbon atom.",
             "difficulty": "medium"},
            {"question": "2. What is the freezing point of water in Celsius?",
             "answer": "0",
             "hint": "It's the same as the freezing point of ice.",
             "difficulty": "medium"},
            {"question": "1. What planet is known as the 'Giant Planet'?",
             "answer": "jupiter",
             "hint": "It's the largest planet in our solar system.",
             "difficulty": "hard"},
            {"question": "2. Name the process by which plants convert atmospheric nitrogen into a form usable for their growth?",
             "answer": "nitrogen fixation",
             "hint": "This process involves bacteria and is crucial for enriching the soil.",
             "difficulty": "hard"},
        ],
        "3": [
            {"question": "1. Which sport is known as 'the beautiful game'?",
             "answer": "soccer",
             "hint": "It's called football in most countries.",
             "difficulty": "easy"},
            {"question": "2. How many players are there in a soccer team?",
             "answer": "11",
             "hint": "This includes both outfield players and a goalkeeper.",
             "difficulty": "easy"},
            {"question": "1. Which country won the FIFA World Cup in 2018?",
             "answer": "france",
             "hint": "This country is famous for its Eiffel Tower.",
             "difficulty": "medium"},
            {"question": "2. Term for a baseball game without an opponent?",
             "answer": "batting practice",
             "hint": "It's when a player practices hitting the ball.",
             "difficulty": "medium"},
            {"question": "1. How many points for a touchdown in American football?",
             "answer": "6",
             "hint": "This does not include extra points or field goals.",
             "difficulty": "hard"},
            {"question": "2. Who holds the record for the most career home runs in Major League Baseball (MLB)?",
             "answer": "babe ruth",
             "hint": "This record was set by a player known as The Sultan of Swat.",
             "difficulty": "hard"},
        ],
        "4": [
            {"question": "1. What is the largest ocean on Earth?",
             "answer": "pacific",
             "hint": "It covers more than 60 million square miles.",
             "difficulty": "easy"},
            {"question": "2. Which continent is the Sahara Desert located on?",
             "answer": "africa",
             "hint": "It's the second-largest continent by land area.",
             "difficulty": "easy"},
            {"question": "1. Which river is the primary source of water for the city of Cairo, Egypt?",
             "answer": "nile river",
             "hint": "This river flows northward through northeastern Africa.",
             "difficulty": "medium"},
            {"question": "2. Which river is the longest in South America?",
             "answer": "amazon river",
             "hint": "This river flows through the Amazon Rainforest.",
             "difficulty": "medium"},
            {"question": "3. Which mountain range separates Europe and Asia?",
             "answer": "ural",
             "hint": "It's located in Russia and Kazakhstan.",
             "difficulty": "hard"},
            {"question": "4. Which country has the most time zones?",
             "answer": "russia",
             "hint": "This country spans across the entire width of Eurasia.",
             "difficulty": "hard"},
        ],
        "5": [
            {"question": "1. What is the square root of 64?",
             "answer": "8",
             "hint": "It's a whole number between 7 and 9.",
             "difficulty": "easy"},
            {"question": "2. What is the value of pi to two decimal places?",
             "answer": "3.14",
             "hint": "Ratio of a circle's circumference to its diameter.",
             "difficulty": "easy"},
            {"question": "3. What is the result of 7 * 9?",
             "answer": "63",
             "hint": "It's the product of two single-digit numbers.",
             "difficulty": "medium"},
            {"question": "4. What is 15 divided by 3?",
             "answer": "5",
             "hint": "It's a single-digit number.",
             "difficulty": "easy"},
            {"question": "5. Next number in the sequence: 2, 4, 8, 16, ...?",
             "answer": "32",
             "hint": "Each number is double the previous one.",
             "difficulty": "medium"},
        ]
    }

def ask_multiple_questions(topic, difficulty_level):
    """Ask questions based on the selected topic and difficulty level, and validate the answers."""
    questions = get_questions().get(topic, [])
    score = 0

    try:
        # Filter questions based on the selected difficulty level
        selected_questions = [q for q in questions if q['difficulty'] == difficulty_level]

        # Check for available questions for the selected difficulty level
        if not selected_questions:
            print("No questions available for this difficulty level.")
            return 0, 0  # Return score of 0 if no questions are available

        # Ask the questions to the user
        for q in selected_questions:
            try:
                print(q["question"])
                
                hint_request = input("Do you want a hint? (yes/no)\n").strip().lower()
                if hint_request == "yes":
                    print(f"Hint: {q['hint']}")
                
                user_answer = input("Your answer:\n").strip().lower()
                if user_answer == q["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was {q['answer']}.")
            
            except Exception as e:
                print(f"An error occurred while processing the question: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Return the score and the number of questions asked
    return score, len(selected_questions)
