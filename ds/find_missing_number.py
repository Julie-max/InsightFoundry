def missingNum(arr):
    n = len(arr)+1
    missed_num= (n*(n+1)//2) - sum(arr)
    
    return missed_num



if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))