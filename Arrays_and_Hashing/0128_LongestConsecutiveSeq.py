## Good Solution - O(N)
# every start of sequence number would not have a left neighbor
# NOTE :time complexity to search through ta set is O(1) as a set is implemented through hash tables
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        res = 0
        for n in nums :
            # check if n is start of a seq
            if (n-1) not in numset :
                seq_len = 0
                while (n+seq_len) in numset:
                    seq_len += 1
                res = max(res,seq_len)
        return res

## Sorting Solution - O(N log N)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 :
            return 0
        sort_nums = sorted(list(set(nums))) ## O(n log n)
        res,ans,i = 1,1,1
        while i < len(sort_nums) : ## O(n)
            if sort_nums[i] - sort_nums[i-1] == 1 :
                ans += 1
            else:
                ans = 1
            res = max(ans,res)
            i += 1
        return res