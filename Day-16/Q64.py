# Write a program to Remove duplicates from array

arr = [1, 2, 2, 3, 4, 3, 5]

for i in range(len(arr)):
    duplicate = False

    for j in range(i):
        if arr[i] == arr[j]:
            duplicate = True
            break

    if duplicate == False:
        print(arr[i], end=" ")