class Solution:
    # Function to find maximum consecutive 1's in an array
    def findMaxConsecutiveOnes(self, nums):
        current_count=0
        max_count=0
        for i in range(len(nums)):
            if nums[i]==1:
                current_count+=1
                if max_count<current_count:
                    max_count=current_count
            elif nums[i]==0:
                current_count=0
        return max_count




# Input array
nums = [1, 1, 0, 1, 1, 1]

# Create Solution object
obj = Solution()

# Get answer
ans = obj.findMaxConsecutiveOnes(nums)

# Print result
print("The maximum consecutive 1's are", ans)