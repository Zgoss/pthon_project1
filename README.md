# pthon_project1
# Zachary Gossett
# A quiz asking a variety of questions
print ("Hello, welcome to the quiz. This quiz will ask a variety of questions, on a different number of topics. Lets begin. \n")
score = 0
answer1 =input ("Who currently has the most Surperbowl ring? \na. Emmit Smith \nb. Tom Brady \nc. Peyton Manning \nd. Eli Manning \nAnswer: ")
if answer1 == "b" or answer1 == "Tom Brady":
    score += 1
    print("correct")
    print("score: ", score)
    print("\n")
else:
    print("Wrong! The answer is Tom Brady")
    print("score: ", score)
    print("\n")
answer1 =input ("What is 4 + 5 * 3 / 3 equal to? \nAnswer: ")
if answer1 == "9":
    score += 1
    print("correct")
    print("score: ", score)
    print("\n")
else:
    print("Wrong! The answer is 9 ")
    print("score: ", score)
    print("\n")

     
