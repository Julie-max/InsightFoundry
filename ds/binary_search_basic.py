class Solution:
    # Function to perform Binary Search on sorted list
    def binarySearch(self, nums: [int], target: int) -> int:
       start = 0
       end = len(nums)-1
       while(start<=end):
           mid = (start+end)//2
           if target == nums[mid]:
               return mid
           elif target<nums[mid]:
               end = mid-1
           else:
               start=mid+1  
       return -1

if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]  # sorted list
    target = 6  # target element to search

    obj = Solution()  # Create object of Solution class
    ind = obj.binarySearch(a, target)

    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind)
