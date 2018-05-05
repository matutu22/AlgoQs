# 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:  

    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].  
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

---


##### Solution 1:
    class Solution(object):
        def letterCombinations(self, digits):
            """
            :type digits: str
            :rtype: List[str]
            """
            if not digits:
                return []

            dic = {
                "2": ["a","b","c"],
                "3": ["d","e","f"],
                "4": ["g","h","i"],
                "5": ["j","k","l"],
                "6": ["m","n","o"],
                "7": ["p","q","r","s"],
                "8": ["t","u","v"],
                "9": ["w","x","y","z"]
            }
            result = []
            l = len(digits)

            def helper(digits, path, result):
                if len(path) == l:
                    result.append(path)
                for i in range(len(digits)):
                    for j in dic[digits[i]]:
                        helper(digits[i+1:], path+j, result)

            helper(digits,"",result)            
            return result
