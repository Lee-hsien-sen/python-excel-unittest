# coding:utf-8
# -*- coding:utf-8 -*-
'''
Created on 2016年10月9日

@author: mengxing
'''
from xml.sax import saxutils
import sys
import datetime
import xlrd
import os

# reload(sys)
# sys.setdefaultencoding('utf8')
d = datetime.datetime.now()
HTML_TMPL = r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>%(title)s</title>
    <meta name="generator" content="%(generator)s"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    %(stylesheet)s
</head>
<body>
<script language="javascript" type="text/javascript"><!--
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}


function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>

%(heading)s
%(report)s
%(ending)s

</body>
</html>
"""
# variables: (title, generator, stylesheet, heading, report, ending)


# ------------------------------------------------------------------------
# Stylesheet
#
# alternatively use a <link> for external style sheet, e.g.
#   <link rel="stylesheet" href="$url" type="text/css">

STYLESHEET_TMPL = """
<style type="text/css" media="screen">
body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
table       { font-size: 100%; }
pre         { }

/* -- heading ---------------------------------------------------------------------- */
h1 {
 font-size: 16pt;
 color: gray;
}
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}

.heading .attribute {
    margin-top: 1ex;
    margin-bottom: 0;
}

.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}

/* -- css div popup ------------------------------------------------------------------------ */
a.popup_link {
}

a.popup_link:hover {
    color: red;
}

