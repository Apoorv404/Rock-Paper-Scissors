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

game_images = [rock,paper,scissors]
move = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
rand = random.randint(0,2)
if 0 <= move <= 2:
    print("You chose:")
    print(game_images[move])
print("Computer chose:")
print(game_images[rand])


if move < 0 or move > 2:
    print("You typed invalid input!")
elif move == rand:
    print("It's a draw!")
elif move == 0 and rand == 2:
    print("You win!")
elif move == 2 and rand == 0:
    print("You lose!")
elif rand > move:
    print("You lose!")
elif move > rand:
    print("You win!")
