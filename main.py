print("Welcome to number guessing game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Select your difficulty, easy or hard: ")

while difficulty != "easy" or difficulty != "hard":
  difficulty = input("Your difficulty entry was invalid\nPlease try again: ")


