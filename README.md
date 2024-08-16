# Mind Master Quiz Game

Welcome to the MIND MASTER Quiz Game! This is an interactive quiz application designed to test your knowledge across various topics with different difficulty levels. This README provides detailed instructions on how to use, install, and contribute to the project.

[Live project hosted on Heroku]:()

 Mind Mastery repository URL: [https://github.com/yourusername/mind-master-quiz-game]

# Overview
The MIND MASTER Quiz Game is a Python-based quiz application that allows users to answer questions from multiple topics. Users can choose from various topics and difficulty levels to tailor the quiz to their preferences. The application provides feedback based on user performance and allows them to continue or exit after each quiz session.

## Features

* Interactive Quiz: Users can select from different quiz topics and difficulty levels.

* Hints: Optional hints are provided for each question to help users.

* Feedback: After completing the quiz, users receive feedback based on their performance.

* Easy Navigation: Users can choose to return to the home page or exit the game after completing a quiz.

## Installation
### Prerequisites

* Python 3.x installed on your system.

* Basic knowledge of how to run Python scripts.

### Steps to Install

1. Clone the Repository
   
   [Cloning of the Repository Code locally] (#Cloning-of-the-Repository-Code-locally)
   * git clone https://github.com/yourusername/mind-master-quiz-game.git
   
   * cd mind-master-quiz-game(project directory)

    ![alt text](image-10.png)

2. Ensure Python Environment.
* Make sure you have Python 3.x installed. You can verify this by running:
  
    ![alt text](image-9.png)

3. Navigate to Project Directory
 * Change to the directory where the run.py and questions.py files are located.  

4. Run the Application

* Execute the following command to start the quiz game:  
    ![alt text](image-11.png)  


## Usage
### Running the Game
1. Start the Game

* Run the run.py script using Python. The application will prompt you to enter a name and select a quiz topic.
     
    ![alt text](image-1.png)

    ![alt text](image-2.png)

2. Select a Topic

* You will be presented with a list of topics. Choose a number corresponding to the topic you want to be quizzed on.
    
    ![alt text](image-3.png)

3. Choose Difficulty Level

* After selecting a topic, you will be asked to choose a difficulty level: easy, medium, or hard.
    
    ![alt text](image-4.png)

4. Answer Questions

* Answer the questions as they appear. You can request a hint if needed.

![alt text](image-5.png)

5. Review Feedback

* After answering all questions, the game will provide feedback on your performance and your final score.
  
![alt text](image-6.png)

![alt text](image-7.png)

![alt text](image-12.png)
    
6. Continue or Exit

You will have the option to return to the home page or exit the game.

![alt text](image-13.png)

   * If exit is selected, a message is displayed, 
    
![alt text](image-14.png)

   * otherwise it returns to the main menu and the game starts all over again.

![alt text](image-15.png)

## File Structure
* `run.py`: The main script that runs the quiz game. Handles user input, displays questions, and provides feedback.
  
* `questions.py`: Contains quiz questions categorized by topic and difficulty level. Provides functions to retrieve and filter questions.

## Functions Overview
### `run.py`
* `get_user_name()`
    * Prompts the user to create a name. Ensures the input is non-empty.

* `display_topic_options()`
    * Displays a list of available quiz topics to choose from.

* `get_topic_selection()`
    * Prompts the user to select a valid topic option from 1 to 5.

* `provide_feedback(score, total_questions)`
    * Provides feedback based on the user's score out of the total number of questions.

* `end_of_quiz_prompt()`
    * Prompts the user to decide whether to return to the home page or exit the game.

* `main()`
    * Runs the main quiz game setup, handles user interactions, and tracks the score. It controls the flow of the game, from selecting topics to providing feedback and managing game sessions.
### `questions.py`
1. `get_questions()`

    * Returns a dictionary of quiz questions categorized by topic and difficulty level.
2. `ask_multiple_questions(topic, difficulty_level)`
   
   *  Asks a set of questions based on the selected topic and difficulty level, validates answers, and calculates the score.
  
## Contributing
* Contributions to the MIND MASTER Quiz Game are welcome! If you'd like to contribute, please follow these guidelines:

* Fork the Repository: Create your own fork of the repository.
* Clone Your Fork: Clone the forked repository to your local machine.
* Create a Branch: Create a new branch for your changes.
* Make Your Changes: Implement your changes or improvements.
* Test Your Changes: Ensure your changes work as expected and do not introduce bugs.
* Submit a Pull Request: Push your changes to your fork and submit a pull request to the original repository.

## Cloning of the Repository Code locally

* Go to the Github repository that you want to clone.
* Click on the Code button located above all the project files.
* Click on HTTPS and copy the repository link.
* Open the IDE of your choice and and paste the copied git url into the IDE terminal.
* The project is now created as a local clone.

## Deployment

## Contact

For any issues or contributions, please contact 
- bicahaadiyah@gmail.com