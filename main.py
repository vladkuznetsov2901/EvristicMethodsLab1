import random

from cmp import *

cnt_processors = int(input("Enter count of processors: "))
a = int(input("Enter value from: "))
b = int(input("Enter value to: "))
N = int(input("Enter the count of columns: "))

rows = random.randint(a, b)
columns = 2

T = []

for i in range(rows):
    T.append(random.randint(a, b))

print()
print("################################################")
print()

print("T:", T)

arr_processors_random = []

for i in range(cnt_processors):
    arr_processors_random.append([])

for i in range(len(T)):
    index = minimal_load_processor(arr_processors_random)
    arr_processors_random[index].append(T[i])

for i in range(len(arr_processors_random)):
    print(f"p{i + 1} =", arr_processors_random[i])

T.sort()

print()
print("################################################")
print()

print("T:", T)

arr_processors_sort_up = []

for i in range(cnt_processors):
    arr_processors_sort_up.append([])

for i in range(len(T)):
    index = minimal_load_processor(arr_processors_sort_up)
    arr_processors_sort_up[index].append(T[i])

_max = sum_of_processor(arr_processors_sort_up[0])
for i in range(len(arr_processors_sort_up)):
    if sum_of_processor(arr_processors_sort_up[i]) > _max:
        _max = sum_of_processor(arr_processors_sort_up[i])
    print(f"p{i + 1} =", arr_processors_sort_up[i], "Sum:", sum_of_processor(arr_processors_sort_up[i]))
print("Max:", _max)

T.sort(reverse=True)

print()
print("################################################")
print()

print("T:", T)

arr_processors_sort_down = []

for i in range(cnt_processors):
    arr_processors_sort_down.append([])

for i in range(len(T)):
    index = minimal_load_processor(arr_processors_sort_down)
    arr_processors_sort_down[index].append(T[i])

for i in range(len(arr_processors_sort_down)):
    print(f"p{i + 1} =", arr_processors_sort_down[i])

print()
print("################################################")
print()

print("T:", T)

arr_subprocesses = []

for i in range(cnt_processors * 2):
    arr_subprocesses.append([])

for i in range(len(T)):
    minimal_load_processor_value = minimal_load_processor(arr_subprocesses)

for i in range(len(arr_subprocesses)):
    print(f"p{i + 1} =", arr_subprocesses[i])
