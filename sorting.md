<h1>Sorting coordinate</h1>
<hr>
<h2>Problem</h2><br>
There are N points above a 2-dimensional plane. Arrange coordinates in the order where x-coordinate increases. If there are points whose x-coordinate is the same for each other, arrange them in the order where y-coordinate increases. Write pseudo-code for solution.
<hr>
<h2>Algorithm hint</h2><br>
Use sorting algorithm. ex) Bubble sort, Selection sort, Merge sort, Quick sort, etc...
<hr>
Pseudo-code example (Bubble sort)

'''
    for i=(length_of_array-1) downto 1
        for j=0 to i-1
            if array[j].x > array[j+1].x then
                swap(array[j], array[j+1])
            else if array[j].y > array[j+1].y then
                swap(array[j], array[j+1])
        end of j loop
    end of i loop
'''

출처: Baekjoon Online judge 11650번 문제 https://www.acmicpc.net/problem/11650


Python source code example

'''python
    for i in range(n-1,-1,-1):
    for j in range(0, i):
        if arr[j][0]>arr[j+1][0]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        elif arr[j][1]>arr[j+1][1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
'''
