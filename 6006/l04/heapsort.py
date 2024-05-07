import sys, time
import numpy as np

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heap_sort(arr):
    start = time.time()
    N = len(arr)

    #build max heap
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)

    #swap max elements
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


    end = time.time()

    return arr, end - start

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
        print(f"# number to to sort: {arr_len}")

    vector = np.random.randint(min, max, arr_len).tolist()
    
    if(arr_len <= 20):
        print(f"Vector Created: {vector}")
    else:
        print(f"Vector Created")

    sorted_1, time_1 = heap_sort(vector.copy())

    if(arr_len <= 20):
        print(f"Heap sort: {sorted_1} Time: {time_1}")
    else:
        print(f"Heap sort time: {time_1}")
    

if __name__ == "__main__":
    main()

