from collections import deque


def maxSlidingWindow(nums, k):
    # Initialize the deque and the result list
    deq = deque()
    result = []

    for i, num in enumerate(nums):
        # Remove elements not in the sliding window
        while deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove elements smaller than the current number
        # as they will not be the maximum in this window
        while deq and nums[deq[-1]] < num:
            deq.pop()

        # Add the current number's index to the deque
        deq.append(i)

        # If the window has reached its size, append the maximum to the result
        if i >= k - 1:
            result.append(nums[deq[0]])

    return result
