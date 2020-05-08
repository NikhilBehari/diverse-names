import random
import linecache
import os


def generate_name(n=1):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(folder_path, 'names.txt')
    sample_lines = random.sample(range(19948), n)
    return [linecache.getline(file, i) for i in sample_lines]
