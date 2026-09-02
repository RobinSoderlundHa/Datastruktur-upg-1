import random
import time
import copy

# ---------------------------------------------------------
# 1. Bubble Sort (O(n^2) time complexity)
# ---------------------------------------------------------
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# ---------------------------------------------------------
# 2. Insertion Sort (O(n^2) time complexity)
# ---------------------------------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# ---------------------------------------------------------
# 3. Quick Sort (O(n log n) average time complexity)
# ---------------------------------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Pick a pivot (middle element)
    pivot = arr[len(arr) // 2]
    
    # Partition the array into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# ---------------------------------------------------------
# 4. Merge Sort (O(n log n) time complexity)
# ---------------------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the two sorted halves
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ---------------------------------------------------------
# 5. Python's Built-in Sort (Timsort - O(n log n))
# ---------------------------------------------------------
def builtin_sort(arr):
    # sorted() returns a new sorted list, leaving the original intact
    return sorted(arr)


# =========================================================
# Testing and Benchmarking
# =========================================================
if __name__ == "__main__":
    sizes = [100, 1000, 10000]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
        "Built-in Sort": builtin_sort
    }

    for size in sizes:
        print(f"\n--- Sorting List of {size} Elements ---")
        # Generate a random list of 'size' elements between 1 and 100,000
        original_data = [random.randint(1, 100000) for _ in range(size)]
        
        for algo_name, algo_func in algorithms.items():
            # Create a fresh copy of the data for each algorithm so they all start unsorted
            data_copy = copy.deepcopy(original_data)
            
            start_time = time.time()
            algo_func(data_copy)
            end_time = time.time()
            
            duration = end_time - start_time
            print(f"{algo_name:<16}: {duration:.5f} seconds")