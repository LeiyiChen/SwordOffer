# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return None
        if len(sequence) == 1:
            return True
        for i in range(len(sequence)-1):
            if sequence[i] > sequence[-1]:
                break
        for j in range(i+1, len(sequence)-1):
            if sequence[j] < sequence[-1]:
                return False
        left_BST = sequence[:i]
        right_BST = sequence[i:-1]
        if left_BST and right_BST:
            return self.VerifySquenceOfBST(left_BST) and self.VerifySquenceOfBST(right_BST)
        elif left_BST:
            return self.VerifySquenceOfBST(left_BST)
        else:
            return self.VerifySquenceOfBST(right_BST)