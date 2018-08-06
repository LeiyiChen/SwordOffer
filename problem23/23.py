# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
    def pop(self):
        # write code here
        if self.stack != []:
            self.stack.pop(-1)
    def top(self):
        # write code here
        if self.stack != []:
            return self.stack[-1]
        else:
            return None
    def min(self):
        # write code here
        return min(self.stack)