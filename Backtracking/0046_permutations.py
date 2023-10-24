class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1 :
            return [nums]
        vis = dict((k,0) for k in nums)
        ans = []
        def solve(nums,output,vis) :
            if len(nums) == len(output) :
                ans.append(output[:])
                return
            for i in nums :
                if vis[i] == 1 :
                    continue
                output.append(i)
                vis[i] = 1
                solve(nums,output[:],vis)
                vis[i] = 0
                output.pop()
        
        solve(nums,[],vis)
        return ans