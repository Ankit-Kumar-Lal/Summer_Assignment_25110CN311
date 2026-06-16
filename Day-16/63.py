# Write a program to Find pair with given sum

arr = [1, 4, 5, 6, 8, 2]
s = 10   #target to find pair of sum 10

n = 0
for x in arr:
    n = n + 1

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == s:
            print(arr[i], arr[j])