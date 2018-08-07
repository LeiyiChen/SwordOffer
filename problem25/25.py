# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        pre_level = [root]
        res = [root.val]
        next_level = []
        while True:
            while pre_level:
                cur_node = pre_level.pop(0)
                if cur_node.left:
                    next_level.append(cur_node.left)
                    res.append(cur_node.left.val)
                if cur_node.right:
                    next_level.append(cur_node.right)
                    res.append(cur_node.right.val)
            if next_level == []:
                break
            pre_level = next_level
            next_level = []
        return res




