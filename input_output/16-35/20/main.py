# Formatted Table of Factorials

import math

for x in range(1,10):
    values = f"{x:{x}d}{math.factorial(x):10d}"
    print(values)
    print("-"*len(values))

