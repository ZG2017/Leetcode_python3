# binary search

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) <= 3:
            return 1
        p1 = 0
        p2 = len(arr)-1
        while p1+1 != p2:
            mid = (p1 + p2)//2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                p1 = mid
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                p2 = mid
        return -1
