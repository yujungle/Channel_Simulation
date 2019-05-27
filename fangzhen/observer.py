
def observer_init(total_number):

    if total_number >= 50:
        mem_each_group = int(0.1 * float(total_number))
        group = {}
        for i in range(10):
            group[i] = []
        for i in range(10):
            for j in range(mem_each_group):
                group[i].append(i*mem_each_group + j)

    else:
        group_number = int(float(total_number)//5)
        group = {}
        for i in range(group_number):
            group[i] = []
        for i in range(group_number):
            for j in range(5):
                group[i].append(i*5 + j)
    return group

def observer(Observer, current_time, queue_luk):
    group_num = 0

    for i in Observer.keys():
        group_num += 1
    a = (current_time//1000) % group_num

    for i in Observer[a]:
        if i in queue_luk:
            current_time += 5
        else:
            return i