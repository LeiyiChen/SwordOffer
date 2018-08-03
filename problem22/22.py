# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix is None or matrix == []:
            return []
        row = len(matrix)
        column = len(matrix[0])
        res = []
        i = r_count = c_count = 0
        j = -1
        while r_count < row and c_count < column:
            n = column - c_count
            if n <= 0:
                break
            while n > 0:
                j += 1
                n -= 1
                res.append(matrix[i][j])
            r_count += 1
            n = row - r_count
            if n <= 0:
                break
            while n > 0:
                i += 1
                n -= 1
                res.append(matrix[i][j])
            c_count += 1
            n = column - c_count
            if n <= 0:
                break
            while n > 0:
                j -= 1
                n -= 1
                res.append(matrix[i][j])
            r_count += 1
            n = row - r_count
            if n <= 0:
                break
            while n > 0:
                i -= 1
                n -= 1
                res.append(matrix[i][j])
            c_count += 1
        return res






