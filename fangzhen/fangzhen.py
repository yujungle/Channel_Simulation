import test
import take_time
import delay_
import observer

people = test.Nodes
wait_queue = []  # 等待队列
current_time = 0
total_number = test.N
DELAY = delay_.find_delay(total_number)
observer_group = observer.observer_init(total_number)
queue_luk = []

#每个人的类
class Person(object):
    def __init__(self, number, request_time, speak_time):
        self.number = number
        self.request_time = request_time
        self.speak_time = speak_time


def check():
    global current_time, total_number
    max_request_time = 0
    #找到最终的请求的时间
    for i in range(total_number):
        for j in range(len(people[i])):
            if people[i][j][0] > max_request_time:
                max_request_time = people[i][j][0] + people[i][j][1]

    # 遍历寻找特定时间请求发言者
    while current_time <= max_request_time:
        for number in range(total_number):
            for j in range(len(people[number])):
                if people[number][j][0] <= current_time:
                    temp = Person(number, current_time, people[number][j][1])
                    wait_queue.append(temp)
                    queue_luk.append(number)
                    people[number].pop(j)
                    break

        #该时刻开始发言，判断该时刻是否有冲突

        if wait_queue:#有人请求发言
            print('申请发言！')
            current_time += (2*DELAY + 5)
            Observer = observer.observer(observer_group, current_time, queue_luk)

            #发言队列仅一人 无冲突
            if len(wait_queue) == 1:  # 此时等待发言的只有一个人
                print('观察者' + str(Observer) +': 信道无冲突')
                speak(wait_queue[0])
                wait_queue.pop(0)
                queue_luk.pop(0)

            else:  # 此时有多人想发言
                print('观察者' + str(Observer) +'：多人申请，信道内有冲突！！')
                half(wait_queue, 0, total_number - 1)  # 找到当前可以发言的人
                wait_queue.clear()  # 清空等待队列
                queue_luk.clear()

        else:  # 此时无人请求发言
            current_time = current_time + 1

#该函数定义所谓的发言行为
def speak(speak_person):
    global current_time, total_number
    speak_person.request_time = current_time
    end_time = speak_person.request_time + speak_person.speak_time
    print( str(take_time.take_number(speak_person)) + ' 号可以发言')
    print('发言时间从' + str(speak_person.request_time) + '到' + str(end_time))
    print('\n')
    current_time = end_time


#该函数用于冲突后的折半解决
def half(queue, forward, backward):
    global current_time,observer_group,queue_luk
    queue.sort(key=take_time.take_number)
    temp_ = []
    length = len(queue)


    print("折半剩余节点（实际信道中以下信息不可知） ： ")
    for i in range(length):
        temp_.append(queue[i].number)
    print(temp_)
    poi = -1
    print('\n信道中有请求者发言')

    if length > 1:
        print('观察者' + str(observer.observer(observer_group, current_time, queue_luk)) +'：有冲突，进行折半')
        current_time += (2*DELAY + 5)
        print('\n')
        mid = (forward + backward)//2
        #找到比mid之前的一半的最后位置
        for i in temp_:
            poi += 1
            if i > mid:
                break
        if poi != 0:
            half(queue[0:poi], forward, mid)
        else:
            print('经过 ' + str(2*DELAY + 5) + ' ms后无发言')
            current_time += (2*DELAY + 5)
            print('发言者不在 ' + str(forward) + ' 到 ' + str(mid) + ' 区间之间')
            print('当前时间： ' + str(current_time) + '\n')

        half(queue[poi:length], mid, backward)
    else:
        print('观察者' + str(observer.observer(observer_group, current_time, queue_luk)) + '：当前无冲突，')
        current_time += (2 * DELAY + 5)
        speak(queue[0])


if __name__ == '__main__':
    check()
    print('发言结束')
