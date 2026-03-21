class UpperBoundFinder:
    # Binary search to find upper bound
    def upper_bound(self, arr, x):
        start = 0
        end = len(arr)-1
        index = len(arr)
        while(start<=end):
            mid = (start+end)//2
            if arr[mid]>x:
                index = mid
                end = mid-1
            else:
                start = mid+1
        return index




# Driver code
arr = [3, 5, 8, 9, 15, 19]
x = 9

finder = UpperBoundFinder()
ind = finder.upper_bound(arr, x)

print("The upper bound is the index:", ind)