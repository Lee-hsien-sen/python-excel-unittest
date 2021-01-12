# -*- coding: gbk -*-
# 声明一下编码，支持中文

# 遍历字典查找对应的key的所有值，并以列表的形式返回
# 传入数据的value值是字典，则调用get_target_value  传入数据的value值是列表或者元组，则调用get_list_tuple_value

#遍历函数1：传入数据的value值是字典，则直接调用自身
def get_dict_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return '传值错误：argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():    #会自动跳过其它子项中也有key的情况
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
    else:
        for value in dic.values():  # 传入数据不符合则对其value值进行遍历
            if isinstance(value, dict):
                get_dict_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
            elif isinstance(value, (list, tuple)):
                get_list_tuple_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用get_list_tuple_value
                #以下逻辑不能通用，仍在test_kdear.py中分别判断
                    # # 如果该key的velue是一个数组，且该数组中的元素不是字典类型，需要做下处理
                    # # 先判断tmp_list1是【只有一个元素】，再判断tmp_list1[0]为数组类型，如果是数组，则只取tmp_list1[0]赋给tmp_list1
                    # if len(tmp_list) == 1 and isinstance(tmp_list[0], list):
                    #     tmp_list = tmp_list[0]
                    #     print("该key的value是个纯数组类型，即非标准的字典键值对，已做处理")
    return tmp_list

#遍历函数01：传入数据的value值是字典，则直接调用自身
def get_list_tuple_value(key, val, tmp_list):
    for val_ in val:
        # print(val_,type(val_))
        if isinstance(val_, dict):
            get_dict_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            get_list_tuple_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身

# 以上2个函数是一套，一下2个函数是另一套
# 以上2个函数是一套，一下2个函数是另一套

