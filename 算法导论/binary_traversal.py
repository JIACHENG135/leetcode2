# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:38:18 2018

@author: ljc
"""
def midOrder(root):
    if root == None:
        return
    res_stack = []
    node = root
    while node or res_stack:
        while node:
            # from root utill the left node doesn't have l.child
            res_stack.append(node)
            node = node.lchild
        # keep in mind that this node is a NIL. Then reset it
        node = res_stack.pop()
        print(node.val)
        # right nodes
        node = node.rsibling
    
    
def postOrder(root):
    if root == None:
        return
    res_stack_1 = []
    res_stack_2 = []
    node = root
    res_stack_1.append(node)
    while res_stack_1:
        node = res_stack_1.pop()
        if node.lchild:
            res_stack_1.append(node.lchild)
        if node.rsibling:
            res_stack_1.append(node.rsibling)
        res_stack_2.append(node)
    while res_stack_2:
        node = res_stack_2.pop()
        print(node.val)
