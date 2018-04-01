from formula import refund
from random import random
import json
d = {}
for i in range(10):
    d[int(random()*99999) + 100000] = (int(random()*3000) + 7300, int(random()*100) + 40)

print(f(d, 8800))
