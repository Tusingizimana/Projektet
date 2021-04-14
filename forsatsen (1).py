#!/usr/bin/env python
# coding: utf-8

i = 0
while i < 5:
    print(i)
    i = i + 1

print()

for i in (0, 1, 2, 3, 4):
    print(i)

print()

# OBS!! range(5) <=> range(0,5) <=> range(0,5,1)
#
#       range(från_variabel, till_variabel, steglängd)

for i in range(0,5):
    print(i)

print()




for i in range(1,10,1):
    print(i)

print()

for j in range(1,20,2):
    print(j)

print()

for j in range(20,1,-2):
    print(j)

print()

for i in (7, 4, -1, 2, 10):
    print(i)

print()

for a in ['Adam', 'Bertil', 'C', 123, 9.97]:
    print(a)

print()

for tecken in "Cesar":
    print(tecken)

print()    

for tecken in "Cesar":
    print(tecken, end='')

print()    

numbers = [2,64,1,46,32]
sum = 0
for t in numbers:
    sum += t

print("Detta är dina tal: ", numbers)
print("Detta är summan av dina tal: ",sum)



for y in range(1,5):
    for x in range(1,10):
        print('*', end=' ')
    print()