import random
#繰り返した回数
ren = 0
#調べる回数
resarch = 10
#最大値
max = 10
#ランダムな数字を格納するリスト
numbers = []
#結果を格納するリスト
result_all = []
#数える数↓
examine1 = 1
examine2 = 0
#理論上の値
theoretical = 0.1
#結果
result = 0
errorn_list = []
for n in range(10):
    #正確性を上げるため、10回の平均値をとる
    for i in range(resarch):
        numbers = []
        result = 0
        #繰り返す回数
        for index in range(100):
            ren += 1
            number = random.randint(1, max)
            numbers.append(number)
            if number == examine1 or number == examine2:
                result += 1
        result_all.append(result)
    result_ratio = sum(result_all) / ren
    print("出た回数の平均回数" + str(sum(result_all) / len(result_all)))
    #理論上との相対誤差
    errorn = (result_ratio - theoretical ) / theoretical
    errorn_list.append(errorn)
    print("理論上との相対誤差" + str(errorn))
print("全体の数" + str(len(numbers)))
all_result = sum(errorn_list) / len(errorn_list)
print("相対誤差の平均" + str(all_result))
