a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20]

def binary_search(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] < key:
            l = mid + 1
        elif arr[mid] > key:
            r = mid - 1
        else:
            return mid
        
print(binary_search(a, 18))