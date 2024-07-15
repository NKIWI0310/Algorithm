# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''

2차원 배열 descriptions를 받고, description은 = [parent, child, isLeft], 
isLeft가 1이면 왼쪽 child임


'''
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if not descriptions:
            return None

        nodes = {}
        pNodes = set()
        cNodes = set()

        for p, c, is_left in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
            
            if is_left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            pNodes.add(p)
            cNodes.add(c)
        
        rNode = pNodes - cNodes

        if rNode:
            root_val = rNode.pop()
            return nodes[root_val]
        else:
            return None
