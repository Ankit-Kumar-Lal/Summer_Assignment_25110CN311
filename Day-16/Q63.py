# Write a program to Find pair with given sum

# arr = [1, 4, 5, 6, 8, 2]
# target = 10

# found = False

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print("Pair found:", arr[i], arr[j])
#             found = True

# if found == False:
#     print("No pair found")

arr = [1, 4, 5, 6, 8, 2]
target = 10

# Count elements manually
n = 0
for x in arr:
    n = n + 1

# Find pairs
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            print("Pair found:", arr[i], arr[j])