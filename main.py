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
import random
# Taking User Input
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
# Assigning user input to images
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("Wrong Choice")

game = [rock,paper,scissors]

computer = random.choice(game)

print("Computer Chose \n", computer)

# Checking Winner

if choice == 0 and computer == rock:
  print("It's a draw")
elif choice == 0 and computer == paper:
  print("You Loose")
elif choice == 0 and computer == scissors:
  print("You Win!")
elif choice == 1 and computer == paper:
  print("It's a draw")
elif choice == 1 and computer == scissors:
  print("You Loose")
elif choice == 1 and computer == rock:
  print("You Win!")
elif choice == 2 and computer == paper:
  print("You Win!")
elif choice == 2 and computer == scissors:
  print("It's a draw")
elif choice == 2 and computer == rock:
  print("You Loose")
