
def maxSlidingWindow(nums, k):
    if len(nums) < k:
        return []

    max_window = []
    window_index = 0

    while window_index < len(nums) - k + 1:
        current_window = nums[window_index:window_index + k]
        max_window = max(max_window, current_window)

        window_index += 1

    return max_window
