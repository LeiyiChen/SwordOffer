# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n >= 0:
        	num =  ('{:032b}'.format(n))
        else:
        	res =  ('{:032b}'.format(-n))[1:]
        	num =  '1'
        	flag = 0
        	for i in range(len(res)-1,-1,-1):
        		if res[i] == '1':
        			index = i
        			flag = 1
        			break
        	if flag:
        	    for i in res[:index]:
        		    num += str(int(i) ^ 1)
        	    num += res[index:]
        	else:
        		num += res
        	print(num,len(num))
        return num.count('1')
