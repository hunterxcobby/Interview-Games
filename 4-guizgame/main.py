#!/usr/bin/python3  # This is a shebang line that tells the OS to run the script using Python3

# Print welcome message to the quiz game
print("\n##########################")
print("Hello, Welcome To My Quiz Game\n")

# A list of dictionaries containing the quiz questions and their respective correct answers.
question_bank = [
    {"text": "The ability of one class to acquire methods and attributes from another class is called ___.", "answer": "A"},
    {"text": "Which of the following is a type of inheritance?", "answer": "D"},
    {"text": "What type of inheritance has multiple subclasses inheriting from a single base class?", "answer": "C"},
    {"text": "What is the depth of multilevel inheritance?", "answer": "C"},
    {"text": "What does MRO stand for?", "answer": "B"},
]

# A list of lists, where each sublist contains the multiple-choice options for the corresponding question in question_bank.
options = [
    ["A. Inheritance", "B. Encapsulation", "C. Polymorphism", "D. Abstraction"],
    ["A. Single", "B. Multiple", "C. Multilevel", "D. All of the above"],
    ["A. Single", "B. Multiple", "C. Multilevel", "D. None of the above"],
    ["A. 1", "B. 2", "C. 3", "D. 4"],
    ["A. Method Resolution Order", "B. Multiple Resolution Order", "C. Multi Resolution Order", "D. None of the above"]
]

# Initialize a variable to store the player's score
score = 0

# Define a function to check if the user's guess matches the correct answer
# Takes two arguments: 'guess' (user's choice) and 'answer' (correct answer)
def check_answer(guess, answer):
    # If the guess is correct, return True
    if guess == answer:
        return True
    else:
        # If the guess is incorrect, return False
        return False


# Start of the main loop that iterates over each question in the question_bank
for question_num in range(len(question_bank)):
    # Print a separator for better readability in the console
    print("++++++++++++++++++++++++\n")
    
    
    # Print the current question's text
    print(question_bank[question_num]["text"])

    # Print the options associated with the current question
    for i in options[question_num]:
        print(i)

    # Get the user's guess and convert it to uppercase (to standardize the input)
    guess = input("Enter your answer (A, B, C, D): ").upper()

    # Check if the user's guess is correct by calling the check_answer() function
    is_correct = check_answer(guess, question_bank[question_num]["answer"])
    
    # If the answer is correct
    if is_correct:
        print("Correct Answer!")
        # Increase the score by 1
        score += 1
    else:
        # If the answer is wrong, let the user know
        print("Wrong Answer")
        # Display the correct answer for the user to learn from the mistake
        print(f"Correct Answer is {question_bank[question_num]['answer']}")
    
    # Display the current score after each question is answered
    print(f"Your current score is {score}/{question_num + 1}\n")


# At the end of the quiz, calculate the user's score as a percentage
print(f"You had {(score / len(question_bank)) * 100}% in total ")
