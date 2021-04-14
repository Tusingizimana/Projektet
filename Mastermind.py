
# coding: latin-1

# Mastermind game 
import random 

def correctguess(answer):
  return 3
  
print("Welcome to mastermind")
#Code=random.randint(1,6)
code= "2354"

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
      print(lista)
    else:
      for tecken in code:
        print( tecken)
        
        print(answer[index])
        ''' when the guessed answer has index that are found in the code but not the correct positiion,
            then I print "-" '''
        
        if answer[index]== tecken:
          lista[index] = "-"
          print(lista)
  
  answer=input("what is your guess: ") 
  
  #nu finns coden utanfor whileloppen
  # when the guess and the code are the same then user prints "correct"
if answer ==code:
    print("correct")
    
      
      
         
  

