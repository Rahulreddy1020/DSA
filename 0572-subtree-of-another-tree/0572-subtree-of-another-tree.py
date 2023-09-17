# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
    
        if not root: return False
    
        if self.issametree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    
    
    def issametree(self,root,subRoot):
        
        if root is None and subRoot is None: return True
        
        elif root is None or subRoot is None: return False
        
        elif (root.val != subRoot.val):
            return False
        
        return self.issametree(root.left,subRoot.left) and self.issametree(root.right,subRoot.right)
            
# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not subRoot: return True
    
#         if not root: return False
    
#         if self.issametree(root,subRoot):
#             return True
        
#         return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    
    
#     def issametree(self,root,subRoot):
#         if root is None and subRoot is None:
#             return True
#         elif root is None or subRoot is None:
#             return False
#         elif root.val != subRoot.val:
#             return False
#         else:
#             return self.issametree(root.left, subRoot.left) and self.issametree(root.right, subRoot.right)
            


        