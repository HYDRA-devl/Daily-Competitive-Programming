def two_sum(nums, target):
    index_map = {}  # Store number and its index
    for i, num in enumerate(nums):
        complement = target - num  # What we need to find
        if complement in index_map:
            return [index_map[complement], i]  # Return indices
        index_map[num] = i  # Store current number's index
    return []

# Example usage:
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
