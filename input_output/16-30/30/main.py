# Simulate a progress bar from 1 to 100, updating a single console line (e.g., [#### ] 40%). Use a short delay each iteration.
import math
from time import sleep

delay = 0.00001

width = 40
total = 10000
for x in range(1,total):
    percentage = (x/total)*100
    filled = max(1,math.floor(x*width/total))
    bar = "#" * filled + " "*(width-filled)
    print(f"\r[{bar}] {percentage:3f}%",end="",flush=True)
    sleep(delay)
