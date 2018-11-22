# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:54:00 2018

@author: ljc
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #res = []
        #def isValidBSThelper(root,res)
        if not root:
            return False
        if root.left:
            if root.left.val>root.val:
                return False
            else:
                return self.isValidBST(root.left)
        if root.right:
            print('right')
            if root.right.val<root.val:
                return False
            else:
                return self.isValidBST(root.right)
        return True