import sys, time
import numpy as np

def find_smallest(arr):
    min = arr[0]
    min_ix = 0
    for i in range(0,len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_ix = i

    return min_ix


def selection_sort(arr):
    if(len(arr) < 2):
        return arr, 0
    
    arr2 = []
    start = time.time()
    for i in range(0,len(arr)):
        min_ix = find_smallest(arr)
        arr2.append( arr.pop(min_ix))
        
    end = time.time()
    return arr2, (end - start)

def insertion_sort(arr):
    if(len(arr) < 2):
        return arr, 0
    
    start = time.time()
    for i in range(1,len(arr)):
        j = i
        while(j > 0 and arr[j-1] > arr[j]):
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j = j - 1
        
    end = time.time()
    return arr, (end - start)

def merge(start, l, r):
    ml = len(l) + len(r)
    K = [0] * ml

    i = 0
    j = 0
    k = 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            K[k] = l[i]
            i = i + 1
        else:
            K[k] = r[j]
            j = j + 1
        k = k + 1

    while i < len(l):
        K[k] = l[i]
        i = i + 1
        k = k + 1

    while j < len(r):
        K[k] = r[j]
        j = j + 1
        k = k + 1

    return K
    

def divide(arr, start, end):
    if start >= end:
        return [arr[start]]
    
    m = start + (end - start)//2
    l = divide(arr, start, m)
    r = divide(arr, m + 1, end)
    return merge(start, l, r)


def merge_sort(arr):
    if(len(arr) < 2):
        return arr, 0
    
    start = time.time()
    arr = divide(arr, 0, len(arr) - 1)
    end = time.time()
    return arr, (end - start)

def main():
    arr_len = 4000
    min = -500000
    max = 500000
    if len(sys.argv) != 4:
        print(f"Using default # of numbers for sorting: {arr_len}")
    else:
        arr_len = int(sys.argv[1])
        min = int(sys.argv[2])
        max = int(sys.argv[3])
        print(f"# numberto to sort: {arr_len}")

    vector = np.random.randint(min, max, arr_len).tolist()

    print(f"Vector Created")

    sorted_1, time_1 = selection_sort(vector.copy())
    sorted_2, time_2 = insertion_sort(vector.copy())
    sorted_3, time_3 = merge_sort(vector.copy())

    if(arr_len <= 20):
        print(f"Selection sort: {sorted_1} Time: {time_1}")
        print(f"Insertion sort: {sorted_2} Time: {time_2}")
        print(f"Merge sort: {sorted_3} Time: {time_3}")
    else:
        print(f"Selection sort time: {time_1}")
        print(f"Insertion sort time: {time_2}")
        print(f"Merge sort time: {time_3}")
    

if __name__ == "__main__":
    main()
    #import profile
    #profile.run("main()")
