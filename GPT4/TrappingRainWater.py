def trap_water(height):
    left, right = 0, len(height) - 1  # Initialize left and right pointers
    left_max, right_max = 0, 0  # Initialize maximum heights to 0
    water_trapped = 0  # Initialize the total water trapped to 0

    while left < right:
        # Move the left pointer to the right
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1
        # Move the right pointer to the left
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1

    return water_trapped

