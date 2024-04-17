def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            print(f"Element {target} found at index {mid}.")
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 5

result = binary_search(arr, target)
