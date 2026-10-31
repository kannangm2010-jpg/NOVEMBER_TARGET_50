def binary_search(arr, target):
    left = 0
    right=len(arr)-1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if the target is at the middle pointer
        if arr[mid] == target:
            return mid
            
        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If the target is smaller, ignore the right half
        else:
            right = mid - 1
            
    # Target was not found in the list
    return -1

# Example usage:
numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23

result = binary_search(numbers, target_value)
print(f"Element found at index: {result}")
