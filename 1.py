import time
import os, psutil
import random
t_start = time.perf_counter()
process = psutil.Process(os.getpid())


def test(a, b):
    k = []
    for i in range(0, a):
        k.append(random.randint(-b, b))
    return k


def test_test(arr):
    k = False
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


f = open("1_input.txt", "w")
m = open("1_output.txt", "w")
"""num = int(f.readline())
string = f.readline()
numbers = list(map(int, string.split()))

insertion_sort(numbers)
m.write(" ".join(map(str, numbers)))"""

#код для тестов
f.write("1000\n")
numbers = test(1000, 1000000000)
f.write(" ".join(map(str, numbers)))
insertion_sort(numbers)
if test_test(numbers):
    m.write(" ".join(map(str, numbers)))

f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")