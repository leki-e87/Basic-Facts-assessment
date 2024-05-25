import random

numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Check user has entered a valid response for instructions
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"


# Check user has entered a valid operator
def int_check(question):
    while True:
        error = "Please enter a valid operator."

        response = input(question)

        if response == "+" or response == "addition" or response == "plus" or response == "add":
            print("You chose addition")
            return "+"

        elif response == "-" or response == "subtraction" or response == "subtract" or response == "minus":
            print("You chose subtraction")
            return "-"

        elif response == "x" or response == "multiplication" or response == "times" or response == "multiply":
            print("You chose multiplication")
            return "x"

        elif response == "/" or response == "division" or response == "divide":
            print("You chose division")
            return "/"

        elif response == "r" or response == "random" or response == "randomise":
            print("You chose random")
            return "r"

        else:
            print(error)


def instructions():
    print('''
             Choose an operator to begin the quiz.
             You can choose between multiplication, addition, subtraction and division.
             Or, you can press <R> to randomise it.
             
             You need to press "+" (Addition), "-" (Subtraction), "x" (Multiplication or "/" (Division) 
    ''')


# main routine

# variables for gameStart
# user chooses amount of questions


q_correct = 0
q_wrong = 0

numOne = random.choice(numlist)
numTwo = random.choice(numlist)

operator_list = ["+", "-", "x", "/"]
answerHistory = []

print("Basic Math Quiz - Alexander Motufoua")
print()
print()

want_instructions = yes_no("Would you like instructions for this quiz?")
if want_instructions == "yes":
    instructions()

# Check which operator users want to use for the quiz
question_check = int_check(" Which operator would you like to use?")
