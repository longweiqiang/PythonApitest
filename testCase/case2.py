#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 14:31
# @Author  : Weiqiang.long
# @Site    : 
# @File    : case2.py
# @Software: PyCharm

class A():

    def a_add_b(self):
        a=10
        b=20
        self.S=a+b
        print (self.S)
        return self.S

    def c_add_ab(self):
        c=30
        s=c+self.S
        print ('s的值是:',s)



t=A()
#
# print(t.a_add_b())
#
print(t.c_add_ab())