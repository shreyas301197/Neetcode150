class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def solve(root,k) :
            if root == None :
                return -1
            left = solve(root.left,k)
            # propagate the value till the top
            if left!=-1:return left
            k[0] -= 1
            if k[0] == 0 : return root.val
            return solve(root.right,k)

        return solve(root,[k])