def binary_search(sequence, target):
    first, last = 0, len(sequence) - 1
    while first <= last:
        mid = (first + last) // 2
        if sequence[mid] < target:
            first = mid + 1
        elif target < sequence[mid]:
            last = mid - 1
        else:
            return mid
    return None
