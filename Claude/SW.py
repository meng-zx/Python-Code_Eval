from collections import deque


def maxSlidingWindow(nums, k):
    n = len(nums)
    if n == 0 or k == 0:
        return []

    # Create a deque to store the indices of the elements
    dq = deque()
    # Initialize the result list
    result = []

    # Process the first k elements
    for i in range(k):
        # Remove all elements from the deque that are smaller than nums[i]
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        # Add the index of the current element to the deque
        dq.append(i)

    # Process the remaining elements
    for i in range(k, n):
        # Add the maximum element of the previous window to the result list
        result.append(nums[dq[0]])

        # Remove all elements from the deque that are out of the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove all elements from the deque that are smaller than nums[i]
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()

        # Add the index of the current element to the deque
        dq.append(i)

    # Add the maximum element of the last window to the result list
    result.append(nums[dq[0]])

    return result
