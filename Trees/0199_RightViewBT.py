# both are pretty much similar solutions, BFS in trees implies Level Order Traversal
# just that the second solution is a bit more compact and doesnt require 2 diff functions

import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
      
          :rtype: List[List[int]]
        """
        if not root :
            return []
        ans,res = [],[]
        q = collections.deque([root,None])
        # front = 
        while len(q)!=0 :
            front = q.popleft()  
            if front!=None :
                ans.append(front.val)
                if front.left :
                    q.append(front.left)
                if front.right :
                    q.append(front.right)
            else:
                # res.pop()
                ans.append('#')
                if len(q)!= 0:
                    q.append(None)
                res = []
        ans.pop()
        return  ans
        

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root :
            return []
        ans = self.levelOrder(root)
        if len(ans) == 1:
            return ans
        res = []
        # print(ans)
        for i in range(1,len(ans)) :
            if ans[i] == '#':
                res.append(ans[i-1])
            if i == len(ans) - 1 :
                res.append(ans[i])

        return res
        
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res