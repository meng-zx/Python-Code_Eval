def lengthOfLIS(nums):
    tails = []  # Initialize an empty list to keep track of the minimum tail of LIS of each length
    for num in nums:
        left, right = 0, len(tails)
        # Use binary search to find the correct position of num in tails
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:  # If num is bigger, it can extend the subsequence
                left = mid + 1
            else:  # Otherwise, num can potentially replace a bigger element in tails
                right = mid
        # If num is larger than any element in tails, append it, indicating we found a longer LIS
        if left == len(tails):
            tails.append(num)
        else:  # Otherwise, replace the first element that is not smaller than num
            tails[left] = num
    return len(tails)  # The length of tails will be the length of the longest increasing subsequence
