# coding: utf-8
# Your code here!
n = 1
while n < 500:
    i = n
    num = 0
    while n != 1:
        num += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3 + 1
    print(str(i) +" 計算回数:" + str(num))
    n = i + 1
    