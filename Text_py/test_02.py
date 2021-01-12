y =[]
print("请输入100以内正数")
x = 99
if (x > 100 or x < 0):
    print("X须是100以内正数")
else:
    y.append(int(x / 10))
    y.append(int((x % 10) /5))
    y.append(int(((x % 10) % 5) /2))
    y.append(int((((x % 10) % 5) % 2) / 1))
    print("{0}元等于{1}个十元，{2}个五元，{3}个二元，{4}个一元", x, y[0], y[1], y[2], y[3])
