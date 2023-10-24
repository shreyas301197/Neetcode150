class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        dict = {}
        for ch in s :
            try :
                dict[ch] += 1
            except:
                dict[ch] = 1
        for ch in t :
            try :
                dict[ch] -= 1
            except:
                return False
        for k in dict:
            if dict[k] != 0 :
                return False
        return True