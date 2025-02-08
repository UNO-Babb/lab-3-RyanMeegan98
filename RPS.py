#RPS.py
#Name:Ryan Meegan
#Date:Feb 8 2025
#Assignment:Rock Paper Scissors
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  choices = {"rock": "R", "paper": "P", "scissors": "S"}
  print("Welcome to Rock, Paper, Scissors!")

  while True:
    computer_choice = random.choice(["R", "P", "S"])
    user_choice = input("Choose Rock, Paper or Scissors: ").strip().lower()
    if user_choice not in choices:
      print("Invalid choice. Please type Rock, Paper, or Scissors.")
      continue

    user_choice = choices[user_choice]
    computer_full = {v: k.capitalize() for k, v in choices.items()}[computer_choice]

    print(f"Computer chose: {computer_full}")

    if user_choice == computer_choice:
      print("It's a tie!")
      ties += 1

    elif (user_choice == "R" and computer_choice == "S") or \
         (user_choice == "S" and computer_choice == "P") or \
         (user_choice == "P" and computer_choice == "R"):
      print("You win!")
      wins += 1

    else:
      print("You lose!")
      losses += 1

    play_again = input("Play again? (yes/No): ").strip().lower()
    if play_again !="yes":
      break

    print("\nFinal Stats:")
    print("wins \t Ties \t Loses")
    print("---- \t ---- \t ----")
    print(wins, "\t", ties, "\t", losses)


  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
