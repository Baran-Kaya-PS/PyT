list = []
for x in range(3):
    temp_list = []
    for y in range(5):
        temp_list.append((y+1)*(x+1))
    list.append(temp_list)

print(list)

copy_list = list[0].copy() # deep copy
copy_list[0] = 52
print(copy_list)
print(list[0])

print(" reset ---------------")
copy_list = list[1] # same ptr
copy_list[1] = 32

print(copy_list)

print(list[1])