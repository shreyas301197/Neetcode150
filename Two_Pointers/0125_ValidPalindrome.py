class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ''
        for i in s :
            if i.isalnum() :
                new_s += i.lower()
        i,j = 0,len(new_s)-1
        while i <= j:
            if new_s[i] != new_s[j] :
                return False
            i += 1
            j -= 1
        return True