import random

def random_int(min_val, max_val):
    return random.randint(min_val, max_val)

def random_list(count, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(count)]

def shuffle_list(items):
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled