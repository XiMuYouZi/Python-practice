__author__ = 'Administrator'
#coding=utf_8
import os


#将path分割成目录和文件名二元组返回。
# print  os.path.split(r'D:\Program Files (x86)\Python\beautifulsoup4\bs4\testing.py')
#
# print os.path.join(os.path.sep, "a", "b", "c")
#
# relative_path = os.path.join("a", "b", "c", "..", "d")
# print os.path.abspath(relative_path)
#
# print os.listdir(os.getcwd())
#
# os.rmdir(r'e:\python\12')

nums = range(2, 50)

for i in range(2,8):
    print i
    nums = filter(lambda x:x==i or x%i , nums)#x%i表示x除以i的余数不为零
    print nums
    print '@@@@@@@@@@@@@@@@'

print '~~~~~~~~~~~~~~~~'
print nums
'''
i=2:
nums=[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
i=3
[5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
i=4
[5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
i=5
[7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49]
i=6
[7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49]
i=7
[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
'''


