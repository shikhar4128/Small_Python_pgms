#!/usr/bin/env python
import random

correct_num=random.randint(1,21)
guesses=[]
print("Hello! What is your name?")
myname=input()
print("\n")
print(f'Well, {myname}, I am thinking of a number between 1 and 20')
print("You will get six attempts to guess the number!!" +"\n")

for i in range (1,7):
    print(f'Take a guess - Attempt :{i}')
    mynumber=int(input())
    guesses.append(mynumber)
    if mynumber==correct_num:
        print("\n")
        print(f'Good job {myname}! You guessed the number in {len(guesses)} attempts')
        break
    elif mynumber > correct_num:
        print('Your guess is higher than the correct number'+"\n")
    else:
        print('Your guess is lower than the correct number'+"\n")

if mynumber!=correct_num:
    print("\n")
    print('Well! you maxed out your attempts. Bad luck.')
    print(f'The number I was thinking of was {correct_num}')
        
   


        
        


      
