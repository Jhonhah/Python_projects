import random

from select import select

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
computer = random.randint(0,2)
user = int(input("What do you choose? type 0 for Rock, 1 for paper and 2 for scissors\n"))
print(f"You chose {options[user]}")
print(f"The computer chose {options[computer]}")

if user == computer:
    print("looks like a draw")
elif user > computer:
    if user == 2 and computer == 1:
        print("You lose") 
    else:{
        print("You win")
    }
else:
    print("you lose")


