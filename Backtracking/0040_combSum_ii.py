class Solution(object):
    def combinationSum2(self, candidates, target):
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
                # make sure that no duplication solution sets are formed
                if (i > idx) & (input[i] == input[i-1]) :
                    continue
                if (input[i] > tgt) :
                    break
                output.append(input[i])
                combSum(input,output[:],ans,tgt-input[i],i+1)
                output.pop()

        ans = []
        combSum(sorted(candidates),[],ans,target,0)
        return ans