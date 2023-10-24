class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '' :
            return []
        map = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl',\
        '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
        # if (len(digits) == 1) & (digits is in map) :
        #     return 
        ans = []
        def solve(idx,digits,output) :
            if idx == len(digits) :
                ans.append(''.join(output))
                return
            if digits[idx] not in map :
                return
            keypad_str = map[digits[idx]]
            for ch in keypad_str :
                output.append(ch)
                solve(idx+1,digits,output) 
                output.pop()
        solve(0,digits,[])
        return ans
            