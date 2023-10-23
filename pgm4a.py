import random

# Merge Sort Implementation
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        # Merge the sorted halves back together
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in left_half and right_half
        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

    return lst

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate a random list of numbers
my_list = [random.randint(0, 999) for _ in range(10)]

# Display the unsorted list
print("Unsorted List:")
print(my_list)

# Sort the list using Insertion Sort
insertion_sort(my_list)
print("\nSorting using Insertion Sort:")
print(my_list)

# Generate another random list of numbers
my_list = [random.randint(0, 999) for _ in range(10)]

# Display the unsorted list
print("\nUnsorted List:")
print(my_list)

# Sort the list using Merge Sort
merge_sort(my_list)
print("\nSorting using Merge Sort:")
print(my_list)

