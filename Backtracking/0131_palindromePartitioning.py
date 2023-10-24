class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans, output = [], []
        def isPalindrome(str) :
            s,e = 0,len(str)-1
            while s < e :
                if str[s]!=str[e] :
                    return False
                s += 1
                e -= 1
            return True
        
        def solve(s, idx) :
            if idx == len(s) :
                ans.append(output[:])
                return
            for i in range(idx,len(s)) :
                output_str = s[idx:i+1]
                # print(output_str)
                if isPalindrome(output_str) :
                    output.append(str(output_str))
                    solve(s,i+1)
                    output.pop()
            
        solve(s, 0)
        return ans