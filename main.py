import random

from cmp import *

cnt_processors = int(input("Enter count of processors: "))
a = int(input("Enter value from: "))
b = int(input("Enter value to: "))

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

_max = sum_of_processor(arr_processors_random[0])
for i in range(len(arr_processors_random)):
    if sum_of_processor(arr_processors_random[i]) > _max:
        _max = sum_of_processor(arr_processors_random[i])
    print(f"p{i + 1} =", arr_processors_random[i], "Sum:", sum_of_processor(arr_processors_random[i]))
print("Max:", _max)

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

_max = sum_of_processor(arr_processors_sort_down[0])
for i in range(len(arr_processors_sort_down)):
    if sum_of_processor(arr_processors_sort_down[i]) > _max:
        _max = sum_of_processor(arr_processors_sort_down[i])
    print(f"p{i + 1} =", arr_processors_sort_down[i], "Sum:", sum_of_processor(arr_processors_sort_down[i]))
print("Max:", _max)

print()
print("################################################")
print()

is_even = False

while not is_even:
    if cnt_processors % 2 == 0:
        is_even = True
    else:
        print("Enter the even count")
        cnt_processors = int(input("Enter count of processors: "))

print("T:", T)

for i in range(len(arr_processors_sort_down)):
    print(f"p{i + 1} =", arr_processors_sort_down[i])

arr_subprocesses = []

for i in range(cnt_processors * 2):
    arr_subprocesses.append([])

start_index = 0
end = start_index + cnt_processors // 2
for i in range(len(arr_processors_sort_down)):
    for k in range(len(arr_processors_sort_down[i])):
        if end > len(arr_subprocesses):
            break
        index = minimal_load_processor_hdmt(arr_subprocesses, start_index,
                                            end)
        arr_subprocesses[index].append(arr_processors_sort_down[i][k])
    start_index += cnt_processors // 2
    end = start_index + cnt_processors // 2

print()
print("################################################")
print()

for i in range(len(arr_subprocesses)):
    print(f"p{i + 1} =", arr_subprocesses[i], "Sum:", sum_of_processor(arr_subprocesses[i]))
