class Solution:
    def moveZeroes(self,arr):
        # Initialize a pointer for the position of the next non-zero element
        j=0
        for i in range(len(arr)):
            if arr[i] != 0:
                # Swap the non-zero element with the element at pointer j
                arr[j], arr[i] = arr[i], arr[j]
                j += 1
        return arr
        
    
# Main function
def main():
    arr = [0, 1, 0, 3, 12]
    sol = Solution()
    result = sol.moveZeroes(arr)
    
    # Print result
    print("Array after moving zeroes:", end=" ")
    for num in result:
        print(num, end=" ")
    print()

# Driver code
main()