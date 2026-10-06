import random
import sys
probability = 0.01
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()
    for line in lines:
        the_sample = random.random()
        if the_sample < probability:
            print(line)
