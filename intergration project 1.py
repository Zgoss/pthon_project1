"""
A quiz asking a variety of questions
__author__= "Zachary Gossett"
python_project1
"""
print("Hello, welcome to the quiz. This quiz will ask a variety of questions,"
      " on a different number of topics.\nPlease answer with the letter of "
      "the option, the full name of the option exactly how it appears, \n"
      "or the number of your choosing when required. Lets begin. \n")
player_score = 0
answer1 = input("Who currently has the most Superbowl ring? \na. Emmit Smith"
                " \nb. Tom Brady \nc. Peyton Manning\nd.Eli Manning"
                "\nAnswer: ")

if answer1 == "b" or answer1 == "Tom Brady":
    player_score += 1
    print("correct")
    print("score: ", player_score)
    print("\n")
else:
    print("Wrong! The answer is Tom Brady")
    print("score: ", player_score)
    print("\n")
answer2 = input("What is 4 + 5 * 3 / 3 equal to? \nAnswer: ")
if answer2 == "9":
    player_score += 1
    print("correct")
    print("score: ", player_score)
    print("\n")
else:
    print("Wrong! The answer is 9 ")
    print("score: ", player_score)
    print("\n")
answer3 = input("Who has the most three pointers made in the NBA?"
                " \na. Reggie Miller \nb. Stephen Curry \nc. Ray Allen"
                " \nd. Kyle Korver \nAnswer: ")

if answer3 == "c" or answer3 == "Ray Allen":
    player_score += 1
    print("correct")
    print("score: ", player_score)
    print("\n")
else:
    print("Wrong! The answer is Ray Allen")
    print("score: ", player_score)
    print("\n")
answer4 = input("Who wrote the Declaration of Independence?"
                " \na. John Adams\nb. George Washington\nc. Benjamin Franklin"
                "\nd. Thomas Jefferson \nAnswer: ")

if answer4 == "d" or answer4 == "Thomas Jefferson":
    player_score += 1
    print("correct")
    print("score: ", player_score)
    print("\n")
else:
    print("Wrong! The answer is Thomas Jefferson")
    print("score: ", player_score)
    print("\n")

for x in range(1):
    print("Your score is", player_score)


def number_multiplication(num1, num2):
    """
    calculates score and score as a percentage
    :return: score and score as a percentage
    """

    num1 = player_score
    num2 = 4
    answer5 = num1 / num2 * 100
    print("Your score as a percentage is", format(answer5, "0.2f"), "%")


number_multiplication(player_score, 4)
