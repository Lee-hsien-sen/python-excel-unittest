#coding:utf-8
import xlrd
from xlrd import xldate_as_tuple
import openpyxl
from datetime import datetime
class readexcel(object):
    def __init__(self,path,row):
        self.path = path
        self.row = row
        self.row =self.getrows()

    def getsheet(self):
        #通过索引获取一个工作表
        data = xlrd.open_workbook(self.path)
        sheet = data.sheet_by_index(0)
        return sheet

    #获取表的行数
    def getrows(self):
        if self.row < 2:  # 如果self.row小于2时，则按excel中实际数据行数请求接口
            row = self.getsheet().nrows
        else:
            row = self.row  # # # # # #如果self.row大于等于2时，则按传入的self.row的值取数据
        return row

    #获取列数
    def getcol(self):
        col = self.getsheet().ncols
        return col

    # 判断各标题所在的列
    def getallcol(self):
        testallcol = []
        x = self.getcol()
        for i in range(0,x):
            testallcol.append(self.getsheet().cell(0, i).value)
        return testallcol

    #分别获取每一列的数值
    def get_paidanjigou(self):
        x = self.getallcol().index('派单机构')
        items = self.getsheet().col_values(x)
        return items

    def get_paidanjigou_yuan(self):
        x = self.getallcol().index('原派单机构')
        items = self.getsheet().col_values(x)
        return items
    def get_paidanjigou_xin(self):
        x = self.getallcol().index('新派单机构')
        items = self.getsheet().col_values(x)
        return items
    def get_crm_id(self):
        x = self.getallcol().index('CRM_ID')
        items = self.getsheet().col_values(x)
        return items


    def get_guanjia(self):
        x = self.getallcol().index('医美管家姓名')
        items = self.getsheet().col_values(x)
        return items

    def get_paidanyisheng(self):
        x = self.getallcol().index('派单医生')
        items = self.getsheet().col_values(x)
        return items

    def get_chengjiaojigou(self):
        x = self.getallcol().index('成交机构')
        items = self.getsheet().col_values(x)
        return items
    def get_chengjiaoyisheng(self):
        x = self.getallcol().index('成交医生')
        items = self.getsheet().col_values(x)
        return items

    def openpyxl_read_sheet(self):
        book = openpyxl.load_workbook(self.path)
        return book



     
    
     

    
            
 
            
    
