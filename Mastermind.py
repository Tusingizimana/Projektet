

# coding: utf-8
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
# över 
while answer !=code:
  lista =[" "," ", " ", " "]
  for index in range (0,4):
    
    if answer[index]== code[index]:
      lista[index]= "+"
      print(lista)
    else:
      for tecken in code:
        print( tecken)
        
        print(answer[index])
        
        if answer[index]== tecken:
          lista[index] = "-"
          print(lista)
  
  answer=input("what is your guess: ") 
  
  #nu finns coden utanfor whileloppen
if answer ==code:
    print("correct")
    
      
      
         
  

