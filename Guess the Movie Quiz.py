<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:32:44 2020

@author: Stephen James Mebana
"""
    
# function to check scores
def check_answers(answers, corrects):
    score = 0

    for i in range(min(len(answers), len(corrects))):
        if answers[i].upper() == corrects[i].upper():
            score += 1

    rate = (score / 4) * 100

    if rate == 100:
        comment = "PERFECT!"
    elif rate < 100 and rate >= 75:
        comment = "Good Job."
    else:
        comment = "You failed."

    return [score, rate, comment]

# start of variables
eol = "\n"  
username = input("Hey there! Enter your name to play:")
question_num = 1
answers = []
corrects = []
questions = [
             ('🌊🧔🔱🐟', 'a. 2012' + eol + 'b. Aquaman' + eol + 'c. Oceans 11' + eol, 'b'),
             ('👨‍🦱👴🏎️⌚', 'a. Back to the Future' + eol + 'b. Rush Hour' + eol + 'c. The Curious Case of Benjamin Button' + eol, 'a'), 
             ('🏰👩👩‍🦳❄️☃️', 'a. Frozen' + eol + 'b. Anastacia' + eol + 'c. Jack Frost' + eol, 'a'), 
             ('🌊1️⃣1️⃣', 'a. 2012' + eol + 'b. Little Mermaid' + eol + 'c. Oceans 11' + eol, 'c')
            ]


#
print('Guess the Movie Quiz')
# username is required to play
while username == "":
    username = input("Hey there! Enter your name to play:")

# loops and user input
if username != "":
    print(eol + "Hi " + str(username.title()) + "! Enter the letter of your answer." +eol)

# game play
while len(answers) != len(questions):
    for question, options, correct_answers in questions:
        print(eol + "Guess the movie #" + str(question_num))
        print(question)

        answer = input(str(options))
        answers.append(answer)
        corrects.append(correct_answers)
        question_num += 1

# game result 
result = check_answers(answers, corrects)
score =  result[0]
rate = result[1]
comment = result[2]
print(eol + "<h1>Your score is " + str(score) + " out of 4" + eol + "Your rate is " + str(rate) + "! " + str(comment) + "</h1>")


=======
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:32:44 2020

@author: Stephen James Mebana
"""
    
# function to check scores
def check_answers(answers, corrects):
    score = 0

    for i in range(min(len(answers), len(corrects))):
        if answers[i].upper() == corrects[i].upper():
            score += 1

    rate = (score / 4) * 100

    if rate == 100:
        comment = "PERFECT!"
    elif rate < 100 and rate >= 75:
        comment = "Good Job."
    else:
        comment = "You failed."

    return [score, rate, comment]

# start of variables
eol = "\n"  
username = input("Hey there! Enter your name to play:")
question_num = 1
answers = []
corrects = []
questions = [
             ('🌊🧔🔱🐟', 'a. 2012' + eol + 'b. Aquaman' + eol + 'c. Oceans 11' + eol, 'b'),
             ('👨‍🦱👴🏎️⌚', 'a. Back to the Future' + eol + 'b. Rush Hour' + eol + 'c. The Curious Case of Benjamin Button' + eol, 'a'), 
             ('🏰👩👩‍🦳❄️☃️', 'a. Frozen' + eol + 'b. Anastacia' + eol + 'c. Jack Frost' + eol, 'a'), 
             ('🌊1️⃣1️⃣', 'a. 2012' + eol + 'b. Little Mermaid' + eol + 'c. Oceans 11' + eol, 'c')
            ]


#
print('Guess the Movie Quiz')
# username is required to play
while username == "":
    username = input("Hey there! Enter your name to play:")

# loops and user input
if username != "":
    print(eol + "Hi " + str(username.title()) + "! Enter the letter of your answer." +eol)

# game play
while len(answers) != len(questions):
    for question, options, correct_answers in questions:
        print(eol + "Guess the movie #" + str(question_num))
        print(question)

        answer = input(str(options))
        answers.append(answer)
        corrects.append(correct_answers)
        question_num += 1

# game result 
result = check_answers(answers, corrects)
score =  result[0]
rate = result[1]
comment = result[2]
print(eol + "<h1>Your score is " + str(score) + " out of 4" + eol + "Your rate is " + str(rate) + "! " + str(comment) + "</h1>")


>>>>>>> c7661adc3d767b07f712a25a588a05981ead6eed
