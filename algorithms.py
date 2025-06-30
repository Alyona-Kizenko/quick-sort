
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))

def find_max(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])
    return max(left_max, right_max)
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(nums)
print(find_max(nums))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

unsorted = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quick_sort(unsorted)
print(unsorted)
print(sorted_list)
