# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if popV is None:
            return None
        pop_num = 0
        try:
            c_index = pushV.index(popV[0])
        except ValueError:
            return False
        l = pushV[:c_index]
        for i in range(1, len(popV)):
            pre_index = c_index
            if popV[i] == l[-1]:
                l.pop(-1)
                pop_num += 1
                continue
            try:
                c_index = pushV.index(popV[i])
            except ValueError:
                return False
            if c_index > pre_index:
                if pre_index + 1 != c_index:
                    l.extend(pushV[pre_index+1:c_index])
            else:
                return False
        return True