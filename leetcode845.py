# 845. Longest Mountain in Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

# Example 1:

# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.
 

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104


def  longestMountain(arr):
    n=len(arr)
    if n<3:
        return 0
    maxlen=0

    for i in range(1,n-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            left=i-1
            right=i+1
            while left>0 and arr[left]>arr[left-1]:
                left-=1
            while right<n-1 and arr[right]>arr[right+1]:
                right+=1
            maxlen=max(maxlen,right-left+1)
    return maxlen

 
print(longestMountain([2,1,4,7,3,2,5]))

print(longestMountain([2,2,2]))

print(longestMountain([1,3,2]))