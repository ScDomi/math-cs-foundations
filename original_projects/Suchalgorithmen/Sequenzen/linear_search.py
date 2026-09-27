a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

print(linear_search(a, 7))


