class Solution(object):

    def maxPathSum(self, root):
        """
        :type node: TreeNode
        :rtype: int
        """
        result = [root.val]

        def dfs(node):
            if not node :
                return 0
            leftMax = max(dfs(node.left),0) # max(,0) done to make sure we dont add negative children
            rightMax = max(dfs(node.right),0) # max(,0) done to make sure we dont add negative children
            # compute max when we split at node
            result[0] = max(result[0],node.val + leftMax + rightMax)

            # the value that we return is the one we we DONT split
            return node.val + max(leftMax,rightMax)
        
        dfs(root)
        return result[0]