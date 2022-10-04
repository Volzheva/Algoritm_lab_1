import time
import os, psutil
t_start = time.perf_counter()
process = psutil.Process(os.getpid())


def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]


f = open("6_input.txt")
m = open("6_output.txt", "w")
num = int(f.readline())
string = f.readline()
numbers = list(map(int, string.split()))

bubble_sort(numbers)
m.write(" ".join(map(str, numbers)))
f.close()
m.close()


print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")