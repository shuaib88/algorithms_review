import random

def unique_finder(delivery_ids):
    out_delivering = {}

    for id in delivery_ids:
        if id not in out_delivering:
            out_delivering[id] = True
        else:
            out_delivering.pop(id)

    return out_delivering

def unique_finder(delivery_ids):

    unique_id = 0
    for id in delivery_ids:
        unique_id = unique_id^id
    return unique_id




#test
a = []
for i in range(1,100):
    a.append(i)
    a.append(i)
a.append(103)

random.shuffle(a)

print unique_finder(a)