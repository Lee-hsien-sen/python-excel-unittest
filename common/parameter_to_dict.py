# -*- encoding:utf-8 -*-

import json
from furl import furl



def parameter_to_dict(str_parameter):
    if not isinstance(str_parameter, str):
        print("传入的参数不是str,需转换成str,1")
        str_parameter=str(str_parameter)
        if "?" in str_parameter and "=" in str_parameter:
            g = furl(str_parameter)
            print(g.args)
            return (dict(g.args))
        elif "=" in str_parameter:
            str_parameter = "?" + str_parameter
            g = furl(str_parameter)
            print(g.args)
            return (dict(g.args))
        else:
            print("传入的参数没有等于号“=”,1")
            return {}
    else:
        if "?" in str_parameter and "=" in str_parameter:
            g = furl(str_parameter)
            print(g.args)
            return (dict(g.args))
        elif "=" in str_parameter:
            str_parameter = "?" + str_parameter
            g = furl(str_parameter)
            print(g.args)
            return (dict(g.args))
        else:
            print("传入的参数没有等于号“=”,2")
            return {}


if __name__ == "__main__":
    a = "eclassID=2107&pageSize=50&pageNo=1&startTime=&endTime=&readType=all_read"
    b = parameter_to_dict(a)
    b = json.dumps(b)
    print(b)
