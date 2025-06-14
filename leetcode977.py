# 977. Squares of a Sorted Array
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.


def sortedSquares(nums):
    n=len(nums)
    ans=[0]*n
    left,right=0,n-1
    pos=n-1

    while left<=right:
        if abs(nums[left])>abs(nums[right]):
            ans[pos]=nums[left]*nums[left]
            left+=1
        else:
            ans[pos]=nums[right]*nums[right]
            right-=1
        pos-=1
    return ans


print(sortedSquares([-4,-1,0,3,10]))

print(sortedSquares([-7,-3,2,3,11]))