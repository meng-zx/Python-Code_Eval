def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array to minimize the binary search space.
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        # If partitionX is 0 it means nothing is there on the left side. Use -inf for maxLeftX
        # If partitionX is the length of array then there is nothing on the right side. Use +inf for minRightX
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # We have partitioned array at the correct place
            # Now get max of left elements and min of right elements to get the median in case of even length combined array size
            # or get max of left for odd length combined array size.
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)

        elif maxLeftX > minRightY:  # we are too far on right side for partitionX. Go on left side.
            high = partitionX - 1
        else:  # we are too far on left side for partitionX. Go on right side.
            low = partitionX + 1

    # If the array lengths are zero or the arrays do not follow the problem constraints.
    raise ValueError