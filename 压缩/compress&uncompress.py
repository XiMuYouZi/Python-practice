__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import zipfile,os,glob

# 压缩单个文件
f=zipfile.ZipFile('test.rar','w',zipfile.ZIP_DEFLATED)
f.write('1.txt','11.txt')
f.write('1.doc')
f.write('1.jpg')
f.setpassword(pwd=123)
f.close()


#获取压缩文件test.rar内部的11.txt文档的属性
zipInfo =f.getinfo('11.txt')
print zipInfo.date_time


#压缩一个文件夹test
compress_dir=r'E:\Python\test'
f1=zipfile.ZipFile('test2.rar','w',zipfile.ZIP_DEFLATED)

for dirpath,dirname,filenames in os.walk(compress_dir):
    print dirpath,dirname,filenames
    for filename in filenames:
        f1.write(os.path.join(dirpath,filename))



# 解压一个压缩文件
filename='test1.rar'
uncompress_dir=r'E:\Python\test'
relative_path=os.path.join(os.path.sep, 'test')
uncompress_dir_1=os.path.abspath(relative_path)

judge=zipfile.is_zipfile(filename)

if judge:
    file=zipfile.ZipFile(filename)
    print file.namelist(),
    print file.getinfo('1.txt')
    print file.infolist()

#方法一：使用extract解压
    for file1 in file.namelist():
        print file1
        file.extract(file1,uncompress_dir)

#方法二：使用extractall方法解压
    file.extractall(path=uncompress_dir_1)

else:
    print filename+'不是一个标准的zip文件，无法解压'


