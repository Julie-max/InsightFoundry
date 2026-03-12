class Solution:
    # Variant 1: Check if two numbers sum to target using two-pointer approach
    def two_sum_exists(self, arr, target):
        mp={}
        for i in range(len(arr)):
            mp.update({arr[i]:i})
        for i in range(len(arr)):
            needed = target - arr[i]
            if needed in mp and mp[needed]!=i:
                return "YES"
        return "NO" 
     # Variant 2: Return indices of two numbers that sum to target
    def two_sum_indices(self, arr, target):
        mp={}
        for i in range(len(arr)):
            mp.update({arr[i]:i})
        for i in range(len(arr)):
            needed = target - arr[i]
            if needed in mp and mp[needed]!=i:
                return [i,mp[needed]]



if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print(sol.two_sum_exists(arr, target))  # Output: YES
    print(sol.two_sum_indices(arr, target)) # Output: [1, 3]