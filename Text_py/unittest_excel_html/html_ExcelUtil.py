import xlrd
import xlsxwriter
import traceback
class ParseExcel(object):
    #excel路径，sheet页名称
    def __init__(self,excelPath,sheetName):
        try:
            #将读取得excel加载到内存
            self.wb=xlrd.open_workbook(excelPath)
        except Exception as e:
            print(traceback.format_exc())
        else:
            #通过工作表名称获取一个工作表对象
            self.sheet=self.wb.sheet_by_name(sheetName)
            #获取工作表中存在数据的区域的最大行号
            self.maxRowNum=self.sheet.nrows
    def getDatasFromSheet(self):

        #用于存放从工作表中读取出来的数据
        dataList=[]
        #因为工作表中的第一行是标题行，所以需要去掉
        for i in range(1,self.maxRowNum):
            #行内容
            row = self.sheet.row_values(i)
            if row:
                temList=[]
                temList.append(row[1])
                temList.append(row[2])
                temList.append(row[3])
                temList.append(row[4])
                temList.append(row[5])
                temList.append(row[6])
                dataList.append(temList)

        # print(dataList)
        return dataList



# ParseExcel('/Users/wangsen/PycharmProjects/WEB_TEST/EXCEL/web自动化测试数据.xlsx','搜索数据表').getDatasFromSheet()