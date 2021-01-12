import os
import xlrd

def open_excel(file= 'crm_case.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)

def main():
    #tables = excel_table_byindex()
    #for row in tables:
    #  print (row)
    fw=open('D:\\test3.txt','a')

    data = open_excel("D:\PythonPrp\python+excel+unittest\excel_case\crm_case.xlsx")
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    print(nrows)
    print(ncols)
    for rownum in range(2,nrows):
        row = table.row_values(rownum)
        exceline=''
        if row:
            for colnum in range(ncols):
                wordhk=row[colnum]
                if type(wordhk)==type(1.0):
                    wordhk=int(wordhk)
                    wordhk=str(wordhk)
                if colnum==1:
                    if str(row[7]).strip()=='':
                        exceline=exceline+'<tr bordercolor="#cccccc" clas=""><td width="195"><p class="myaa" align="left"><a class="myaa" href="#" target="_blank">'+wordhk+'</a></p></td>'
                    else:
                        exceline=exceline+'<tr bordercolor="#cccccc" clas=""><td width="195"><p class="myaa" align="left"><a class="myaa" href="'+str(row[7])+'" target="_blank">'+wordhk+'</a></p></td>'
                if colnum==2:
                    exceline=exceline+'<td width="203"><p class="myaa" align="left">'+wordhk+'</p></td>'
                if colnum==3:
                    exceline=exceline+'<td width="57"><p class="myaa" align="center">'+wordhk+'</p></td>'
                if colnum==4:
                    exceline=exceline+'<td width="48"><p class="myaa" align="center">'+wordhk+'</p></td>'
                if colnum==5:
                    exceline=exceline+'<td width="74"><p class="myaa" align="center">'+wordhk+'</p></td>'
                if colnum==6:
                    exceline=exceline+'<td width="77"><p class="myaa" align="center">'+wordhk+'</p></td></tr>\n'
            print(exceline)
            fw.write(exceline)
        fw.close()
        fr=open('D:\\test3.txt')
        for line in fr.readlines():
            print(line)
        fr.close()

if __name__=="__main__":
    main()
