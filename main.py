
import random
import math
from replit import clear
from art import logo


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  picked = random.choice(cards)
  return picked  
  
def calculate_score(list_name):
  score = sum(list_name)
  if score == 21 and len(list_name) == 2:
    return 0
  
  if 11 in list_name and score >21:
    list_name.remove(11)
    list_name.append(1)
    score = sum(list_name)
  
  return score

def compare(users_total, computers_total):
  if users_total > 21 and  computers_total > 21:
    return "Yall both lose"
  if users_total == computers_total:
    print(f"Its a draw, your score was {users_total} and computers score was {computers_total} ")
  elif users_total == 0:
    print(f"You win, total is {users_total}, computers total is {computers_total}")
  elif computers_total == 0:
    print(f"You lose, total is {users_total}, computers total is {computers_total} blakjack")
  elif users_total > 21:
    print(f"You lose, total is {users_total}, computers total is {computers_total}")
  elif computers_total > 21:
    print(f"You win, total is {users_total}, computers total is {computers_total}")
  elif users_total > computers_total:
    print(f"You win, total is {users_total}, computers total is {computers_total}")
  else:
    print(f"You lose, total is {users_total}, computers total is {computers_total}")

def play_game():    
  print(logo)
  user = [] 
  computer = []
  for entry in range(2):
    user.append(deal_card())
    computer.append(deal_card())
  
  still_in = True
  while still_in:
  
    users_total = calculate_score(user)
    computers_total = calculate_score(computer)
    print(f"Your cards are {user}, your current total is: {users_total}") 
    print(f"Computers first card is: {computer[0]}")
      
    if users_total == 0 or computers_total == 0 or users_total > 21:
      still_in = False
    else:
      draw = input("Would you like to draw another card? ")  
      if draw == 'y':
          user.append(deal_card())
      else:
        still_in = False
          
  while computers_total != 0 and computers_total < 17:
    computer.append(deal_card())
    computers_total = calculate_score(computer)
  compare(users_total, computers_total)
  print(f"Your final hand was {user}")
  print(f"Computers final hand was {computer}")
new_game = input("Do you want to play a game of black jack ? ")
if new_game == 'y':
  clear()
  play_game()
