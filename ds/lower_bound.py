class LowerBoundFinder:
    # Function to find the lower bound index using binary search
    def lower_bound(self, arr, x):
        start=0
        end =len(arr)-1
        
        index = len(arr)
        while(start<=end):
            mid = (start+end)//2
            if x<=arr[mid]:
                index=mid
                end = mid-1

            else:
                start= mid+1
        return index
                



# Driver code
arr = [3,5,8,15,19]                # Sorted input array
x = 9                               # Target value

finder = LowerBoundFinder()           # Create object
ind = finder.lower_bound(arr, x)      # Call method

print("The lower bound is the index:", ind)  # Output result