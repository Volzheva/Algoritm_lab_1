import time
import os, psutil
import copy
import random
t_start = time.perf_counter()
process = psutil.Process(os.getpid())


def insertion_sort(arr): #функция, которая сортирует массив методом вставок (по возрастанию)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        smallest = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[smallest]:
                smallest = k
        arr[i], arr[smallest] = arr[smallest], arr[i]


def search_number(a, index, arr, arr_clone): #функция, которая ищет определенный элемент в первеночальном массиве и возвращает его место (индекс+1)
    for i in range(0, a):
        if arr_clone[i] == arr[index]:
            return i + 1


f = open("7_input.txt")
m = open("7_output.txt", "w")
num = int(f.readline())
string = f.readline()
#numbers = list(map(float, string.split()))
numbers = []
for i in range(0, 10000):
    numbers.append(random.randint(0, 100))
numbers_clone = copy.copy(numbers)
result = []

selection_sort(numbers)
print(numbers)
result.append(search_number(num, 0, numbers, numbers_clone)) #самый бедный
result.append(search_number(num, int((num-1)/2), numbers, numbers_clone)) #средний
result.append(search_number(num, -1, numbers, numbers_clone)) #самый богатый
m.write(" ".join(map(str, result)))

f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")