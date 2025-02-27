def find_min_max(arr, left, right):
    if left == right:
        return arr[left], arr[left]
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    mid = (left + right) // 2
    left_min, left_max = find_min_max(arr, left, mid)
    right_min, right_max = find_min_max(arr, mid + 1, right)
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)
    return overall_min, overall_max
arr = [3, 5, 1, 2, 4, 8, 7, 6]
min_value, max_value = find_min_max(arr, 0, len(arr) - 1)
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
