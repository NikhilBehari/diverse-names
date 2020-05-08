import random
import linecache


def generate_name(n=1):
    file = "names.txt"
    sample_lines = random.sample(range(19948), n)
    return [linecache.getline(file, i) for i in sample_lines]
