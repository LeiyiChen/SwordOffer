#coding:utf-8
'''
题目：
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。

'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # first solution
        '''
        for i in array:
            if target in i:
                return True
        return False
        '''
        # better solution
        m = len(array)
        n = len(array[0]) - 1
        i = 0
        while i < m and n >= 0:
        	if target > array[i][n]:
        		i += 1
        	elif target < array[i][n]:
        		n -= 1
        	else:
        		return True
        return False

