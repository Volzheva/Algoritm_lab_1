import time
import os, psutil
import copy, random
t_start = time.perf_counter()
process = psutil.Process(os.getpid())


def test(a, b):
    k = []
    for i in range(0, a):
        k.append(random.randint(-b, b))
    return k


def insertion_sort(arr1, arr2):
    arr2[0] = 0 #первый элемент(с индексом 0) остается на месте
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i-1
        while j >= 0 and key < arr1[j]:
            arr1[j+1] = arr1[j]
            j -= 1
        arr1[j+1] = key
        arr2[i] = j + 1 #заносим индекс, куда был переставлен соответсвующий элемент


f = open("2_input.txt")
m = open("2_output.txt", "w")
num = int(f.readline())
string = f.readline()
numbers = list(map(int, string.split()))
numbers_copy = copy.copy(numbers)
insertion_sort(numbers, numbers_copy)
m.write(" ".join(map(str, numbers_copy)))
m.write('\n')
m.write(" ".join(map(str, numbers)))
f.close()
m.close()


print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")