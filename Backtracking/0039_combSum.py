class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def combSum(input,output,ans,tgt,idx):
            if tgt == 0:
                ans.append(output[:])
                return
            if (tgt < 0 )| (idx == len(input)):
                return
            for i in range(idx,len(input)) :
                if (input[i] > tgt) :
                    continue
                output.append(input[i])
                combSum(input,output[:],ans,tgt-input[i],i)
                output.pop()

        ans = []
        combSum(candidates,[],ans,target,0)
        return ans