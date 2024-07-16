# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        return self.dfs(root, startValue, destValue)[1]
    
    def dfs(self, root, startValue, destValue):
        if not root:
            return 0, ''
        
        dirL, pathL = self.dfs(root.left, startValue, destValue)
        dirR, pathR = self.dfs(root.right, startValue, destValue)

        dirs = dirL + dirR - (root.val == startValue) + (root.val == destValue)

        if dirL < 0:
            return (dirs, pathL + 'UR' + pathR) if dirR else (dirs, pathL + 'U')
        elif dirL > 0:
            return (dirs, pathR + 'UL' + pathL) if dirR else (dirs, 'L' + pathL)
        elif dirR < 0:
            return dirs, pathR + 'U' 
        elif dirR > 0:
            return dirs, 'R' + pathR
        return dirs, pathL + pathR