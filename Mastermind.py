
# coding: latin-1
''' This is how this programm works, as a player you are going to start the game by guessing a four digit 
    optional code.The user will inspect the guessed code to examine if there be any of the elements in it
    that are also found  in the correct code, and if there be any, the user has to see if it is found in the right 
    position and print + in the position of that correct element, otherwise the user prints out blank,
    however if the guessed code contians any element it print - in the correct position of that element 
    that is found in the code but allocated in an incorrect position. 
    And it is up to the play to found what that element must be'''

# Mastermind game 
import random 

def showhelp ():
 print ('''To win the game you have to have less than 4 guesses.
           If you have played 4 times and still haven´t found out which is the correct code,  
           You will be asked if you want to continue or lose the game
           If you choose to continue, you are given 2 more chances or else the compture 
           wins by showing the correct code.''')
 
def correctdigitsincode(answer):
   feedback=True 
   feedback=feedback and answer.isdigit()
   for character in answer:
    feedback=feedback and int(character) >0 and int(character)<7
   return feedback
  
def getanswer():
 answer=input("what is your guess: ") 
 while len(answer)!=4 or not correctdigitsincode(answer):
  answer=input("sorry the guess needs to be exactly 4 digits and only numbers between 1 and 6, try again: ")   
 
 return answer

print("Welcome to mastermind")
answer=input("do you want to see the meny instructions first (y/n)? ")
answer=answer.strip()
if answer=='y':
 showhelp()
 
 
code="" 

for k in range ( 0,4):
 code+=str (random.randint(1,6))
 
 
print ("I have a code with four digits between 1 and 6")

answer=getanswer()

counter=1

# The lopp will continue to play as long is the correct guess is not found
while answer !=code:
  if counter==4:
   response=input("you haven´t guessed a correct code yet, but you have 2 more chances do you want to continue (y/n)? ")
   response=response.strip()
   if not response=='y':
    print(" thank you for your effort, howewer the code remains hidden......")  
    exit(0)
  elif counter==6:
   print(" thank you for your effort, sorry you didn´t make it this time, here comes the correct code.")  
   print("code:",code)
   exit(0)   
  
   
  lista =[" "," ", " ", " "]
  for index in range (0,4):
    ''' when the guessed code contains elements/index that are both in the same possition and are equal
        to the correct code, the print "+" for every element, but the user prints "-" 
        for every element that is found in the code and but in the wrong position  '''
    
    if answer[index]== code[index]:
      lista[index]= "+"
      
    else:
      for tecken in code:
      
        
        if answer[index]== tecken:
          lista[index] = "-"
  print(lista)
  
  answer=getanswer()
  
  counter=counter+1
  


  # Now the code is find outside the whileloppen
  # when the guess and the code are the same then user prints "correct"
if answer ==code:
    print("correct")
    print (counter)
    
if counter <=2:
 print("you´re on fire")
 
elif counter<=3:
  print (" you´re brilliant :")
else:
 print(" you made it:")
 
    
      
      
         
  

