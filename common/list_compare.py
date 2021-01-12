#两个数组的元素进行【无序】比较
#两个数组的元素进行【无序】比较
def list_compare(a,b):
    if len(a)==len(b):
        for each_a in a:
            # print(each_a, type(each_a))
            if isinstance(each_a, int):             #不判断整形，直接str转换也行的，但是有绝对值考虑还是判断合适
                print(str(each_a) + " 是int类型，先取【绝对值】再转换为字符串")
                each_a =str(abs(each_a))
            each_a_str="'"+each_a+"'"
            print("打印要比较的a的元素====================")
            print(each_a, type(each_a))
            print("打印要比较的a的元素的两个单引号====================")
            print(each_a_str, type(each_a_str))
            tem = False
            for each_b in b:
                if isinstance(each_b, int):
                    print(str(each_b) + " 是int类型，先取【绝对值】再转换为字符串")
                    each_b_str = str(abs(each_b))
                else:
                    each_b_str = each_b
                print("打印要比较的b的元素====================")
                print(each_b_str, type(each_b_str))
                if (each_a == each_b_str) or (each_a_str == each_b_str):
                    print("a中有元素在b中： " + each_a + " ，或该元素加上单引号后在b中： " + each_a_str)
                    b.remove(each_b)
                    print("打印更新后的b====================")
                    print(b)
                    tem =True
                    print("打印b列表循环后的tem的布尔值====================")
                    print(tem)
                    break
            if tem==False:
                print("a中有元素不在b中： "+each_a+" ，并且该元素加上单引号后也不在b中： "+each_a_str)
                break
    else:
        tem = False
        print("a列表b列表的长度不同，直接匹配失败")
    print(tem)
    return tem