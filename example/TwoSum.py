def two_sum(nums, target):
    # Create a hash map to store the value and its index
    hash_map = {}
    # Iterate through the list
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        # Check if the complement exists in the hash map
        if complement in hash_map:
            # If found, return the indices
            return [hash_map[complement], i]
        # If not found, add the current number and its index to the hash map
        hash_map[num] = i
    return None