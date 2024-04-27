def insert_into_sorted_array(arr, n):
    # Find the index where the number should be inserted
    index = 0
    while index < len(arr) and arr[index] < n:
        index += 1

    # Shift elements to the right to make space for the new number
    arr.append(0)  # Add a placeholder at the end
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]

    # Insert the new number at the appropriate index
    arr[index] = n

    return arr


sorted_array = [1, 3, 5, 7, 9]
n = 6
new_array = insert_into_sorted_array(sorted_array, n)
print(f"Sorted Array: {new_array}")
print(len(sorted_array))
