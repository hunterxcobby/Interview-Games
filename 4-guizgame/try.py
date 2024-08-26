#!/usr/bin/python3

questions_bank = [
    {"texts":"What is the name of the president of Ghana?", "Answer": "B"},
    {"texts":"How old is the 46 president of America", "Answer":"C"},
    {"texts":"What is the middle name of Donald Trump", "Answer":"D"},
    {"texts": "Who was the first president of Nigeria", "Answer":"A"},
    {"texts": " When does Ghana celebrate their indeoendendce day"," Answer": "A"}
]


for question in questions_bank:
    print(question["texts"])