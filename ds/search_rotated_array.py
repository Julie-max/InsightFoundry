class Solution:
    # Function to search target in rotated sorted array using binary search
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while(start<=end):
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[start]<=nums[mid]:
                if target<nums[mid] and target>=nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target>nums[mid] and target<=nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


# Driver code
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3

obj = Solution()
result = obj.search(nums, target)

print(result)