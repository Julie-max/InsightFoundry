# find last index of key using binary search
def solve(n: int, key: int, v: list[int]) -> int:
    start, end = 0, n-1
    ub = n
    while(start<=end):
        mid = (start+end)//2
        if v[mid]>key:
            ub = mid
            end = mid-1
        else: 
            start = mid +1
    if (ub-1)<0 or v[ub-1]!=key:
            return -1
    else:
        return ub-1

# program entry
def main():
    # define input size and key
    n = 7
    key = 13
    # define sorted list
    v = [3, 4, 13, 13, 13, 20, 40]
    # print last occurrence index (or -1)
    print(solve(n, key, v))

# run main
if __name__ == "__main__":
    main()