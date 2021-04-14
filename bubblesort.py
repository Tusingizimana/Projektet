#coding: utf-8
#Bubble sort
'''Bubble Sort is a simple algorithm and it is used to sort a given set of
   n elements provided in form of an array with n number of elements. 
   Bubble Sort compares all the element one by one and sort them based on their values.
   If the array has to be sorted with ascendning order, it compares the first element with the second
   and swaps their position if the first is greater than the second, 
   then it continues to compare the second with the third and so on, untill all the array is sorted'''

def bubbelsort(numbers):
    N= len (numbers)
    for j in range(0, len (numbers)):
        for k in range( 1, len (numbers)):
            if (numbers [k] < numbers [k-1]):
                ''' If item K is lesser than the previous iterm, that is to say that item located infront of k,
                    I create a temporally variable where K can placed as that larger item moves to k´s position,
                    after that K fills that place of the larger one and thus swaping position, according to the 
                    items values. From smaller to largest '''
                temp= numbers[k]
                numbers[k] = numbers[k-1]
                numbers[k-1]= temp
                
    return numbers

def runtestcode(numbers):
    '''Din testkod'''

    print('-'*50)
    print("Din lista       : ", numbers)
    sortedlist = bubbelsort(numbers)
    print("Din lista sorterad: ", sortedlist)
    
    
runtestcode([5,3,2,4,1,7,9])
runtestcode([])
runtestcode([1,2,3])