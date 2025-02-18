print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay let's play :  ")

score = 0

answer = input("what does CPU stand for?  ")
if answer == "central processing unit":
    print("correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does GPU stands for?  ")
if answer == "Graphic processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does RAM stand for?  ")
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("what does API stand for?  ")
if answer == "Application Programme Interface":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("what does OS for?  ")
if answer == "operating system":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does MS for?  ")
if answer == "mild screening":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does PSU stand for?  ")
if answer == " power supply unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

    print("You got " + str(score) + "questions correct!")
    print("You got" + str(score / 7 * 100) + "%")