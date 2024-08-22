#!/usr/bin/python3

print("\n##########################")
print("Hello, Welcome To My Quiz Game\n")


question_bank = [
    {"text": "The abilily of one class to acquire methods and attributes from another class is called ___.","answer": "A"},
    {"text": "Which of the following is a type of in inheritance?","answer": "D"},
    {"text": "What type of inherintance has multiple subclasess inheriting from a single base class?","answer": "C"},
    {"text": "What is the depth of multilevel inheritance?","answer": "C"},
    {"text:": "What does MRO stand for","answer": "B"},
]

options = [ ["A. Inheritance", "B. Encapsulation", "C. Polymorphism", "D. Abstraction"],
            ["A. Single", "B. Multiple", "C. Multilevel", "D. All of the above"],
            ["A. Single", "B. Multiple", "C. Multilevel", "D. None of the above"],
            ["A. 1", "B. 2", "C. 3", "D. 4"],
            ["A. Method Resolution Order", "B. Multiple Resolution Order", "C. Multi Resolution Order", "D. None of the above"]
]


for question_num in range(len(question_bank)):
    print(question_bank[question_num])
    # answer = input("Provide your answer here.\n").upper()
    # if answer == question_bank["answer"]:
    #     print("Correct Answer")
    # else:
    #     print("Wrong")