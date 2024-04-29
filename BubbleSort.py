def bubble_sort(arr) -> list:
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n -i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
        print(arr)
        
arr = [4,567,3,114,62,6,3,1]
bubble_sort(arr)
