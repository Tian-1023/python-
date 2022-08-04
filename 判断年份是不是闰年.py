# 输入数字判断年份，输入q，退出程序；判断年份是否为闰年
run = True
while run:
    a = input('请输入年份：')
    is_exit = a == 'q'
    if is_exit:
        run = False
        print('程序退出!')
    else:
        b = int(a)
        is_leap = b % 4 == 0 and b % 100 != 0 or b % 400 == 0
        if not is_leap:
            print('%d年不是闰年。' % b)
        else:
            print('%d年是闰年。' % b)
