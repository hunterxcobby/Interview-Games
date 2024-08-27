#!/usr/bin/python3

questions_bank = [
    {"texts":"What is the name of the president of Ghana?", "Answer": "B"},
    {"texts":"How old is the 46 president of America", "Answer":"C"},
    {"texts":"What is the middle name of Donald Trump", "Answer":"D"},
    {"texts": "Who was the first president of Nigeria", "Answer":"A"},
    {"texts": "When does Ghana celebrate their independendce day", "Answer": "A"}
]


options = [
    ["A. Kofi Appiah", "B. Akuffo Addo", "C. John Rawlings", "D. Atta Mills"],
    ["A. 12", "B. 24", "C. 45", "D. 71"],
    ["A. Charles", "B. Darwins", "C. Goodluck", "D. None of the above."],
    ["A. Kwame Nkrumah", "B. Donald Trump", "C. Jonathan Goodluck", "D. Asiedu Ampofo"],
    ["A. 1986", "B. 1452", "C. 1919", "D. 1957"]
]


def check_answer(quess, options):

    if quess == options:
        return True
    else:
        return False

numbering = 0
scores = 0

print("\nWelcome to the quiz game")

for question_number in range(len(questions_bank)):

    numbering += 1

    print(f"{numbering}. " + questions_bank[question_number]["texts"])
    print("++++++++++++++++++++++++++++++++\n")

    
    for i in options[question_number]:
        print(i)

    guess = input("Please choose from (A/B/C/D) ").upper()

    correct_answer = check_answer(guess, questions_bank[question_number]["Answer"])

    if correct_answer:
        print(f"Correct !")
        scores += 1
        print(f"Your score is {scores}/{numbering}")
    else:
        print(f'Wrong the answer is {questions_bank[question_number]["Answer"]}')
        print(f"Your score is {scores}/{numbering}")


    print("\n")