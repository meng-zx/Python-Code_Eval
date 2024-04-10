def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2

    l, r = 0, m
    while True:
        i = (l + r) // 2
        j = half - i
        L1 = float('-inf') if i == 0 else nums1[i - 1]
        R1 = float('inf') if i == m else nums1[i]
        L2 = float('-inf') if j == 0 else nums2[j - 1]
        R2 = float('inf') if j == n else nums2[j]

        if L1 > R2:
            r = i - 1
        elif L2 > R1:
            l = i + 1
        else:
            if total % 2 == 0:
                return (max(L1, L2) + min(R1, R2)) / 2
            else:
                return max(L1, L2)

    return