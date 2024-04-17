def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    def recursive_search(low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if arr[mid] == target:
            print(f"Element {target} found at index {mid}.")
            return mid
        elif arr[mid] > target:
            return recursive_search(low, mid - 1)
        else:
            return recursive_search(mid + 1, high)

    return recursive_search(low, high)


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 5

result = binary_search(arr, target)
