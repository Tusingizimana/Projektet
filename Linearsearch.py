#Linjär sökning 
# coding: utf-
''' ”Hur många jämförelser krävs för linjär sökning för
     en lista med 1000 element?”som en kommentar i din kod.
     Svar: Det krävs 1000 jämförelser i värsta fall eftersom programmet måste gå igenom alla 
     element tills det hittar den eftersökta elementet'''

def find(numbers, n):
    #numbers är namnet på listan (tåget) och n är den eftersökta talet
    position = -1
    '''att position = -1 innebär att det eftersökta 
       talet finns inte i den givna lista'''
    
    for index in range(0, len (numbers)):
        
        '''index är vagnens nummer och i varje vagn finns det en element.
           Detta innebär att när man vet vagnens nummber som är i sin tur index,
           kan därefter ta reda på vilken elemenetet som finns i den'''
        if  numbers[index] ==n:
            position = index
            '''position är -1 tills elementet med index innehåller det eftersökta tal och 
              då är index nummer och position samma'''
    return position
   
   
def runtestcode (numbers, n):
    print('-'*50)
    print("Min lista      :", numbers)
    print("Det eftersökta talet: ",n)
    position = find(numbers, n)
    if (position >=0):
        print(n, "finns på plats", position)
    else:
        print(n, "finns inte i listen")
        
        
numbers = [1,2.3,4,5,6,7,8,9,10,120,340,450,987,350]
runtestcode(numbers,1)
runtestcode(numbers,9)
runtestcode(numbers,87)
