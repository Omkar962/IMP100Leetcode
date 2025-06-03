# 46. Permutations
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]
 

# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

def permute(nums):
    ans=[]
    def backtrack(st):
        if st==len(nums):
            ans.append(nums[:])
            return
        for i in range(st,len(nums)):
            nums[st],nums[i]=nums[i],nums[st]
            backtrack(st+1)
            nums[st],nums[i]=nums[i],nums[st]
    backtrack(0)
    return ans

print(permute([1,2,3]))