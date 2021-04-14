# coding: utf-8
'''

print ( "Hello W")
name= input ("vad heter du: ")
print (name, "är bäst")

print (123+345-456)
print (12+ 3*5)
print (7**6)
print ((6+8)*(2+5))

Mile=int(input("ange antal mile: "))
Meter= 1609.344 *Mile
print("Meter: ",Meter)


#!/usr/bin/env python
# coding: utf-8
x=10
y=20
print (x<10)
print (y>2*x)
print (y==10 and y==15)
print (y==10 and y>15)
print (y==10 or y==15)


väder=input("Vad är väderet idag? ")
idag=input("Regnar det (j/n): ")
print(idag)
print (väder)
if idag=="j" or idag=="J":
    print ("Tag paraply")
    
    
Mående=input("hur mår du? ")
Fråga=input("Är du glad (j/n): ")

if Fråga=="j":
  print("Härligt")
elif Fråga=="n":
  print("sad")
else:
  print("tråkigt")

print("1 skapa nytt")
print("2 Öpnna")
print ("3 skriv ut")
print("4 avsluta")
Ans=input("vad vill du göra: ")
if Ans== "1" :
  print("skapa nytt")
elif Ans=="3":
  print("skriv ut")
else:
  print("avsluta or öppna")
  '''


''' uppgift 15#
 t=input("Täljaren:")
t=int(t)
n=input("Nämnaren:")
n=int(n)
if n==0 :
  print("inte okej")
else:
  print("kvoten blir: ",t/n)
  

#while loop uppgifter

n=1
while n<=20:
    print("hej")
    n=n+1
n=1
while n<=31:
    print(n)
    n=n+1
 '''

'''
svar=input("vill du avsluta (j/n)? ")
while svar=="n": 
    svar=input("vill du avsluta (j/n)? ")
'''

'''Nr 28 Gissa talet
import random 
x=random.randint(1,1000)
#print(x)
print ("jag har ett tal mellan 1 0ch 1000")
svar=input("vad gissar du")
svar=int(svar)
counter=1
while svar !=x:
  if svar <x:
    print("mitt tal är högre")
  if svar > x:
    print("mitt tal är längre")
  svar=input("vad gissar du")
  svar=int(svar)
  counter+=1
print("rätt gissat! du klarade det på",counter, "gissningar")
'''

''' Nr 
for i in range(0,10):
    print(i)

    
    x=0
    while x<20:
        print(x)
        x+=1

'''

''' Nr 
x=0
while x<1000:
    print(x)
    x+=100
'''

''' Nr 33
for i in range(1,100,2):
    print(i)
'''

'''Nr 34

m=input("Ange tabel :")
m=int(m)
for i in range(1,11,1):
    print(i,"*",m, "=" ,i*m)
'''

''' Nr 35
for y in range(1,8):
    for x in range(0,y):
        print('*', end=' ')
    print()
    
'''


''' Nr 36
M=[" januari", "februari", "mars", "april", "maj", "juni", "juli", "augusti", "september", "oktober", "november", "december"]  
x=input(" skriv ut ett tal mellan 1 och 12 ")
x=int(x)
x=x-1
print("din månad är",M[x])
'''

''' Nr 37
z= [17,4,6,11,43,32,-9]
minsta = 1000
print ("skriv ut längsta tal") 
for t in z:
    if t< minsta:
        minsta= t
print ("minsta: ",minsta)

'''
''' Nr38
z= [-9,4,6,11,43,32,17]
minsta = 1000
print ("skriv ut längsta tal") 
for t in z:
    if t< minsta:
        minsta= t
print ("minsta: ",minsta)
'''

''' Nr39
sum=input("hur många tal har jag: ,")
sum=int(sum)
lista=[]
for x in range (sum):
    z=input("ange tal: ")
    z=int(z)
    lista.append(z)
print ("detta är min lista", lista)

sum = 0
for z in lista:
    sum += z
print("summan är :", sum)

'''
'''41. Skriv ett program som frågar efter en sträng (Exempel ”bananen Kalle”) . Programmet ska
sedan skriva ut samma text, fast…
a. …med stor bokstav i början (Ex: ”Bananen kalle”)
b. …med enbart små bokstäver (Ex: ”bananen kalle”)
c. …med enbart stora bokstäver (Ex: ”BANANEN KALLE”)
d. …centrerat på 30 tecken (Ex: ” bananen Kalle ”)
e. …högerjusterat på 30 tecken (Ex: ” bananen Kalle”)
f. …tar bort alla mellanslag i början och slutet av en mening.
(Ex. Exempel ” knas ”, ger utskriften ”knas”)
LÄTT LAGOM SVÅRT

''' 
x=input(" skriv en text: ")

print (x)

print(x.capitalize())


