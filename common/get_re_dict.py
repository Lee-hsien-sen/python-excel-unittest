# -*- coding: gbk -*-
# ����һ�±��룬֧������

# �����ֵ���Ҷ�Ӧ��key������ֵ�������б����ʽ����
# �������ݵ�valueֵ���ֵ䣬�����get_target_value  �������ݵ�valueֵ���б����Ԫ�飬�����get_list_tuple_value

#��������1���������ݵ�valueֵ���ֵ䣬��ֱ�ӵ�������
def get_dict_value(key, dic, tmp_list):
    """
    :param key: Ŀ��keyֵ
    :param dic: JSON����
    :param tmp_list: ���ڴ洢��ȡ������
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # �Դ������ݽ��и�ʽУ��
        return '��ֵ����argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():    #���Զ���������������Ҳ��key�����
        tmp_list.append(dic[key])  # �������ݴ��������tmp_list
    else:
        for value in dic.values():  # �������ݲ����������valueֵ���б���
            if isinstance(value, dict):
                get_dict_value(key, value, tmp_list)  # �������ݵ�valueֵ���ֵ䣬��ֱ�ӵ�������
            elif isinstance(value, (list, tuple)):
                get_list_tuple_value(key, value, tmp_list)  # �������ݵ�valueֵ���б����Ԫ�飬�����get_list_tuple_value
                #�����߼�����ͨ�ã�����test_kdear.py�зֱ��ж�
                    # # �����key��velue��һ�����飬�Ҹ������е�Ԫ�ز����ֵ����ͣ���Ҫ���´���
                    # # ���ж�tmp_list1�ǡ�ֻ��һ��Ԫ�ء������ж�tmp_list1[0]Ϊ�������ͣ���������飬��ֻȡtmp_list1[0]����tmp_list1
                    # if len(tmp_list) == 1 and isinstance(tmp_list[0], list):
                    #     tmp_list = tmp_list[0]
                    #     print("��key��value�Ǹ����������ͣ����Ǳ�׼���ֵ��ֵ�ԣ���������")
    return tmp_list

#��������01���������ݵ�valueֵ���ֵ䣬��ֱ�ӵ�������
def get_list_tuple_value(key, val, tmp_list):
    for val_ in val:
        # print(val_,type(val_))
        if isinstance(val_, dict):
            get_dict_value(key, val_, tmp_list)  # �������ݵ�valueֵ���ֵ䣬�����get_target_value
        elif isinstance(val_, (list, tuple)):
            get_list_tuple_value(key, val_, tmp_list)   # �������ݵ�valueֵ���б����Ԫ�飬���������

# ����2��������һ�ף�һ��2����������һ��
# ����2��������һ�ף�һ��2����������һ��

#��������2���������ݵ�valֵ��list����ֱ�ӵ�������
def get_list_tuple_value2(key, val, tmp_list):
    if not isinstance(val, list) or not isinstance(tmp_list, list):  # �Դ������ݽ��и�ʽУ��
        return '��ֵ����argv[1] not an list or argv[-1] not an list '
    for val_ in val:
        # print(val_,type(val_))
        if isinstance(val_, dict):
            get_dict_value02(key, val_, tmp_list)  # �������ݵ�valueֵ���ֵ䣬�����get_target_value
        elif isinstance(val_, (list, tuple)):
            get_list_tuple_value2(key, val_, tmp_list)   # �������ݵ�valueֵ���б����Ԫ�飬���������
    return tmp_list

#��������02���������ݵ�valueֵ���ֵ䣬��ֱ�ӵ�������
def get_dict_value02(key, dic, tmp_list):
    """
    :param key: Ŀ��keyֵ
    :param dic: JSON����
    :param tmp_list: ���ڴ洢��ȡ������
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # �Դ������ݽ��и�ʽУ��
        return '��ֵ����argv[1] not an dict or argv[-1] not an list '
    if key in dic.keys():   #���Զ���������������Ҳ��key�����
        tmp_list.append(dic[key])  # �������ݴ��������tmp_list
    else:
        for value in dic.values():  # �������ݲ����������valueֵ���б���
            if isinstance(value, dict):
                get_dict_value02(key, value, tmp_list)  # �������ݵ�valueֵ���ֵ䣬��ֱ�ӵ�������
            elif isinstance(value, (list, tuple)):
                get_list_tuple_value2(key, value, tmp_list)  # �������ݵ�valueֵ���б����Ԫ�飬�����get_list_tuple_value


