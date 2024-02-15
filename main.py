import random

from cmp import *
print(30**30)

cnt_processors = int(input("Enter count of processors: "))
a = int(input("Enter value from: "))
b = int(input("Enter value to: "))

rows = random.randint(a, b)
columns = 2

T = []

for i in range(rows):
    T.append(random.randint(20, 35))

print()
print("################################################")
print()


print("T:", T)

arr_processors_random = []

for i in range(cnt_processors):
    arr_processors_random.append([])

for i in range(len(T)):
    minimal_load_processor_value = minimal_load_processor(arr_processors_random)
    for j in range(len(arr_processors_random)):
        if sum(arr_processors_random[j]) == minimal_load_processor_value:
            arr_processors_random[j].append(T[i])
            break

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
    minimal_load_processor_value = minimal_load_processor(arr_processors_sort_up)
    for j in range(len(arr_processors_sort_up)):
        if sum(arr_processors_sort_up[j]) == minimal_load_processor_value:
            arr_processors_sort_up[j].append(T[i])
            break

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
    minimal_load_processor_value = minimal_load_processor(arr_processors_sort_down)
    for j in range(len(arr_processors_sort_down)):
        if sum(arr_processors_sort_down[j]) == minimal_load_processor_value:
            arr_processors_sort_down[j].append(T[i])
            break

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
    for j in range(cnt_processors // 2):
        

for i in range(len(arr_subprocesses)):
    print(f"p{i + 1} =", arr_subprocesses[i])

