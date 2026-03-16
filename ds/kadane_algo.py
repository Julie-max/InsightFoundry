from typing import List

class Solution:
    # Function to find maximum sum of subarrays
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        current_sum=0
        for i in range(len(nums)):
            current_sum+=nums[i]
            if current_sum>maxi:
                maxi=current_sum
            if current_sum<0:
                current_sum=0
        return maxi

if __name__ == "__main__":
    arr = [-2, -3, -7, -2, -10, -4 ]

    # Create an instance of Solution class
    sol = Solution()

    maxSum = sol.maxSubArray(arr)

    # Print the max subarray sum
    print(f"The maximum subarray sum is: {maxSum}")