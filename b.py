def isSubsetSumRec(arr,  n, sum, memo):

    # If the sum is zero, we found 
    # a subset
    if sum == 0:
        return True

    # If no elements are left
    if n <= 0:
        return False

    # If the value is already 
    # computed, return it
    if memo[n][sum] != -1:
        return memo[n][sum]

    # If the last element is greater 
    # than the sum, ignore it
    if arr[n - 1] > sum:
        memo[n][sum] = isSubsetSumRec(arr, n - 1, sum, memo)
    else:
      
        # Include or exclude the last element
        # directly
        memo[n][sum] = (isSubsetSumRec(arr, n - 1, sum, memo)
                        or isSubsetSumRec(arr, n - 1, sum - arr[n - 1], memo))

    return memo[n][sum]


def isSubsetSum(arr, sum):
    n = len(arr)
    memo = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]
    if sum==0 or len(arr)==0:
        return True
    memo[0,:]=0
    memo[:,0]=0
    for i in range(1,len(n+1)):
        for j in range(1,sum+1):
            memo[i][j]=ne

    
           


if __name__ == "__main__":
    arr = [1, 5,1]
    sum = 8

    if isSubsetSum(arr, sum):
        print("True")
    else:
        print("False")