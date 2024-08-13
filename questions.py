
def ask_multiple_questions(topic):
    """Ask a question based on the selected topic and validate the answer."""
    questions = {
        "1": [
            {"question": "-What is the capital of France?",
             "answer": "paris",
             "hint": "It's also known as the City of Lights.",
             "difficulty": "easy"},
            {"question": "-What is the largest city in France?",
             "answer": "paris",
             "hint": "It's the same as the capital of France.",
             "difficulty": "medium"},
            {"question": "-Which planet is known as the Red Planet?",
             "answer": "mars",
             "hint": "Named after the Roman god of war.",
             "difficulty": "easy"},
            {"question": "-Who wrote 'To Kill a Mockingbird'?",
             "answer": "harper lee",
             "hint": "Her first name is Harper.",
             "difficulty": "medium"},
            {"question": "-What is the chemical symbol for gold?",
             "answer": "au",
             "hint": "It comes from the Latin word for gold.",
             "difficulty": "hard"}
        ],
        "2": [
            {"question": "-What is the chemical symbol for water?",
             "answer": "h2o",
             "hint": "It's made up of two hydrogen atoms and one oxygen atom.",
             "difficulty": "easy"},
            {"question": "-What element has the symbol 'O'?",
             "answer": "oxygen",
             "hint": "It's essential for respiration.",
             "difficulty": "easy"},
            {"question": "-What is the atomic number of carbon?",
             "answer": "6",
             "hint": "It's the number of protons in a carbon atom.",
             "difficulty": "medium"},
            {"question": "-What planet is known as the 'Giant Planet'?",
             "answer": "jupiter",
             "hint": "It's the largest planet in our solar system.",
             "difficulty": "hard"},
            {"question": "-What is the freezing point of water in Celsius?",
             "answer": "0",
             "hint": "It's the same as the freezing point of ice.",
             "difficulty": "easy"}
        ],
        "3": [
            {"question": "-Which sport is known as 'the beautiful game'?",
             "answer": "soccer",
             "hint": "It's called football in most countries.",
             "difficulty": "easy"},
            {"question": "-How many players are there in a soccer team?",
             "answer": "11",
             "hint": "This includes both outfield players and a goalkeeper.",
             "difficulty": "easy"},
            {"question": "-Which country won the FIFA World Cup in 2018?",
             "answer": "france",
             "hint": "This country is famous for its Eiffel Tower.",
             "difficulty": "medium"},
            {"question": "-Term for a baseball game without an opponent?",
             "answer": "batting practice",
             "hint": "It's when a player practices hitting the ball.",
             "difficulty": "medium"},
            {"question": "-How many points for touchdown in American football?",
             "answer": "6",
             "hint": "This does not include extra points or field goals.",
             "difficulty": "easy"}
        ],
        "4": [
            {"question": "-What is the largest ocean on Earth?",
             "answer": "pacific",
             "hint": "It covers more than 60 million square miles.",
             "difficulty": "easy"},
            {"question": "-Which continent is the Sahara Desert located on?",
             "answer": "africa",
             "hint": "It's the second-largest continent by land area.",
             "difficulty": "medium"},
            {"question": "-Which river is the longest in the world?",
             "answer": "nile",
             "hint": "It flows through northeastern Africa.",
             "difficulty": "medium"},
            {"question": "-What is the smallest country in the world by area?",
             "answer": "vatican city",
             "hint": "It's an independent city-state surrounded by Rome.",
             "difficulty": "hard"},
            {"question": "-Which mountain range separates Europe and Asia?",
             "answer": "ural",
             "hint": "It's located in Russia and Kazakhstan.",
             "difficulty": "hard"}
        ],
        "5": [
            {"question": "-What is the square root of 64?",
             "answer": "8",
             "hint": "It's a whole number between 7 and 9.",
             "difficulty": "easy"},
            {"question": "-What is the value of pi to two decimal places?",
             "answer": "3.14",
             "hint": "Ratio of a circle's circumference to its diameter.",
             "difficulty": "easy"},
            {"question": "-What is the result of 7 * 9?",
             "answer": "63",
             "hint": "It's the product of two single-digit numbers.",
             "difficulty": "medium"},
            {"question": "-What is 15 divided by 3?",
             "answer": "5",
             "hint": "It's a single-digit number.",
             "difficulty": "easy"},
            {"question": "-Next number in the sequence: 2, 4, 8, 16, ...?",
             "answer": "32",
             "hint": "Each number is double the previous one.",
             "difficulty": "medium"}
        ]
    }

    score = 0
    difficulty_level = input(
        "Select difficulty level (easy/medium/hard):\n").strip().lower()
    difficulty = ["easy", "medium", "hard"]
    while difficulty_level not in difficulty:
        difficulty_level = input(
            "Invalid, options are easy, medium or hard, enter again:\n").strip(
            ).lower()

    selected_questions = [q for q in questions.get(
        topic, []) if q['difficulty'] == difficulty_level]

    if not selected_questions:
        print("No questions available for this difficulty level.")
        print("Please choose a different level.")
        return 0

    for q in selected_questions:
        print(q["question"])
        hint = input("Do you want a hint? (yes/no)\n").strip().lower()
        if hint == "yes":
            print(f"Hint: {q['hint']}")
        user_answer = input("Your answer:\n").strip().lower()
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f'Your score for this topic is {score}/{len(selected_questions)}.')
    return score
