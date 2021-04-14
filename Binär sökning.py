# coding: utf-8
# Binär sökning
 
def befind(numbers, n):
    #numbers är namnet på listan (tåget) och n är den eftersökta talet
    N = len(numbers)
    # N är längden på elementet in listan
    first= 0
    # att first är lika med noll innebär att första talet position är noll
    last= N-1
    # längden på listan minus 1 är lika med sista elements position
    
while first<=last:
        middle = (first + last)//2
if  numbers[middle] ==n:
    return middle
   
        #Om det eftersökta talet är lika med median av första och sista talet, då returns den till middle
elif numbers [middle]<n:
            first= middle + 1
            '''Om det eftersökta talet är större än mitt talet, dår betyder det att den finns i övre halven
               och att hitta den blir middle +1 och man tar median på den och gör samma saker till man hittar den'''
elif numbers[middle]>n:
            last= middle - 1
            ''' Om det eftersökta talet mindre än mitt talet, dår betyder det att den finns i nedre halven
               och att hitta den blir middle -1 och man tar median på den och gör samma saker 
               tills man hittar den eftersökta talet'''
            return -1
'''när programmet har kört alla dessa processer som jag skrev ovan och visar att det eftersökta talet 
   finns inte med, då returneras -1 att visa att talet finns inte med i listan'''
   
   
def runtestcode (numbers, n):
    print('-'*50)
    print("Min lista      :", numbers)
    print("Det eftersökta talet: ",n)
    position = befind(numbers, n)
    if (position >=0):
        print(n, "finns på plats", position)
    else:
        print(n, "finns inte i listen")
        
        
numbers = [1,2.3,4,5,6,7,8,9,10,120,340,450,987,350]
runtestcode(numbers,1)
runtestcode(numbers,9)
runtestcode(numbers,87)



