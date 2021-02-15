import random

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

image = [rock, paper, scissors]
usrChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
cpuChoice = random.randint(0, 2)

if usrChoice == 0:
  print(image[0])
elif usrChoice == 1:
  print(image[1])
elif usrChoice == 2:
  print(image[2])
else:
  print("Error1")


if cpuChoice == 0:
  print("Computer chose: Rock")
  print(image[0])
elif cpuChoice == 1:
  print("Computer chose: Paper")
  print(image[1])
elif cpuChoice == 2:
  print("Computer choce: Scissors")
  print(image[2])
else:
  print("Error2")

if usrChoice == cpuChoice:
  print("Its a draw")
elif usrChoice == 0:
  if cpuChoice == 2:
    print("You win!")
  else:
    print("You lost :(")
elif usrChoice == 1:
  if cpuChoice == 0:
    print("You win!")
  else:
    print("You lost :(")
elif usrChoice == 2:
  if cpuChoice == 1:
    print("You win!")
  else:
    print("You lost :(")
else:
  print("Error3")