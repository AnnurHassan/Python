import random

name = input("Please enter your name: ")
question = input("Enter yout question: ")
answer = ""

random_number = random.randint(1, 9)

if random_number == 1:
    answer = "Yes - Definitely."

elif random_number == 2:
    answer = "It is decidedly so."

elif random_number == 3:
    answer = "Without a doubt."

elif random_number == 4:
    answer = "Reply hazy ,try again."

elif random_number == 5:
    answer = "Ask again later."

elif random_number == 6:
    answer = "Better not tell you know."

elif random_number == 7:
    answer = "My sources say no."

elif random_number == 8:
    answer = "Outlook not so good."

elif random_number == 9:
    answer = "Very doubtful"

else:
    answer = "Error"


print(f'{name} asks: {question}')
print(f"Magic *-Ball's answer: {answer}")