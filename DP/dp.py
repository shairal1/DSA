'''
https://pythontutor.com
#  Types of DP
1. 0-1 knapsack
2. Unbounded knapsack
3. Fibonacci Series
4. Longest Common Subsequence
5. Longest Increasing Subsequence
6. Kadane's Algorithm
7. Matrix Chain Multiplication
8. DP on Tree
9. DP on Grid
10. other types
'''
'''

--------------------------------
0-1 knapsack : in this we can take an item only once (0 or 1)
--------------------------------
-variation :
  -subset sum
  -equal sum partition
  -count of subset sum
  -minimum subset sum difference
  -target sum
  -number of subset given difference
--------------------------------
note: Fractional knapsack is not a DP problem , it is a greedy problem
'''
# RECURSIVE SOLUTION
def knapsack(wt,val,W,n):
    if n==0 or W==0: # think of base case -> ie. smallest valid input
        return 0
    if wt[n-1]<=W:
        return max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
    else:
        return knapsack(wt,val,W,n-1)
#TOP DOWN SOLUTION --MEMOIZATION (RECURSIVE + MEMOIZATION)
'''
🌲 Top-Down (Memoization): Tree-Like Structure n->n-1->n-2->...->0
Formed via recursion.
Each node branches out into subproblems.
Forms a recursive tree, but thanks to memoization, repeated subproblems are not recomputed, just reused.
🔁 Characteristics:

Looks like a tree with pruning due to memoization.
You only compute what's necessary for the original problem.
Useful when the number of actually needed subproblems is small.
Code:
    - choice diagram :
    - if wt[n-1]<=W:
        - include
        - exclude
    - else:
        - exclude
    - base case : if n==0 or W==0: return 0
'''
"""
MISTAKES:
dp mei phele y hota hai , then x hota hai
dp[y][x] first y is for length of array , x is for target sum
ulta karti hu mai
 dp=[[-1]* (5)for _ in range(7)]
 this will create 7*5 grid
    for row in dp:
        print(row)
    for y in range(7):
            dp[0][y]=0

    for row in range(5):
        dp[row][0]=0
mei x movement karti hu , then y movement karti hu

so it should be 
   

"""
def knapsack_memo(wt,val,W,n):
    dp = [[-1 for i in range(W+1)] for j in range(n+1)]
    def knapsack_memo_helper(wt,val,W,n):
        if n==0 or W==0:
            return 0
        if dp[n][W]!=-1:
            return dp[n][W]
        if wt[n-1]<=W:
            dp[n][W] = max(val[n-1]+knapsack_memo_helper(wt,val,W-wt[n-1],n-1),knapsack_memo_helper(wt,val,W,n-1))
        else:
            dp[n][W] = knapsack_memo_helper(wt,val,W,n-1)
        return dp[n][W]
    return knapsack_memo_helper(wt,val,W,n)

# BOTTOM UP SOLUTION --TABULATION
'''
🧱 Bottom-Up (Tabulation): Table-Filled Iteratively 0->1->2->...->n
No recursion, just filling up a 2D DP table.
You compute all subproblems in a specific order (usually increasing size).
There's no tree, just a grid being filled from the smallest subproblems up.
🔁 Characteristics:

All entries are filled, even if not all are needed.
Better control over memory and often better performance due to iteration (and avoiding recursion stack).
📊 Looks Like:
Filling dp[0...n][0...W] with loops:
code:
    - Initialize dp table with (0,col) and (row,0) = recursion base case
    - fill the table in a specific order
    - return dp[n][W]
'''
def knapsack_tab(wt,val,W,n):
    dp = [[-1 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif wt[i-1]<=j:
                dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]

# Subset sum problem
'''
q: given a set of non-negative integers, 
and a value sum, determine if there is a subset of the given set with sum equal to given sum.

'''
def subset_sum(arr,sum):
    if sum==0:
            return True
    if arr==[]:
            return False
    def subset_sum_helper(arr,tsum,n):
        if tsum==sum:
            return True
        if n <0:
            return False
        if arr[n]<=sum:
            return subset_sum_helper(arr,tsum+arr[n],n-1) or subset_sum_helper(arr,tsum,n-1)
        else:
            return subset_sum_helper(arr,tsum,n-1)
    return subset_sum_helper(arr,0,len(arr)-1)
    

def canPartition( nums):
        def recc(nums,sumleft,sumright):
            if not nums:
                return False 
            if sumleft ==sumright and sumleft !=0:
                return True 
            return recc(nums[:-1],sumleft+nums[-1],sumright)or recc(nums[:-1],sumleft,nums[-1]+sumright)
        return recc(nums,0,0)

# Equal sum 
# count subest
def countSubsets(arr, total):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(total + 1)]

    # There is 1 way to make sum 0 (pick nothing)
    for j in range(n + 1):
        dp[0][j] = 1

    for i in range(1, total + 1):
        for j in range(1, n + 1):
            if arr[j - 1] > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - arr[j - 1]][j - 1]

    for row in dp:
        print(row)

    return dp[total][n]
