import random


# function to check whether user chooses yes or no for the instructions
def yes_no(question):
    while True:
        # display error if user chooses anything other than yes or no
        error = "Please enter a valid response. (Say 'Yes' or 'No'.)"
        response = input(question).lower()

        # if the user says yes or y, display the instructions
        if response == "yes" or response == "y":
            return "yes"
        # if the user says no or n, skip them
        elif response == "no" or response == "n":
            return "no"
        # if the user types an invalid response, print error statement
        else:
            return error


# provides history of every question at the end of the quiz
def quiz_history():
    while True:
        # if the user chooses no as their response, print "thank you" message and end quiz
        show_history = yes_no("Would you like to see the quiz history?: ")
        if show_history == "no" or show_history == "n":
            print("🏁 Thank you for playing my Basic Facts quiz, I hope you enjoyed! 🏁")
            break

        # display history
        for item in history_list:
            print(item)

        # if user chooses yes as their response, display history and then "thank you" message + end quiz
        if show_history == "yes" or show_history == "y":
            print("🏁 Thank you for playing my Basic Facts quiz, I hope you enjoyed! 🏁")
            print()
            break


# instructions function to be called at the start of the quiz
def instructions():
    print('''
           🔰🔰  Welcome to my Addition quiz! Choose between 1 and 30 questions,
             and if you're feeling smart, you can press [ENTER] to play infinitely.
             If you feel like quitting at anytime during INFINITE MODE, feel free to
             type "xxx" to quit the quiz. Have fun, good luck! 🔰🔰''')


def int_check(question):
    while True:
        # error message if user chooses an improper integer for the amount of questions
        error = "Please enter a proper integer."

        # checks user input to ensure they provide proper answers
        # to engage infinite mode, or quit the quiz
        to_check = input(question)

        # if user presses enter, return infinite mode
        if to_check == "":
            return "infinite"
        # if user enters "xxx", return exit code
        elif to_check == "xxx":
            return "xxx"

        # checks for valid integer input
        try:
            response = int(to_check)

            # checks that the number of questions are more than / equal to 1 + less than 30
            if response < 1:
                print(error)

            elif response > 30:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# routine begins
print("Basic Math Quiz - Alexander Motufoua")

# asks user if they want instructions
want_instructions = yes_no("Would you like to read the instructions? ")

# if user says yes, display instructions
if want_instructions == "yes":
    instructions()

# starting the quiz in regular mode
mode = "regular"

# starting quiz with "questions answered" and "answered correctly" as 0
q_answered = 0
q_correct = 0
history_list = []

# asks for number of questions and offers infinite mode
q_amount = int_check('''
How many questions would you like? Choose between 1 and 30 questions.
You can also press [ENTER] for infinite mode, then type "xxx" while IN infinite mode to quit the quiz. ''')

# checks for infinite mode
if q_amount == "infinite":
    mode = "infinite"
    q_amount = 5

# quiz loop begins
while q_amount > q_answered:
    # question headings (based on mode)
    if mode == "infinite":
        q_heading = f"\n Question {q_answered + 1} (Infinite Mode)"
    else:
        q_heading = f"\n Question {q_answered + 1} of {q_amount}! "

    print(q_heading)

    # generates a series of random numbers and puts them into equations
    int_one = random.randrange(1, 10)
    int_two = random.randrange(1, 10)
    int_three = random.randrange(5, 10)

    equation = int_one + int_two + int_three
    main_question = f"{int_one} + {int_two} + {int_three}"
    print(main_question)

    answer = int_check("Answer here! = ")
    if answer == equation:
        q_correct += 1
        print("Nice, you got it right! ")

    elif answer == "xxx":
        break

    else:
        print("Ahh, you got it wrong!")

    # if the user gets their answer correct, add 1 point to the "answered correctly" variable
    result = answer

    if result == equation:
        feedback = f" Nice! This one was correct! - 🏆 "
        q_correct += 1

    else:
        feedback = "Darn, you got this one wrong. - 😪"

    # headings for the quiz history

    history_item = f"Question {q_answered + 1} - {feedback}"

    # adds the history item to the history list
    history_list.append(history_item)

    q_answered = q_answered + 1

    # if users are in infinite mode, increase number of questions
    if mode == "infinite":
        q_amount += 1

# display quiz history at the end of the quiz
quiz_history()
