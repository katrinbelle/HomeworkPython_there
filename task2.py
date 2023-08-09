# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
import random
def SignReplacement (listSign,indexN):
    if indexN==len(listSign)-1:
        return listSign[len(listSign)-2]
    else:
        return listSign[listSign.index(indexN)+1]
def Check(listRanom,number, indexN):
    if len(listRanom)>1:
        return SignReplacement(listRanom,indexN)
    else: 
         return(listRanom[listRanom.index(number)])
numberOfUser=int(input("Введите количество элементов в массиве->    "))
listOfRanom=[]
for i in range(numberOfUser):
    listOfRanom.append(random.randint(1,numberOfUser))
print(*listOfRanom)
numberX=int(input("Введите число для поиска->  "))
listOfRanom.sort()
counNumber=listOfRanom.count(numberX)
indexNumber=listOfRanom.index(numberX)

if counNumber==1:
    print(SignReplacement(listOfRanom, indexNumber))
else:
    for i in range(counNumber-1):
         listOfRanom.pop(listOfRanom.index(numberX))
    print( Check(listOfRanom,indexNumber,indexNumber))