a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def interpolation_search(arr, key):
    l = 0
    r = len(arr)-1
    while l <= r and key >= arr[l] and key <= arr[r]:
        pos = l + (key-arr[l]*(r-l)//(arr[r]-arr[l]))
        if arr[pos] < key:
            l = pos + 1
        elif arr[pos] > key:
            r = pos - 1
        else: 
            return pos

print(interpolation_search(a, 12))
