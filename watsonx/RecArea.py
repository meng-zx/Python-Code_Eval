def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    # Calculate the lengths of the sides of both rectangles
    length_rl = abs(ax2 - ax1)
    width_rl = abs(ay2 - ay1)
    length_tl = abs(bx2 - bx1)
    height_tl = abs(by2 - by1)

    # Calculate the areas of both rectangles
    area_rl = length_rl * width_rl
    area_tl = length_tl * height_tl

    # Return the sum of the areas of both rectangles
    return area_rl + area_tl
