class Solution:
    def findUnion(self, arr1, arr2, n, m):
        i=0
        j=0
        Union=[]
        while i<n and j<m:
            if arr1[i]<arr2[j]:
                if len(Union)==0 or Union[-1]!=arr1[i]:
                    Union.append(arr1[i])
                i+=1
            elif arr2[j]<arr1[i]:
                if len(Union)==0 or Union[-1]!=arr2[j]:
                    Union.append(arr2[j])
                j+=1
            else:
                if len(Union)==0 or Union[-1]!=arr1[i]:
                    Union.append(arr1[i])
                i+=1
                j+=1
        if i<n:
            Union.extend(arr1[i:n])
        else:
            Union.extend(arr2[j:m])
        return Union


# Driver code
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    n, m = len(arr1), len(arr2)

    obj = Solution()
    result = obj.findUnion(arr1, arr2, n, m)
    print("Union of arr1 and arr2 is:", *result)