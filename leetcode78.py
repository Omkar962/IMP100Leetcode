# 78. Subsets
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

def subsets(nums):
    ans=[]
    def backtrack(st,path):
        ans.append(path[:])
        for i in range(st,len(nums)):
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()
    backtrack(0,[])
    return ans

print(subsets([1,2,3]))