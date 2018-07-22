# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 2:
            return number
        res = [0] * (number + 1)
        res[1] = 1
        res[2] = 2
        for i in range(3, number + 1):
            res[i] += 1
            for j in range(1, i):
                res[i] += res[i - j]
        return res[number]