.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #E6E6D6;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 8pt;
    width: 500px;
}

}
/* -- report ------------------------------------------------------------------------ */
#show_detail_line {
    margin-top: 3ex;
    margin-bottom: 1ex;
}
#result_table {
    width: 80%;
    border-collapse: collapse;
    border: 1px solid #777;
}
#header_row {
    font-weight: bold;
    color: white;
    background-color: #777;
}
#result_table td {
    border: 1px solid #777;
    padding: 2px;
}
#total_row  { font-weight: bold; }
.passClass  { background-color: #6c6; }
.failClass  { background-color: #c60; }
.errorClass { background-color: #c00; }
.passCase   { color: #6c6; }
.failCase   { color: #c60; font-weight: bold; }
.errorCase  { color: #c00; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }


/* -- ending ---------------------------------------------------------------------- */
#ending {
}

</style>
"""

# ------------------------------------------------------------------------
# Heading
#

HEADING_TMPL = """<div class='heading'>
<h1>%(title)s</h1>
%(parameters)s
<p class='description'>%(description)s</p>
</div>

"""  # variables: (title, parameters, description)

HEADING_ATTRIBUTE_TMPL = """<p class='attribute'><strong>%(name)s:</strong> %(value)s</p>
"""  # variables: (name, value)

# ------------------------------------------------------------------------
# Report
#
# <a href='javascript:showCase(0)'>Summary</a>
# <a href='javascript:showCase(1)'>Failed</a>
REPORT_TMPL = """
<p id='show_detail_line'>Show
<a href='javascript:showCase(0)'>收起</a>
<a href='javascript:showCase(1)'>失败</a>
<a href='javascript:showCase(2)'>展开</a>
</p>
<table id='result_table'>
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>
<tr id='header_row'>
    <td>%(Project_Name)s</td>
    <td>总数</td>
    <td>通过</td>
    <td>失败</td>
    <td>查看</td>
</tr>
%(test_list)s
<tr id='total_row'>
    <td>合计</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>&nbsp;</td>
</tr>
</table>
"""  # variables: (test_list, count, Pass, fail, error)

REPORT_CLASS_TMPL = r"""
<tr class='%(style)s'>
    <td>%(desc)s</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td><a href="javascript:showClassDetail('%(cid)s',%(count)s)">折叠用例</a></td>
</tr>
"""  # variables: (style, desc, count, Pass, fail, error, cid)

REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_%(tid)s')" >
        %(status)s</a>

    <div id='div_%(tid)s' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_%(tid)s').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        <div style="WORD-BREAK: break-all; WORD-WRAP: break-word">
        %(script)s
        </div>
        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>%(status)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
"""  # variables: (id, output)

# ------------------------------------------------------------------------
# ENDING
#

ENDING_TMPL = """<div id='ending'>&nbsp;</div>"""





# 读取excel文件数据，组装html, 代码如下：
# 注意：文件存入的目录\\result\\下
# print(os.path.dirname(os.getcwd()))  # 上级目录
# print(os.getcwd())  # 当前目录
path = os.getcwd()
# path = os.path.join(os.path.dirname(__file__), 'excel_case', 'crm_case.xlsx')
# path = unicode(os.getcwd(), 'utf-8')

#linux环境与windows有所不同，固做了个适配
if True == os.path.isdir(path + '//excel_report//'):
    path_res = path
    # print("路径一： "+path_res )
elif True == os.path.isdir(os.path.dirname(__file__)+ '//excel_report//'):
    path_res = os.path.dirname(__file__)
    # print("路径二： " + os.path.dirname(__file__))
elif True == os.path.isdir(os.path.dirname(path)+ '//excel_report//'):
    path_res = os.path.dirname(path)
    # print("路径三： "+path_res )
else:
    path_res = "/home/qa/test_crm/python+excel+unittest"
    # print("路径四，linux服务器192.168.1.66的绝对路径： "+path_res )

def getReportAttributes(startTime, duration, success_count, failure_count):
    """
    Return report attributes as a list of (name, value).
    Override this to add custom attributes.
    """
    status = []
    status.append('通过数 %s' % success_count)
    status.append('失败数 %s' % failure_count)
    if status:
        status = ' '.join(status)
    else:
        status = 'none'
    return [
        ('开始时间', startTime),
        ('持续时间', duration),
        ('运行状态', status),
    ]


def generateReport(excel, sheet_name, project_Name, title, duration):
    report, pass_count, fail_count = generate_report(excel, sheet_name, project_Name)
    # print("打印generate_report函数执行的成功数和失败数")
    # print(pass_count,fail_count)
    report_attrs = getReportAttributes(str(d), duration, pass_count, fail_count)
    generator = 'Ports_1.0'
    stylesheet = generate_stylesheet()
    heading = generate_heading(title, report_attrs)
    ending = generate_ending()
    output = HTML_TMPL % dict(
        title=saxutils.escape(title),
        generator=generator,
        stylesheet=stylesheet,
        heading=heading,
        report=report,
        ending=ending,
    )
    # self.stream.write(output.encode('utf8'))
    return output,pass_count, fail_count


def generate_stylesheet():
    return STYLESHEET_TMPL


def generate_heading(title, report_attrs):
    a_lines = []
    for name, value in report_attrs:
        line = HEADING_ATTRIBUTE_TMPL % dict(
            name=saxutils.escape(name),
            value=saxutils.escape(value),
        )
        a_lines.append(line)
    heading = HEADING_TMPL % dict(
        title=saxutils.escape(title),
        parameters=''.join(a_lines),
        description=saxutils.escape(u"执行情况"),
    )
    return heading


def exceldata(excel_path, sheet_name):
    try:
        wb = xlrd.open_workbook(path_res + '//excel_report//' + excel_path)
        # wb = xlrd.open_workbook(os.path.join(path_res, 'excel_report', excel_path))
        # wb = xlrd.open_workbook(os.path.join(os.path.dirname(path), 'excel_report', excel_path))

    except:
        wb = xlrd.open_workbook(excel_path)
    sheet = wb.sheet_by_name(sheet_name)
    return sheet


def Duplicate_removal(info_list):
    if len(info_list) != 0:
        Info = []
        [Info.append(i) for i in info_list if not i in Info]
    else:
        Info = []
    return Info



def getexceldata(excel, sheet_name):
    sheet = exceldata(excel, sheet_name)
    a = []
    b = []
    c = []
    # print(sheet.nrows - 1)
    for x in range(sheet.nrows - 1):
        # print("x："+ str(x))
        cells = sheet.row_values(x + 1)
        a.append(cells[0])
        print(cells[14])
        if cells[14] == 'PASS':  # 统计成功
            # print("成功统计一次")
            b.append("PASS")
        elif cells[14] == 'FAIL':  # 统计失败
            # print("失败统计一次")
            c.append("FAIL")
    # Info = Duplicate_removal(a)
    # print(a,b,c)
    # print(len(b)D,len(c))
    return b, c, sheet


def generate_ending():
    return ENDING_TMPL


def generate_report(excel, sheet_name, project_Name):
    b, c, sheet = getexceldata(excel, sheet_name)
    if "FAIL" in c:
        style = "failClass"
    else:
        style = "passClass"

    rows = REPORT_CLASS_TMPL % dict(
        style=style,
        desc=u"用例名称",
        count=len(b) + len(c),
        Pass=len(b),
        fail=len(c),
        cid='c1',
    )
    rows_list = []
    for x in range(sheet.nrows - 1):
        cells = sheet.row_values(x + 1)
        # print()
        tmp1 = REPORT_TEST_WITH_OUTPUT_TMPL
        # print("打印循环的行数"+str(x))
        # print(cells[14])
        if cells[14] == "FAIL":
            # print("该用例失败")
            class_name = 'none'
            class_style = 'failCase'
            status_res = 'FAIL'
            f_t = "ft1."
        else:
            # print("该用例成功")
            class_name = 'hiddenRow'
            class_style = 'none'
            status_res = 'PASS'
            f_t = "pt1."
        # x+1表示序号，script运行过程及结果----响应状态--响应时间
        xx_res = u"\n用例标签:" + f_t + str(x + 1) + u"\n接口名称：" + \
                 str(cells[0]) + u"\n用例名称：" + str(cells[1]) + \
                 u"\n请求URL:" + str(cells[3]) + u"\n请求方式：" + str(cells[9]) + \
                 u"\n请求参数：\n" + str(cells[6]) + u"\n请求账号信息：" + str(cells[8]) + \
                 u"\n返回报文：\n" + str(cells[12]) + u"\n失败原因：" + str(cells[15]) + \
                 u"\n校验结果：" + str(cells[14]) + u"\n执行时间：" + str(cells[16])
        row = tmp1 % dict(tid=f_t + str(x + 1),Class ="class_name",style = class_style,desc = cells[1],script = saxutils.escape(xx_res),status = status_res )
        rows_list.append(row)
        # excel.split(".xls")[0]
    report = REPORT_TMPL % dict(
        Project_Name = project_Name,
        test_list = rows + ''.join(rows_list),
        count = str(len(b) + len(c)),
        Pass = str(len(b)),
        fail = str(len(c)))
    pass_count = len(b)
    fail_count = len(c)
    # print("打印用例执行通过的数，和失败的数")
    # print(pass_count, fail_count)
    return report, pass_count, fail_count


def c_htmlfile(file_name, result_name):
    import io
    # f = io.open(path_res + '\\excel_report\\' + file_name + '\\' + 'html.html', "a", encoding='utf-8')
    f = io.open(path_res + '//excel_report//' + file_name + '//' + 'html.html', "a", encoding='utf-8')
    # f = io.open(os.path.join(path_res,"excel_report",file_name ,'html.html'), "a", encoding='utf-8')

    f.close()
    import time
    new = time.strftime('%Y%m%d%H%M%S', time.localtime())
    os.rename(path_res + '//excel_report//' + file_name + '//' + 'html.html',
              path_res + '//excel_report//' + file_name + '//' + result_name + '_' + new + '.html')
    # os.rename(path_res + '\\excel_report\\' + file_name + '\\' + 'html.html',
    #           path_res + '\\excel_report\\' + file_name + '\\' + result_name + '_' + new + '.html')
    # os.rename(os.path.join(path_res,"excel_report",file_name ,'html.html'),
    #           os.path.join(path_res, "excel_report", file_name, result_name, '_' , new,'.html'))
    html_result = result_name + '_' + new + '.html'
    return html_result


def write_html(excel, sheet_name, project_Name, title, duration):  # excel名，表名，测试项目名，标题，持续时间
    if True == os.path.exists(path_res + '//excel_report//Html_report\\html.html'):
        # print("走到write_html中的TRUE这一步")
        os.remove(path_res + '//excel_report//Html_repor//html.html')

    output,pass_count, fail_count = generateReport(excel, sheet_name, project_Name, title, duration)

    html_path = c_htmlfile("Html_report", "crm_test")
    import io
    f = io.open(path_res + '//excel_report//Html_report//' + html_path, "a", encoding='utf-8')
    # f = io.open(os.path.join(path_res, "excel_report","Html_report",html_path), "a", encoding='utf-8')
    # print("走到write_html中的写html文件的前一步")
    f.write(output)
    # print("走到write_html中的写html文件的后一步")
    f.close()
    # print(pass_count, fail_count)
    # print(html_path)
    return html_path,pass_count, fail_count


if __name__ == "__main__":
    write_html('crm_report.xlsx',"Sheet1", "Name","CRM接口测试报告", "0:00:46.800000")