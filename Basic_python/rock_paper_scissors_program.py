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
user = int(input("What you choose? type 0 for Rock, 1 for paper or 2 for scissors\n"))
game_list = [rock, paper, scissors]
computer = random.choice(game_list)

if user < 0 or user > 2:
    print("invalid input please enter the right input")
else:
    if user == 0:
        print(game_list[user])
        if computer == game_list[0]:
            print("Computer Choice:")
            print(game_list[0])
            print("you made a draw")
        elif computer == game_list[1]:
            print("Computer Choice:")
            print(game_list[1])
            print("you lost")
        else:
            print("Computer Choice:")
            print(game_list[2])
            print("you won")
    elif user == 1:
        print(game_list[user])
        if computer == game_list[0]:
            print("Computer Choice:")
            print(game_list[0])
            print("you won")
        elif computer == game_list[1]:
            print("Computer Choice:")
            print(game_list[1])
            print("you made a draw")
        else:
            print("Computer Choice:")
            print(game_list[2])
            print("you lost")
    else:
        print(game_list[user])
        if computer == game_list[0]:
            print("Computer Choice:")
            print(game_list[0])
            print("you won")
        elif computer == game_list[1]:
            print("Computer Choice:")
            print(game_list[1])
            print("you lost")
        else:
            print("Computer Choice:")
            print(game_list[2])
            print("you made a draw")





