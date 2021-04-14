#!/usr/bin/env python
# coding: utf-8

a=6
b=10
print(a<b)
print(a>b)

tf = a<=b
print(tf)

print(b==10)
print(b!=10)

if a==5:
    print("Wow!!")
else:
    print("Nope. Inte lika med fem...")
    
# Först några variabler att jobba med
x = 7
y = 3
z = 7

# enkla jämförelser
# kolla om "mindre än" samt "större än"
if y < x:
    print("y är mindre än x")
if x < y:
    print("x är mindre än y")
    
# avgör "mindre eller lika med"
if y <= z:
    print("y är mindre eller lika med z")
    
# Vi kan också kombinera uttryck 
if a==5 and b==10:
    print("Hej!")
    
year=int(input("Vilket år är du född? "))
birthday=input("Har du fyllt år i år (j/n)? ")
if birthday=="j" or birthday=="J":
    age=2018-year
else:
    age=2018-year-1
print("Du är",age,"år gammal")


# "nästla" if-satserna enligt
x = 7
y = 3
z = 7
if z == x:
    print("z är lika med x")
    print("och vi kan skriva")
    print("flera rader")
    if z > y: #Här sätter vi en if-sats INUTI en if-sats, dvs en "nästlad if-sats" 
        print("Dessutom är z större än y")
if z!= 8:
    print("z är INTE lika med 8")
        
'''    
print("1=Röd")
print("2=Grön")
print("3=Blå")
print("4=Gul")
val=int(input("Välj en färg (1-4): "))
if val==1:
    print("Rött är sött")
elif val==2:
    print("Grönt är skönt")
elif val==3:
    print("Blått är flott")
else:
    print("Gult är fult")
   ''' 
    
#Anta att vi har ett betyg som är direkt mappat mot poäng.
# enligt nedan

p = int(input("Ange antal poäng på provet (0-100): "))
if p >= 90:
    print("Betyg = A") 
else:
    # Hit kommer vi bara om poängen är mindre än 90    
    if p >= 80:
        print("Betyg = B")
    else:
        # Hit kommer vi bara om poängen är mindre än 80    
        if p >= 70:
            print("Betyg = C")
        else:
            # Hit kommer vi bara om poängen är mindre än 70    
            if p >= 60:
                print("Betyg = D")
            else:
                # Hit kommer vi bara om poängen är mindre än 60    
                if p >= 50:
                    print("Betyg = E")
                else:
                    # Hit kommer vi bara om poängen är mindre än 50    
                    print("Betyg = F")
                    
# Koden ovan blir svår att läsa, så då är det lättare att använda "elif" , vilket betyder "else if"
# se nedan kod som gör exakt samma sak som ovan kod:

p = int(input("Ange antal poäng på provet (0-100): "))
if p >= 90:
    print("Betyg = A") 
elif p >= 80:
    print("Betyg = B")
elif p >= 70:
    print("Betyg = C")
elif p >= 60:
    print("Betyg = D")
elif p >= 50:
    print("Betyg = E")
else:
    print("Betyg = F")


# Nedan kod fungerar INTE. Skilj på = och ==
if z = y:
    print("Hm... ")
