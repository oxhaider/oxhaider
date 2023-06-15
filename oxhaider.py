import os,  sys
import random

x = random.randint (1,10)

while True:
  y = int(input("What number I am thinking of ?"))
  if y == x :
    print ("You got it!  ")
    break 
  elif x > y :
    print ("the number is low ")
  else :
    print ("No, thats high")
