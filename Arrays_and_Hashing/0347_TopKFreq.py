import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_arr = [[] for _ in range(len(nums)+1)]
        num2count = collections.defaultdict(int)
        for i in nums : 
            num2count[i] += 1
        ans = []
        for ele,freq in num2count.items() :
            count_arr[freq].append(ele)
        for freq in range(len(nums),-1,-1) :
            if k==0 :
                break
            if len(count_arr[freq]) > 0 :
                ans += count_arr[freq]
                k -= len(count_arr[freq])
        return ans