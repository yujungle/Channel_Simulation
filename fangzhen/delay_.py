import random
import math
#延迟 在平面上基本上按人数每人至少3平米的正方形平面中，随机选定坐标
#用勾股定理计算点与点之间最远的一对，来规定传播时延
def find_delay(total):
    V = 340#声速  假定信息是声音
    Squre = float(3 * total)
    D = math.ceil(Squre ** 0.5)
    max_dis = 0

    location = {}

    for i in range(total):
        location[i] = [random.randint(1, D), random.randint(1, D)]
    for i in location.keys():
        for j in location.keys():
            if((location[i][0] - location[j][0])^2 + (location[i][1] - location[j][1])^2) >= max_dis:
                max_dis = (location[i][0] - location[j][0])^2 + (location[i][1] - location[j][1])^2
    delay = round((float(max_dis)/V) * 1000)
    print(location)

    return delay + 4