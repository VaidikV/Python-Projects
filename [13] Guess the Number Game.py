import random

continue_game = True
player_lives_easy = 10
player_lives_hard = 5
#----------
def generate_random_number():
  """
  Returns a randomly generated number between 1 - 100.
  """
  random_number = random.randint(1,100)
  return random_number
random_number = generate_random_number()
#----------
def point_lost(chosen_difficulty):
  """
  Keeps on decreasing the lives of the user if their guess is wrong. If the user has 0 lives left, the function returns message indicating the user has lost.
  """
  if chosen_difficulty == "easy":
    global player_lives_easy
    global continue_game
    if player_lives_easy == 0:
      continue_game = False
      global random_number
      return f"You've run out of guesses, you lose.\nThe correct answer was {random_number}"
    else:
      player_lives_easy -= 1 
  else:
    global player_lives_hard
    if player_lives_hard == 0:
      continue_game = False
      return f"You've run out of guesses, you lose.\nThe correct answer was {random_number}"
    else:
      player_lives_hard -= 1
#----------
def compare(guess, random_number):
  """
  Compares the user-guessed number and the randomly generated number and returns the too high or too low message accordingly. If both numbers are same, the function returns a message indication the user has won.
  """
  if guess == random_number:
    global continue_game
    continue_game = False
    return f"You got it! The answer was {random_number}."
  elif guess > random_number:
    return "Too high"
  elif guess < random_number:
    return "Too low"
  
def game_start():
  """ 
  The game starts here by welcoming the user and asks them to guess the number. After asking the user to guess, the function calls the point_lost function to decrease the point (or end the game if user has no lives left). After decreasing the point, it calls the compare function to compare the user-guessed number and the random number and lets the user know if it's too high or too low. Accordingly, it also lets the user know that they won the game if their numbers matches.
  """
  print("""
  _        ___  __   __     ___       ___                     __   ___  __  
/ _` |  | |__  /__` /__`     |  |__| |__     |\ | |  |  |\/| |__) |__  |__) 
\__> \__/ |___ .__/ .__/     |  |  | |___    | \| \__/  |  | |__) |___ |  \ 
""")
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  # print(random_number)
  chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  while continue_game:
    
    if chosen_difficulty == "easy" and player_lives_easy != 0:
      print(f"You have {player_lives_easy} attempts remaining to guess the number.")
    elif chosen_difficulty == "hard" and player_lives_hard != 0:
      print(f"You have {player_lives_hard} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))
    print(compare(guess, random_number))
    point_lost(chosen_difficulty)

    if player_lives_easy == 0 or player_lives_hard == 0:
      print(point_lost(chosen_difficulty))
#----------xxxx----------

game_start()

    
