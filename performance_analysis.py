import time
import random
from matplotlib import pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    return time.time() - start

if __name__ == "__main__":
    sizes = [10, 100, 500, 1000, 2000, 5000]
    quick_times = []
    insertion_times = []

    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        quick_time = measure_time(quicksort, arr)
        quick_times.append(quick_time)
        insertion_time = measure_time(insertion_sort, arr)
        insertion_times.append(insertion_time)

        print(f"Размер: {size:4d} | QuickSort: {quick_time:.6f} сек | Insertion: {insertion_time:.6f} сек")