#遍历函数2：传入数据的val值是list，则直接调用自身
def get_list_tuple_value2(key, val, tmp_list):
    if not isinstance(val, list) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return '传值错误：argv[1] not an list or argv[-1] not an list '
    for val_ in val:
        # print(val_,type(val_))
        if isinstance(val_, dict):
            get_dict_value02(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            get_list_tuple_value2(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身
    return tmp_list

#遍历函数02：传入数据的value值是字典，则直接调用自身
def get_dict_value02(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return '传值错误：argv[1] not an dict or argv[-1] not an list '
    if key in dic.keys():   #会自动跳过其它子项中也有key的情况
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
    else:
        for value in dic.values():  # 传入数据不符合则对其value值进行遍历
            if isinstance(value, dict):
                get_dict_value02(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
            elif isinstance(value, (list, tuple)):
                get_list_tuple_value2(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用get_list_tuple_value


#正则匹配序列函数
#正则匹配序列函数
def get_re_list(re_test, tmp_list):
    aaa = True
    if isinstance(tmp_list, list):  # 对传入数据进行格式校验
        # print("调用正则匹配序列函数时，传参不是 list对象，即在字典中遍历出某Key的全部值不是一个序列对象")
              #初始化为真
        count=0
        for v1 in tmp_list :
            # v1  # 传入数据的value值是字典，则调用get_dict_value
            # print('当前准备匹配的正则表达式：',re_test)
            # print("str(v1)之前：   ",v1,"     str(v1)之后：  ",str(v1))
            search1 = re_test.search(str(v1))
            count =count + 1
            try:
                if search1 :
                    print("匹配",count,"次成功")
                else:
                    print("正则匹配一次失败，GameOver")
                    aaa = False
                    return aaa
            except:
                print('我的错误提示信息:匹配出错')
        return aaa
    else:
        aaa = False
        print('正则匹配序列函数:传参格式错误')
        return aaa






if __name__ == "__main__":
    json_1 = {"code":200,"msg":"成功","data":[{"level":1,"value":1,"label":"韩国","children":[{"country_id":1,"country_name":"韩国","district_1":556,"district_1_name":"韩国","district_2":0,"district_2_name":"","level":2,"value":556,"label":"韩国","children":[{"country_id":1,"country_name":"韩国","district_1":556,"district_1_name":"韩国","district_2":"45056","district_2_name":"首尔江南区","level":3,"value":"45056","label":"首尔江南区"},{"country_id":1,"country_name":"韩国","district_1":556,"district_1_name":"韩国","district_2":"45057","district_2_name":"首尔江北区","level":3,"value":"45057","label":"首尔江北区"},{"country_id":1,"country_name":"韩国","district_1":556,"district_1_name":"韩国","district_2":"45058","district_2_name":"首尔瑞草区","level":3,"value":"45058","label":"首尔瑞草区"},{"country_id":1,"country_name":"韩国","district_1":556,"district_1_name":"韩国","district_2":"45059","district_2_name":"首尔以外","level":3,"value":"45059","label":"首尔以外"}]}]},{"level":1,"value":3,"label":"台湾","children":[{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":0,"district_2_name":"","level":2,"value":32,"label":"台湾","children":[{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"493","district_2_name":"台北市","level":3,"value":"493","label":"台北市"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"494","district_2_name":"高雄市","level":3,"value":"494","label":"高雄市"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"495","district_2_name":"基隆市","level":3,"value":"495","label":"基隆市"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"496","district_2_name":"台中市","level":3,"value":"496","label":"台中市"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"497","district_2_name":"台南市","level":3,"value":"497","label":"台南市"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"498","district_2_name":"新竹市","level":3,"value":"498","label":"新竹市"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"499","district_2_name":"嘉义市","level":3,"value":"499","label":"嘉义市"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"500","district_2_name":"台北县","level":3,"value":"500","label":"台北县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"501","district_2_name":"宜兰县","level":3,"value":"501","label":"宜兰县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"502","district_2_name":"桃园县","level":3,"value":"502","label":"桃园县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"503","district_2_name":"新竹县","level":3,"value":"503","label":"新竹县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"504","district_2_name":"苗栗县","level":3,"value":"504","label":"苗栗县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"505","district_2_name":"台中县","level":3,"value":"505","label":"台中县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"506","district_2_name":"彰化县","level":3,"value":"506","label":"彰化县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"507","district_2_name":"南投县","level":3,"value":"507","label":"南投县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"508","district_2_name":"云林县","level":3,"value":"508","label":"云林县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"509","district_2_name":"嘉义县","level":3,"value":"509","label":"嘉义县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"510","district_2_name":"台南县","level":3,"value":"510","label":"台南县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"511","district_2_name":"高雄县","level":3,"value":"511","label":"高雄县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"512","district_2_name":"屏东县","level":3,"value":"512","label":"屏东县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"513","district_2_name":"澎湖县","level":3,"value":"513","label":"澎湖县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"514","district_2_name":"台东县","level":3,"value":"514","label":"台东县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"515","district_2_name":"花莲县","level":3,"value":"515","label":"花莲县"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"45070","district_2_name":"新北市","level":3,"value":"45070","label":"新北市"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"45071","district_2_name":"金門縣","level":3,"value":"45071","label":"金門縣"},{"country_id":3,"country_name":"台湾","district_1":32,"district_1_name":"台湾","district_2":"45072","district_2_name":"連江縣","level":3,"value":"45072","label":"連江縣"}]}]},{"level":1,"value":4,"label":"香港","children":[{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":0,"district_2_name":"","level":2,"value":33,"label":"香港","children":[{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"516","district_2_name":"中西区","level":3,"value":"516","label":"中西区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"517","district_2_name":"东区","level":3,"value":"517","label":"东区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"518","district_2_name":"九龙城区","level":3,"value":"518","label":"九龙城区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"519","district_2_name":"观塘区","level":3,"value":"519","label":"观塘区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"520","district_2_name":"南区","level":3,"value":"520","label":"南区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"521","district_2_name":"深水埗区","level":3,"value":"521","label":"深水埗区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"522","district_2_name":"黄大仙区","level":3,"value":"522","label":"黄大仙区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"523","district_2_name":"湾仔区","level":3,"value":"523","label":"湾仔区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"524","district_2_name":"油尖旺区","level":3,"value":"524","label":"油尖旺区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"525","district_2_name":"离岛区","level":3,"value":"525","label":"离岛区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"526","district_2_name":"葵青区","level":3,"value":"526","label":"葵青区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"527","district_2_name":"北区","level":3,"value":"527","label":"北区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"528","district_2_name":"西贡区","level":3,"value":"528","label":"西贡区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"529","district_2_name":"沙田区","level":3,"value":"529","label":"沙田区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"530","district_2_name":"屯门区","level":3,"value":"530","label":"屯门区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"531","district_2_name":"大埔区","level":3,"value":"531","label":"大埔区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"532","district_2_name":"荃湾区","level":3,"value":"532","label":"荃湾区"},{"country_id":4,"country_name":"香港","district_1":33,"district_1_name":"香港","district_2":"533","district_2_name":"元朗区","level":3,"value":"533","label":"元朗区"}]}]},{"level":1,"value":5,"label":"日本","children":[{"country_id":5,"country_name":"日本","district_1":561,"district_1_name":"日本","district_2":0,"district_2_name":"","level":2,"value":561,"label":"日本","children":[{"country_id":5,"country_name":"日本","district_1":561,"district_1_name":"日本","district_2":"45060","district_2_name":"北海道地方","level":3,"value":"45060","label":"北海道地方"},{"country_id":5,"country_name":"日本","district_1":561,"district_1_name":"日本","district_2":"45061","district_2_name":"东北地方","level":3,"value":"45061","label":"东北地方"},{"country_id":5,"country_name":"日本","district_1":561,"district_1_name":"日本","district_2":"45062","district_2_name":"关东地方","level":3,"value":"45062","label":"关东地方"},{"country_id":5,"country_name":"日本","district_1":561,"district_1_name":"日本","district_2":"45063","district_2_name":"中部地方","level":3,"value":"45063","label":"中部地方"},{"country_id":5,"country_name":"日本","district_1":561,"district_1_name":"日本","district_2":"45064","district_2_name":"近畿地方","level":3,"value":"45064","label":"近畿地方"},{"country_id":5,"country_name":"日本","district_1":561,"district_1_name":"日本","district_2":"45065","district_2_name":"中国四国地方","level":3,"value":"45065","label":"中国四国地方"},{"country_id":5,"country_name":"日本","district_1":561,"district_1_name":"日本","district_2":"45066","district_2_name":"九州地方","level":3,"value":"45066","label":"九州地方"}]}]},{"level":1,"value":6,"label":"泰国","children":[{"country_id":6,"country_name":"泰国","district_1":560,"district_1_name":"泰国","district_2":0,"district_2_name":"","level":2,"value":560,"label":"泰国","children":[{"country_id":6,"country_name":"泰国","district_1":560,"district_1_name":"泰国","district_2":"45067","district_2_name":"曼谷","level":3,"value":"45067","label":"曼谷"}]}]},{"level":1,"value":7,"label":"澳门","children":[{"country_id":7,"country_name":"澳门","district_1":34,"district_1_name":"澳门","district_2":0,"district_2_name":"","level":2,"value":34,"label":"澳门","children":[{"country_id":7,"country_name":"澳门","district_1":34,"district_1_name":"澳门","district_2":"534","district_2_name":"澳门特别行政区","level":3,"value":"534","label":"澳门特别行政区"}]}]}]}
    print(type(json_1))
    key = "value"
    list_temp = []
    list_temp = get_dict_value(key,json_1,list_temp)
    print(list_temp)