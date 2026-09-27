a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def exponential_search(arr, key):
    n = len(arr)
    i = 1
    while i < n:
        i *= 2
        l = i // 2 
        r = min(i, n-1)
        while l <= r:
            mid = (l+r)//2
            if arr[mid] < key:
                l = mid + 1
            elif arr[mid] > key:
                r = mid -1
            else:
                return mid


            
print(exponential_search(a, 0))