#����ƥ�����к���
#����ƥ�����к���
def get_re_list(re_test, tmp_list):
    aaa = True
    if isinstance(tmp_list, list):  # �Դ������ݽ��и�ʽУ��
        # print("��������ƥ�����к���ʱ�����β��� list���󣬼����ֵ��б�����ĳKey��ȫ��ֵ����һ�����ж���")
              #��ʼ��Ϊ��
        count=0
        for v1 in tmp_list :
            # v1  # �������ݵ�valueֵ���ֵ䣬�����get_dict_value
            # print('��ǰ׼��ƥ���������ʽ��',re_test)
            # print("str(v1)֮ǰ��   ",v1,"     str(v1)֮��  ",str(v1))
            search1 = re_test.search(str(v1))
            count =count + 1
            try:
                if search1 :
                    print("ƥ��",count,"�γɹ�")
                else:
                    print("����ƥ��һ��ʧ�ܣ�GameOver")
                    aaa = False
                    return aaa
            except:
                print('�ҵĴ�����ʾ��Ϣ:ƥ�����')
        return aaa
    else:
        aaa = False
        print('����ƥ�����к���:���θ�ʽ����')
        return aaa






if __name__ == "__main__":
    json_1 = {"code":200,"msg":"�ɹ�","data":[{"level":1,"value":1,"label":"����","children":[{"country_id":1,"country_name":"����","district_1":556,"district_1_name":"����","district_2":0,"district_2_name":"","level":2,"value":556,"label":"����","children":[{"country_id":1,"country_name":"����","district_1":556,"district_1_name":"����","district_2":"45056","district_2_name":"�׶�������","level":3,"value":"45056","label":"�׶�������"},{"country_id":1,"country_name":"����","district_1":556,"district_1_name":"����","district_2":"45057","district_2_name":"�׶�������","level":3,"value":"45057","label":"�׶�������"},{"country_id":1,"country_name":"����","district_1":556,"district_1_name":"����","district_2":"45058","district_2_name":"�׶������","level":3,"value":"45058","label":"�׶������"},{"country_id":1,"country_name":"����","district_1":556,"district_1_name":"����","district_2":"45059","district_2_name":"�׶�����","level":3,"value":"45059","label":"�׶�����"}]}]},{"level":1,"value":3,"label":"̨��","children":[{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":0,"district_2_name":"","level":2,"value":32,"label":"̨��","children":[{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"493","district_2_name":"̨����","level":3,"value":"493","label":"̨����"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"494","district_2_name":"������","level":3,"value":"494","label":"������"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"495","district_2_name":"��¡��","level":3,"value":"495","label":"��¡��"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"496","district_2_name":"̨����","level":3,"value":"496","label":"̨����"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"497","district_2_name":"̨����","level":3,"value":"497","label":"̨����"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"498","district_2_name":"������","level":3,"value":"498","label":"������"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"499","district_2_name":"������","level":3,"value":"499","label":"������"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"500","district_2_name":"̨����","level":3,"value":"500","label":"̨����"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"501","district_2_name":"������","level":3,"value":"501","label":"������"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"502","district_2_name":"��԰��","level":3,"value":"502","label":"��԰��"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"503","district_2_name":"������","level":3,"value":"503","label":"������"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"504","district_2_name":"������","level":3,"value":"504","label":"������"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"505","district_2_name":"̨����","level":3,"value":"505","label":"̨����"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"506","district_2_name":"�û���","level":3,"value":"506","label":"�û���"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"507","district_2_name":"��Ͷ��","level":3,"value":"507","label":"��Ͷ��"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"508","district_2_name":"������","level":3,"value":"508","label":"������"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"509","district_2_name":"������","level":3,"value":"509","label":"������"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"510","district_2_name":"̨����","level":3,"value":"510","label":"̨����"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"511","district_2_name":"������","level":3,"value":"511","label":"������"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"512","district_2_name":"������","level":3,"value":"512","label":"������"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"513","district_2_name":"�����","level":3,"value":"513","label":"�����"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"514","district_2_name":"̨����","level":3,"value":"514","label":"̨����"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"515","district_2_name":"������","level":3,"value":"515","label":"������"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"45070","district_2_name":"�±���","level":3,"value":"45070","label":"�±���"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"45071","district_2_name":"���T�h","level":3,"value":"45071","label":"���T�h"},{"country_id":3,"country_name":"̨��","district_1":32,"district_1_name":"̨��","district_2":"45072","district_2_name":"�B���h","level":3,"value":"45072","label":"�B���h"}]}]},{"level":1,"value":4,"label":"���","children":[{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":0,"district_2_name":"","level":2,"value":33,"label":"���","children":[{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"516","district_2_name":"������","level":3,"value":"516","label":"������"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"517","district_2_name":"����","level":3,"value":"517","label":"����"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"518","district_2_name":"��������","level":3,"value":"518","label":"��������"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"519","district_2_name":"������","level":3,"value":"519","label":"������"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"520","district_2_name":"����","level":3,"value":"520","label":"����"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"521","district_2_name":"��ˮ����","level":3,"value":"521","label":"��ˮ����"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"522","district_2_name":"�ƴ�����","level":3,"value":"522","label":"�ƴ�����"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"523","district_2_name":"������","level":3,"value":"523","label":"������"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"524","district_2_name":"�ͼ�����","level":3,"value":"524","label":"�ͼ�����"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"525","district_2_name":"�뵺��","level":3,"value":"525","label":"�뵺��"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"526","district_2_name":"������","level":3,"value":"526","label":"������"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"527","district_2_name":"����","level":3,"value":"527","label":"����"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"528","district_2_name":"������","level":3,"value":"528","label":"������"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"529","district_2_name":"ɳ����","level":3,"value":"529","label":"ɳ����"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"530","district_2_name":"������","level":3,"value":"530","label":"������"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"531","district_2_name":"������","level":3,"value":"531","label":"������"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"532","district_2_name":"������","level":3,"value":"532","label":"������"},{"country_id":4,"country_name":"���","district_1":33,"district_1_name":"���","district_2":"533","district_2_name":"Ԫ����","level":3,"value":"533","label":"Ԫ����"}]}]},{"level":1,"value":5,"label":"�ձ�","children":[{"country_id":5,"country_name":"�ձ�","district_1":561,"district_1_name":"�ձ�","district_2":0,"district_2_name":"","level":2,"value":561,"label":"�ձ�","children":[{"country_id":5,"country_name":"�ձ�","district_1":561,"district_1_name":"�ձ�","district_2":"45060","district_2_name":"�������ط�","level":3,"value":"45060","label":"�������ط�"},{"country_id":5,"country_name":"�ձ�","district_1":561,"district_1_name":"�ձ�","district_2":"45061","district_2_name":"�����ط�","level":3,"value":"45061","label":"�����ط�"},{"country_id":5,"country_name":"�ձ�","district_1":561,"district_1_name":"�ձ�","district_2":"45062","district_2_name":"�ض��ط�","level":3,"value":"45062","label":"�ض��ط�"},{"country_id":5,"country_name":"�ձ�","district_1":561,"district_1_name":"�ձ�","district_2":"45063","district_2_name":"�в��ط�","level":3,"value":"45063","label":"�в��ط�"},{"country_id":5,"country_name":"�ձ�","district_1":561,"district_1_name":"�ձ�","district_2":"45064","district_2_name":"���ܵط�","level":3,"value":"45064","label":"���ܵط�"},{"country_id":5,"country_name":"�ձ�","district_1":561,"district_1_name":"�ձ�","district_2":"45065","district_2_name":"�й��Ĺ��ط�","level":3,"value":"45065","label":"�й��Ĺ��ط�"},{"country_id":5,"country_name":"�ձ�","district_1":561,"district_1_name":"�ձ�","district_2":"45066","district_2_name":"���ݵط�","level":3,"value":"45066","label":"���ݵط�"}]}]},{"level":1,"value":6,"label":"̩��","children":[{"country_id":6,"country_name":"̩��","district_1":560,"district_1_name":"̩��","district_2":0,"district_2_name":"","level":2,"value":560,"label":"̩��","children":[{"country_id":6,"country_name":"̩��","district_1":560,"district_1_name":"̩��","district_2":"45067","district_2_name":"����","level":3,"value":"45067","label":"����"}]}]},{"level":1,"value":7,"label":"����","children":[{"country_id":7,"country_name":"����","district_1":34,"district_1_name":"����","district_2":0,"district_2_name":"","level":2,"value":34,"label":"����","children":[{"country_id":7,"country_name":"����","district_1":34,"district_1_name":"����","district_2":"534","district_2_name":"�����ر�������","level":3,"value":"534","label":"�����ر�������"}]}]}]}
    print(type(json_1))
    key = "value"
    list_temp = []
    list_temp = get_dict_value(key,json_1,list_temp)
    print(list_temp)