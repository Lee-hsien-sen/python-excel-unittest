#coding: utf-8 -*-
import os
import re
from common.data_driver_openpyxl import readExcel

path = "D:\PythonPrp\python+excel+unittest\文件夹目录\\"                   # 文件夹目录

def read_file(file_name):     #  读取文件内容并返回
    f = open(file_name,'r',encoding = 'utf-8')          #识别中文目录
    iter_f = iter(f)
    str = ""
    for line in iter_f:   # 遍历文件，一行行遍历，读取文本
        str = str + line
    f.close()
    return str

def write_file(paths):
    flag = True               # 定义一个判断标示
    data = [paths]            #　置一个存放文件夹的list, 这里将要读取的文件夹存入
    filepathname =[]
    fileurl=[]
    filedata=[]
    URL=[]
    URLdata = []
    while flag:
        for i in range(len(data)):  # 遍历目录list
            # print(i)
            file_path = data.pop()   # 取出一个文件目录
            files = os.listdir(file_path)    # 读出目录中的下一级所有文件名和文件夹
            for file in files:               # 遍历文件夹
                # print (file_path+file)
                if not os.path.isdir(file_path+file): #  判断是否是文件夹，不是文件夹才打开
                    if os.path.splitext(file_path+file)[1] == ".py":

                        #
                        # print(file_path + file)
                        filename=file_path + file
                        filename1 = (re.findall('interface test2\\\\(.*)\.py', filename))[0]
                        filepathname.append(filename1)
                        # print(filepathname)
                        #
                        str = read_file(file_path + file)
                        #需要判断是否有url，若无，则保存一个空url，否则，会报错
                        # 需要判断是否有url，若无，则保存一个空url，否则，会报错
                        # 需要判断是否有url，若无，则保存一个空url，否则，会报错
                        # 需要判断是否有url，若无，则保存一个空url，否则，会报错
                        URL=(re.findall('url="(.*)"', str))
                        # print(URL,type(URL))
                        count =0
                        for aa in URL:
                            count = +1
                            # print("URL= ", aa, "}", type(aa))
                        if count > 1:
                            print("打印URL序列有多行=============================================================================================：")
                        else:
                            # URL1 = (re.findall('url="(.*)"', str))[0]
                            fileurl.append(URL[0])
                        #
                        URLdata = (re.findall('{(.*)}', str))
                        # print("打印data序列：")
                        count1=0
                        for aa in URLdata:
                            count1=+1
                            # print("URLdata={",aa,"}",type(aa))
                        if count1 >1:
                            print("打印URLdata序列有多行=========================================================：")
                        else:
                            # URLdata1 = ('data={'+(re.findall('data={(.*)}', str))[0]+'}')
                            # URLdata1 = (re.findall('url="(.*)"', str))[0]
                            URLdata1 = ('{' + URLdata[0] + '}')
                            filedata.append(URLdata1)
                else:
                    # data.append(file_path + file + "/")  # 加入文件夹list
                    if (".") not in file:
                        data.append(file_path + file + "/")  # 加入文件夹list
        if len(data) <= 0:            # 判断文件夹数量，如果为0则置换标示，终止循环
            # print (type(str),str)
            flag = False
            print(len(filepathname), filepathname)
            print(len(fileurl), fileurl)
            print(len(filedata), filedata)

    #
    # 将爬取的name、url、data写入excel
    #
    excel = readExcel(r'D:\PythonPrp\python+excel+unittest\excel_case\paquallpy.xlsx')  # 调用excel文件
    newexcel = excel.writeResults()
    sheet1 = newexcel.get_sheet(0)  # copy原来的excel

    # sheet = data.sheet_by_index(0)
    for j in range(5,(len(filepathname)+5)):   #当前从第五行开始写，可以取原来的row【】【】【后续添加】【】【】
        sheet1.write(j,1,filepathname[j-5])
        sheet1.write(j,2,fileurl[j-5])
        sheet1.write(j,5,filedata[j-5])

    newexcel.save(r'D:\PythonPrp\python+excel+unittest\excel_report\paquallpy2.xls')

write_file(path)