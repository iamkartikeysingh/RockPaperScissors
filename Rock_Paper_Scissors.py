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
game_image = [rock, paper, scissors]
user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if user_choice>=3 or user_choice<0:
    print("You typed the wrong key. You lose.")
else:
    print(game_image[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer Chose: ")
    print(game_image[computer_choice])
    if user_choice == computer_choice:
        print("Draw")
    elif user_choice==0 and computer_choice==1:
        print("You Lost")
    elif user_choice==0 and computer_choice==2:
        print("You Won")
    elif user_choice==1 and computer_choice==0:
        print("You Won")
    elif user_choice==1 and computer_choice==2:
        print("You Lost")
    elif user_choice==2 and computer_choice==0:
        print("You Lost")
    elif user_choice==2 and computer_choice==1:
        print("You Won")