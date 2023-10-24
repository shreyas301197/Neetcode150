from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root :
            return []
        ans,res = [],[]
        q = deque([root,None])
        # front = 
        while len(q)!=0 :
            front = q.popleft()  
            if front!=None :
                res.append(front.val)
                if front.left :
                    q.append(front.left)
                if front.right :
                    q.append(front.right)
            else:
                # res.pop()
                ans.append(res)
                if len(q)!= 0:
                    q.append(None)
                res = []
        return ans