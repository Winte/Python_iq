"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

xample 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Sliding Window Technique

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base Case
        if len(s) == 1: return 1


        count, s_result = 0, ''

        for i in s:
            if i not in s_result:
                s_result += i
            else:
                s_result = s_result[s_result.index(i)+1:] + i

            if len(s_result) > count:
                count = len(s_result)
        
        return count