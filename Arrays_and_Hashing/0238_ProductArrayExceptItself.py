# TIME : O(N)
# SPACE : O(N)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # [ 1 , 2 , 3 , 4 ]
        # [   1    , 1   , 1*2 , 1*2*3 ]
        # [2*3*4 , 3*4  ,  4  ,   1    ]
        ans = []
        pre_arr,post_arr = [1 for _ in range(len(nums))],[1 for _ in range(len(nums))]
        n = len(nums)
        for i in range(1,n) :
            pre_arr[i] = pre_arr[i-1]*nums[i-1]
            post_arr[n - i- 1] = post_arr[n - i] *nums[n-i]
        
        for i in range(n) :
            ans.append(pre_arr[i]*post_arr[i])
        return ans
    
# TIME : O(N)
# SPACE : O(1)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0]*n
        ans[0] = 1
        for i in range(1,n) :
            ans[i] = ans[i-1]*nums[i-1]
        r = 1 # calculating right side product on the fly using just an int variable
        for i in reversed(range(n)):
            ans[i] = ans[i] * r
            r *= nums[i]
        return ans