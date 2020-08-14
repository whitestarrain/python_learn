from multiprocessing import Process
from multiprocessing import Pool
import os
import time
import random


def copyfile(oldfile, newfile):
    file = open(oldfile)
    data = file.read()
    try:
        new_file = open(newfile,"w")
        new_file.write(data)
    except Exception as e:
        print(e)


    pass


def list_file(path,p):
    """ 递归展示所有文件

    :path 目录
    """

    if os.path.isdir(path):
        os.mkdir(path+"复件")
        files = os.listdir(path)
        
        for file in files:
            flag = True
            if os.path.isdir(file):
                flag = False
                print("--------------floder open:: %s" % file)
                list_file(path+"/"+file,p)
                print("--------------floder close")
            else:
                p.apply_async(copyfile,args=(path+"/"+file,path+"复件"+"/"+file+"复件"))
        if flag and file == files[len(files)-1]:
            p.close()
            p.join()

def main():
    p = Pool(3)
    file_name = input("请输入文件名称")
    list_file(file_name,p)
    pass


if __name__ == "__main__":
    main()
