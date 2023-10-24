# runtime complexity - O(N^2 logN)
# space complexity - O(N^2)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for i in strs :
            sorted_i = ''.join(sorted(i))
            try :
                dict[sorted_i].append(i)
            except:
                dict[sorted_i] = [i]
        fin_ls = []
        for i in dict:
            fin_ls += [dict[i]]
        return fin_ls

# runtime complexity - O(N^2)
# space complexity - O(N^2) 
import collections 
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for i in strs :
            count = [0]*26
            for c in i :
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(i)
        return ans.values()