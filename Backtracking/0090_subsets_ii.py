class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def solve(nums,output,idx) :
            ans.append(output[:])
            for i in range(idx,len(nums)) :
                if (i!=idx) & (nums[i] == nums[i-1]) : # important base cond
                    continue
                output.append(nums[i])
                solve(nums,output,i+1)
                output.pop()
        
        nums.sort()
        solve(nums,[],0)
        return ans