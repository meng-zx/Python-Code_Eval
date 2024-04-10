def trap_water(height):
    if not height:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    # Compute the maximum height from the left side
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # Compute the maximum height from the right side
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    # Compute the trapped water
    trapped_water = 0
    for i in range(n):
        trapped_water += max(0, min(left_max[i], right_max[i]) - height[i])

    return trapped_water

