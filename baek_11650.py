'''
n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))
for i in range(n-1,-1,-1):
    for j in range(0, i):
        if arr[j][0]>arr[j+1][0]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        elif arr[j][1]>arr[j+1][1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
'''
n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))
arr.sort()
for i in range(n):
    print(arr[i][0], arr[i][1])