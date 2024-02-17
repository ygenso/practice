import random
seikou = 0
kaisuu = 0
goukei = 0
for i in range(10):
    for i in range(10000):
        kaisuu += 1
        saikoro = random.randint(1, 6)
        if saikoro == 6:
            seikou += 1
    print(seikou)
    print(kaisuu)
    print(seikou/kaisuu)
    goukei += seikou/kaisuu
    input()
print(goukei/10)
input('OK?')