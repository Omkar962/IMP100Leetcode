# 784. Letter Case Permutation
# Medium
# Topics
# premium lock icon
# Companies
# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

 

# Example 1:

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: s = "3z4"
# Output: ["3z4","3Z4"]
 

# Constraints:

# 1 <= s.length <= 12
# s consists of lowercase English letters, uppercase English letters, and digits.

def letterCasePermutation(s):
    ans=[]
    def backtrack(i,path):
        if i==len(s):
            ans.append(path)
            return 
        if s[i].isalpha():
            backtrack(i+1,path+s[i].lower())
            backtrack(i+1,path+s[i].upper())
        else:
            backtrack(i+1,path+s[i])
    backtrack(0,"")
    return ans

print(letterCasePermutation("a1b2"))
