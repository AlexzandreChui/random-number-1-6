from random import *
a = randint(1,6)

n = int(input("Enter a number from 1-6:"))

if a < n:
  print("That is incorrect, the number was: %d" %(a))
if a > n:
  print("That is incorrect, the number was: %d" %(a))
if a == n:
  print("That is correct: %d" %(a))