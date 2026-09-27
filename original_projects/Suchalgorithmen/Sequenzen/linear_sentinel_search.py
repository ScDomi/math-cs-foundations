a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def linear_sentinel_search(arr, key):
    last = arr[len(arr)-1]
    arr[len(arr)-1] = key
    i = 0
    while arr[i] != key:
        i += 1
    if i < len(arr)-1 or last == key:
        return i
    else:
        return None

print(linear_sentinel_search(a, 9))