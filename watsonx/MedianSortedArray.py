def merge_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    return merged

def median(arr):
    if len(arr) % 2 == 0:
        return arr[len(arr) // 2]
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return median(left + middle + right)

def findMedianSortedArrays(nums1, nums2):
    merged = merge_sorted_arrays(nums1, nums2)
    return median(merged)
