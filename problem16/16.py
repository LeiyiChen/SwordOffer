# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        l = 0
        h = len(array)
        while l < h:
        	if array[l] % 2 == 0:
        		array.append(array.pop(l))
        		h -= 1
        	else:
        		l += 1
        return array

