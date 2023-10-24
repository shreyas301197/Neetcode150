# TC = 0(N^2)
class Solution(object):
    def height(self,root) :
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return max(right,left)+1
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        op3 = self.height(root.left)+self.height(root.right)
        return max(left,right,op3)

# TC = 0(N)
def diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def dia(root):
        if not root:
            return 0,0
        left = dia(root.left)
        right = dia(root.right)
        op1,op2 = left[0],right[0]
        op3 =  left[1]+right[1] # diameter using heights
        ans =  (max(op1,op2,op3),1 + max(left[1],right[1])) # (diameter,height
        return ans
    return dia(root)[0]