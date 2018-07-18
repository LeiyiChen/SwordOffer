# -*- coding:utf-8 -*-
'''
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # first solution
        '''
        res = ''
        for i in s:
            if i == ' ':
                res += '%20'
            else:
                res += i
        return res
        '''
        # second solution
        p1 = len(s) - 1
        res = list(s)
        n = s.count(' ')
        res += [0] * n * 2
        p2 = len(res) - 1
        while p1 != p2:
            if res[p1] == ' ':
                res[p2] = '0'
                res[p2 - 1] = '2'
                res[p2 - 2] = '%'
                p2 -= 3
            else:
                res[p2] = res[p1]
                p2 -= 1
            p1 -= 1
        return ''.join(res)


