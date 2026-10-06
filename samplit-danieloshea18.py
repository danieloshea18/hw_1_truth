import random
import sys
probability = 0.01
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()
    for line in lines:
        sample = random.random()
        if sample < probability:
            print(line)
