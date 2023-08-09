# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
import random
listRandom=[]
numberOfUser=int(input("Введите количество элементов в массиве-> "))
for i in range(numberOfUser):
    listRandom.append(random.randint(0,numberOfUser))
print(*listRandom)
searchNumber=int(input("Введите число, которое надо найти-> "))
count=0
for i in range(numberOfUser):
    if listRandom[i]==searchNumber:
        count=count+1
print(f"Количество {searchNumber} в массиве -> {count}")

