import random
import array
import team_selector

def main():

  #setting up the dice
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  dice_sum = 0

  #dice roller and math
  for i in range(0,dice_rolls):
      roll = random.randint(1,dice_size)
      dice_sum += roll
      print(f'You rolled a {roll}')
  if roll == 1:
      print(f'You rolled a {roll}! Bad Roll :(')
  elif roll == dice_size:
      print(f'You rolled a {roll}! Great Roll!')
  else:
      print(f'You have rolled a total of {dice_sum}')

      # WIP arrays for keeping seperate scores
      score1 = array.array('i' , {dice_sum})
      score2 = array.array('i' , {dice_sum})

  print(f'{score1}')
  print(f'{score2}')

if __name__== "__main__":
  main()