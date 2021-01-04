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
rps = [ rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3:
    print("You chose a value that doesn't exist. You lose.")
else:
    print(rps[user_choice])
    print("Computer chose:")
    
    computer = random.randint(0, 2)
    print(rps[computer])

    if user_choice == computer:
        print("It's a draw.")
    elif user_choice == 0 and computer == 1:
        print("You lose.")
    elif user_choice == 0 and computer == 2:
        print("You Win!")
    elif user_choice == 1 and computer == 0:
        print("You Win!")
    elif user_choice == 1 and computer == 2:
        print("You lose.")
    elif user_choice == 2 and computer == 0:
        print("You lose.")
    elif user_choice == 2 and computer == 1:
        print("You Win!")

    

  




