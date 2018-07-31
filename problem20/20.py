# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def similar(self, p, q):
        #如果Tree2已经遍历完了都能对应的上，返回true
        if q == None:
            return True
        #如果Tree2还没有遍历完，Tree1却遍历完了。返回false
        if p == None:
            return False
        #如果其中有一个点没有对应上，返回false
        if p.val != q.val:
            return False
        #如果根节点对应的上，那么就分别去子节点里面匹配
        return self.similar(p.left, q.left) and self.similar(p.right, q.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        #当Tree1和Tree2都不为零的时候，才进行比较。否则直接返回false
        if pRoot1 != None and pRoot2 != None:
            #如果找到了对应Tree2的根节点的点
            if pRoot1.val == pRoot2.val:
                #以这个根节点为为起点判断是否包含Tree2
                result = self.similar(pRoot1, pRoot2)
            #如果找不到，那么就再去root的左儿子当作起点，去判断时候包含Tree2
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            #如果还找不到，那么就再去root的右儿子当作起点，去判断时候包含Tree2
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        #返回结果
        return result