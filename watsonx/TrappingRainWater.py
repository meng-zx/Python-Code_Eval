def trap_water(height):
    # Initialize total water trapped to 0
    total_water = 0

    # Iterate through the height values
    for i in range(len(height)):
        # If the height value is greater than 0, add the width of the corresponding bar to the total water trapped
        if height[i] > 0:
            total_water += height[i] + 1

    # If the last element of the list is less than or equal to 1, add 1 to the total water trapped
    if height[-1] <= 1:
        total_water += 1

    return total_water

