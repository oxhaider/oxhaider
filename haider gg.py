import os, sys
import random

while True:
    p = input ("enter you password")
    pasword = "oxaamir"
    if p == pasword :
        break
    else:
        ("wronge password")





def choices():
    n = random.randrange(1, 4)
    computer = ""
    if (n == 1):
        computer = 'Rock'
    elif (n == 2):
        computer = "scissors"
    else:
        computer = 'paper'

    player = input('choose and enter one of the choices- Rock, Paper or Scissors: ')
    print(computer)
    return computer, player





def rule(computer, player):
    while (computer == player):
        computer, player = choices()
    if(computer == 'Rock') and (player == 'Scissors' or "s" or "S"):
        print('computer wins !')
    elif (computer == 'scissors') and (player == 'Rock' or "r" or "R"):
        print('You win!')
    elif (computer == 'Paper') and (player == 'Scissors' or "s" or "S"):
        print('you win!')
    elif (computer == 'scissors') and (player == 'Paper'or "p" or "P"):
        print('computer win')
    elif (computer == 'Rock') and (player == 'Paper' or "p" or "P"):
        print('you win')
    elif (computer == 'paper') and (player == 'Rock'or "r" or "R"):
        print('computer win')
    return



def main():
    computer, player = choices()
    rule(computer, player)
    sys.exit(0)




if (__name__=="__main__"):
    main()
