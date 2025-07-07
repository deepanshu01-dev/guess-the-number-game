# Guess The number Game 

import random # importing random module to generate random number

def guess_until_win(user, computer): # function that ask user until correct guess
  while (user > computer):
    print("lower number please")
    game_rule(computer)
    break


  while (user < computer):
    print("higher number please")
    game_rule(computer)
    break

def game_rule(computer): # function that check that handle user guesses
  user = int(input("Guess the number: "))
  if (user == computer):
    print(f"Your Choice: {user}, computer Choice: {computer}. You Win!")

  elif (user > computer):
    print(f"Your Choice: {user}.")    
    guess_until_win(user, computer)  

  
  elif (computer > user): 
    print(f"Your Choice: {user}.")
    guess_until_win(user, computer)
  
computer = random.randint(1, 10)
game_rule(computer)

