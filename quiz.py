print("Welcome to the quiz")

playing = input("Do you want to play? ")
score = 0


if playing.lower() != "yes":
    quit()

print("Ok! Let's play :)")

answer = input("What is cognition? ")

if answer.lower() == "mental processes":

    print("correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("Who developed classical conditioning? ")

if answer.lower() == "ivan pavlov":

    print("correct!")
    score += 1
    
else:
    print("Incorrect!")

answer = input("What does ADHD mean? ")
if answer.lower() == "Attention Deficit Hyperactivity":
    print("correct!")
    score += 1

else:

    print("Incorrect!")
answer = input("What is operant conditioning? ")
if answer.lower() == " Learning by consequences":

    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who proposed hierarchy of needs? ")
if answer.lower() == " Abraham Maslow":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
print("you got " + str(score) + " questions correct!")
print("you got " + str((score/5) * 100) + "%")
