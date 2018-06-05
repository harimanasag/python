import random

rChoice = random.choice([0,1,2,3,4,5,6,7,8,9])

while True:

    uChoice = int(input("Guess a number in between 0 to 9:"))
    if rChoice>uChoice :
      print('Your answer is lower than required')
    elif rChoice<uChoice :
      print('Your answer is greater than required')
    else:
      print('Your answer is PERFECT!! Congratulations!!')
      break

print('random number generated', rChoice)




