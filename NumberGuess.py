
# coding: utf-8

# In[1]:


""" The program rolls a pair of dice and asks the user to guess the sum. If the user's guess is equal to the total value of the dice roll, the user wins! Otherwise, the computer wins"""
from random import randint
from time import sleep 
def get_user_guess():
  guess = int(input("Guess a number: "))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides*2
  print("The maximum possible value is %d" %max_val)
  guess = get_user_guess()
  if guess > max_val:
    print("The guess is Invalid")
  else:
    print("Rolling...")
    sleep(2)
    print("The first roll is %d"%first_roll)
    sleep(1)
    print("The second roll is %d"%second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print(total_roll)
    print("Result...")
    sleep(1)
    if guess == total_roll:
      print("you have won the game")
    else:
      print("Sorry, you have lost the game")

