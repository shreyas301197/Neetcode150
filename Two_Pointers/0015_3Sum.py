class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)
        nums.sort()
        for idx,i in enumerate(nums) :
            # this condition is needed to avoid duplicate triplets
            if idx > 0 and nums[idx-1] == i:
                continue
            l,r = idx+1,n-1
            while l < r :
                if nums[l]+nums[r]+i == 0 :
                    ans.append([i,nums[l],nums[r]])
                    # do not forget to update the pointer here to find other solutions
                    l += 1
                    # this loop is needed to avoid duplicates for nums[l]/nums[r]
                    while nums[l] == nums[l-1] and l < r :
                        l += 1
                elif nums[l]+nums[r]+i > 0 :
                    r -= 1
                else:
                    l += 1
        return ans