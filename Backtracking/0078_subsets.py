class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def powerSet(input_arr,output_arr,idx,ans) :
            if idx >= len(input_arr) :
                ans.append(output_arr[:])
                return
            # exclude 
            powerSet(input_arr,output_arr[:],idx+1,ans)

            #include
            output_arr.append(input_arr[idx])
            powerSet(input_arr,output_arr[:],idx+1,ans)

        ans = []
        output_arr = []
        idx = 0
        powerSet(nums,output_arr,idx,ans)
        return ans