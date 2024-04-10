def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    # Calculate the areas of the two rectangles
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)

    # Find the coordinates of the intersection rectangle
    x1 = max(ax1, bx1)
    y1 = max(ay1, by1)
    x2 = min(ax2, bx2)
    y2 = min(ay2, by2)

    # Calculate the area of intersection rectangle
    intersection_area = 0
    if x2 > x1 and y2 > y1:
        intersection_area = (x2 - x1) * (y2 - y1)

    # Calculate the total area covered by the two rectangles
    total_area = area_a + area_b - intersection_area

    return total_area
