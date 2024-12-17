

questions = ("What colour is the ocean? : ",
             "How many elements are in the periodic table?: ",
             "Which animal lays the largest egg?: ",
             "What planet is the hottest?: ",
             "What is 1 + 1?: ")

options = (("A. Blue ", "B. Green ", "C. Yellow ", "D. Red "),
           ("A. 116  ", "B. 117  ", "C. 118  ", "D. 119 "),
           ("A. Chicken ", "B. Ostrich ", "C. Human ", "D. Plant "),
           ("A. Mercury ", "B. Venus ", "C. Earth ", "D. Mars "),
           ("A. 5  ", "B. 2  ", "C. 3  ", "D. 1 "))

answers = ("A", "C", "B", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")#
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----------------------")
print("        RESULTS        ")
print("-----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}% ")
