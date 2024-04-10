def lengthOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)

    # Initialize LIS values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom-up manner
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Return maximum value from LIS array
    return max(lis)
