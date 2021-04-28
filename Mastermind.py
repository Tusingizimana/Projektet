
# coding: latin-1
''' This is how this programm works, as a player you are going to start the game by guessing a four digit 
    optional code.The user will inspect the guessed code to examine if there be any of the elements in it
    that are also found  in the correct code, and if there be any, the user has to see if it is found in the right 
    position and print + in the position of that correct element, otherwise the user prints out blank,
   however if the guessed code contions any element it print - in the correct position of that element 
   that is found in the code but allocated in an incorrect position. 
   And it upp to the play to found what that element must be'''

# Mastermind game 
import random 

def showhelp ():
 print ('''To win the game you have to have less than 4 guesses.
 If you have played 4 times and still haven´t found out which  is the correct code,  
 You will be asked if you want to continue or lose the game
 If you choose to continue, you are given 2 more chances or else the compture wins by showing the correct code.''')


  
  
print("Welcome to mastermind")
answer=input("do you want to see the meny instructions first (y/n)? ")
if answer=='y':
 showhelp()
 
 
code="" 

for k in range ( 0,4):
 code+=str (random.randint(1,6))
 



print ("I have a code with four digits between 1 and 6")

answer=input("what is your guess: ")
counter=1
# loppen kommer att kora sa lange gissningen är fel
while answer !=code:
  lista =[" "," ", " ", " "]
  for index in range (0,4):
    ''' when the guessed code contains elements/index that are both in the same possition and are equal
        to the correct code, the print "+" for every element'''
    
    if answer[index]== code[index]:
      lista[index]= "+"
      
    else:
      for tecken in code:
        
     
        
        if answer[index]== tecken:
          lista[index] = "-"
  print(lista)
  
  answer=input("what is your guess: ") 
  
  #nu finns coden utanfor whileloppen
  # when the guess and the code are the same then user prints "correct"
if answer ==code:
    print("correct")
    
      
      
         
  

