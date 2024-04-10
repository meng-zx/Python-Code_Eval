from collections import deque


def maxSlidingWindow(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        if dq[0] == i - k:
            dq.popleft()

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
