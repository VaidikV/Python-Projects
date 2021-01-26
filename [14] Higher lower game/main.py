from random import choice
from game_data import data
from art import logo, vs 
from replit import clear


game_won = False
game_continue = True
the_list = []
the_lower_one = []
correct_answers = []
correct_celeb_AB = ""
score = 0

def celeb_adder(num):
  """ Appends any number of random celeb dictionaries from the data list situated in game_data."""
  for _ in range(num):
    random_celeb = choice(data)
    data.remove(random_celeb)
    the_list.append(random_celeb)

def the_list_editor():
  """ This function compares the 2 celeb profiles in the_list and declares one as the winner (A or B)."""
  global correct_celeb_AB
  if the_list[0]['follower_count'] > the_list[1]['follower_count']:
    # the_lower_one.append(the_list[1])    
    # correct_answers.append(the_list[0])
    correct_celeb_AB = "A"
  else:
    # the_lower_one.append(the_list[0])
    # correct_answers.append(the_list[1])
    correct_celeb_AB = "B"


def next_round_prep():
  """ This list is used for getting ready for the next round. It removes the winning celeb profile from the_list list."""
  global correct_celeb_AB
  if the_list[0]['follower_count'] > the_list[1]['follower_count']:
    the_list.remove(the_list[0])
    # the_lower_one.clear()
    correct_celeb_AB = ""
  else:
    the_list.remove(the_list[1])
    # the_lower_one.clear()
    correct_celeb_AB = ""

def next_round():
  """ This function is called if the user guesses the correct answer. """
  next_round_prep()
  celeb_adder(1)
  the_list_editor()

celeb_adder(2)
the_list_editor()

def game():
  """ The superficial details of the game enclosed in a function. If the user wins, the screen is cleared and this function is called again. This function uses all the functions created above to carry out calculations."""
  global game_won
  global game_continue
  global score

  compare_a = f"Compare A: {the_list[0]['name']}, a {the_list[0]['description']}, from {the_list[0]['country']}."
  compare_b = f"Compare B: {the_list[1]['name']}, a {the_list[1]['description']}, from {the_list[1]['country']}."

  while game_continue:
    print(logo)
    if game_won == True:
      print(f"You're right! Current score: {score}.")
    print(compare_a)
    print(vs)
    print(compare_b)
    ask = input("Who has more followers? Type 'A' or 'B': ")
    if ask == correct_celeb_AB:
      clear()
      next_round()
      score += 1
      game_won = True
      game()
      
  
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}.")
      game_continue = False


game()












