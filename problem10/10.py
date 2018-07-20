# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0 or n == 1:
            return n
        else:
            res = [0] * (n+1)
            res[1] = 1
            for i in range(2, n+1):
                res[i] = res[i-1] + res[i-2]
            return res[n]
