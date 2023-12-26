import random
def gen_random(num_count, begin, end):
    list = [int(random.uniform(begin, end)) for i in range(num_count)]
    return list
