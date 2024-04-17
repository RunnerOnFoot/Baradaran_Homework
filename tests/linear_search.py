def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


arr = [3, 6, 2, 8, 1, 5]
target = 2
index = linear_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