def ExitSubsets(arr, total):
    n = len(arr)
    dp = [[False] * (n + 1) for _ in range(total + 1)]

    #  T to make sum 0 (pick nothing)
    for j in range(n + 1):
        dp[0][j] = True

    for i in range(1, total + 1):
        for j in range(1, n + 1):
            if arr[j - 1] > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] or dp[i - arr[j - 1]][j - 1]

    for row in dp:
        print(row)

    return dp[total][n]
def EqualSubsetExit(arr):
    sum_arr=0
    for i in range(len(arr)):
        sum_arr=arr[i]+sum_arr
    if sum_arr%2==1:
        return False
    else: 
        return ExitSubsets(arr,sum_arr//2)
    
def ExitSubsets(arr, total):
    n = len(arr)
    dp = [[False] * (n + 1) for _ in range(total + 1)]
    # True if sum is 0 (pick nothing)
    for j in range(n + 1):
        dp[0][j] = True

    for i in range(1, total + 1):#|
        for j in range(1, n + 1):#–
            if arr[j - 1] > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] or dp[i - arr[j - 1]][j - 1]
    for row in dp:
        print(row)
    return dp[total][n]

def EqualSubsetExit(arr):
    sum_arr = sum(arr)
    if sum_arr % 2 == 1:
        return False
    else: 
        return ExitSubsets(arr, sum_arr // 2)
#because full arrary should be used then sum can be dvided 
def MinSubsetExit(arr):
    sum_arr = sum(arr)
    possible = []

    for s in range(sum_arr // 2 + 1):
        if ExitSubsets(arr, s):
            possible.append(s)

    best = max(possible)
    min_diff = sum_arr - 2 * best
    print("Possible subset sums:", possible)
    print("Minimum difference:", min_diff)
    return min_diff

def MinSubsetCount(arr):
    sum_arr = sum(arr)
    possible = {}

    for s in range(sum_arr // 2 + 1):
        if countSubsets(arr, s)!=0:
            possible[s]=countSubsets(arr, s)

    best= max(possible.keys())
    count=possible[best]
    #min_diff = sum_arr - 2 * best
    print("Possible subset sums:", possible)
    print("Minimum difference:", count)
    return count

def Target_Sum(arr, target):
    count=0
    dp=[[0]*(sum+1) for i in range(len(arr)+1)]
    
    for i in range(len(arr)+1):#|
        for j in range(sum+1):#-

            dp[i][j]=dp[i-1][j]

arr = [1, 2, 3, 9]
print("Minimum Subset Sum Difference:", MinSubsetCount(arr))
#unbounded knapsack
def cutRod(self, price):
        dp=[[0]*(len(price)+1) for i in range(len(price)+1)]
        for x in range(1,len(price)+1):#length of rod
            for y in range(1,len(price)+1):#inch
                if x<y:
                    dp[x][y]=dp[x][y-1]
                else :
                    dp[x][y]=max(dp[x][y-1],dp[x-y][y]+price[y-1])# repicked

        return dp[-1][-1]
if __name__ == "__main__":
    wt = arr = [1, 6, 11, 5]
   

    #result = EqualSubsetExit(wt)
    #print("Can be partitioned into two equal subsets:", result)

    #print(MinSubsetCount(wt))
'''if __name__ == "__main__":
    wt = [1,2,3,4,6]
    val = [1,2,3,4,5]
    W = 5
    n = 5
     print(knapsack(wt,val,W,n))
    print(knapsack_memo(wt,val,W,n))
    print(canPartition([1,5,11,5]))
    print(canPartition([1,2,3,5]))

    print(subset_sum([1,2,3,5],5))
    print(subset_sum([1,2,3,5],45))
    print(subset_su8m([7, 4 ,5],2))
    #print(knapsack_tab(wt,val,W,n))'''
    #countSubsets(wt,5)
    #ExitSubsets(wt,5)
    #EqualSubsetExit(wt)
    #print(EqualSubsetExit(wt))
#%%
def isSubsequence(s, t) :
        j=0
     
        for i in s:
            a=False
            while j<len(t):
                if i==t[j]:
                    a=True 
                    j=j+1
                    break
                print(j,i)
                j=j+1
            if  not a :
                return False 
        return True   

s = "axc"
t = "ahbgdc"
isSubsequence(s,t)
# %%
