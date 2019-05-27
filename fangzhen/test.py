#该文件用于产生每个人的信息，信息以  节点名：【请求时间， 请求时长】形式产生


import random
import take_time
#50  range(0 , 600000, 200)
#10  range（0， 5000， 200）
Nodes = {}  # 定义节点
N = 10 # 节点数目
A = []  # 每个节点需要发送的消息数
B = list(range(0, 5000, 200))#前两个参数规定了请求会发生的区间
random.shuffle(B)
i = 0

while i < N:
    Nodes[i] = []
    A.append(random.randint(0, 10))  # 随机生成每个节点需要发送的消息数
    j = 0
    while j < A[i]:
        msg = [B[j] + random.randint(1, 100), random.randint(1, 100)]
        # 随机消息内容和时间(并保证每个节点上次发言的结束时间早于下次发言时间
        Nodes[i].append(msg)
        B.pop(0)
        if len(B) <= A[i]:
            B = list(range(0, 10000, 200))
            random.shuffle(B)
        j += 1
    Nodes[i].sort(key=take_time.take_first)
    i += 1
#Nodes[10] = [[110, 30]]
#Nodes[11] = [[110, 10], [120, 10], [130, 10]]

for k, v in Nodes.items():
    print(k, v)