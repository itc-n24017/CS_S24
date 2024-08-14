import math
import random

total = 0
num_inside = 0
sim_pi = 0
while not math.isclose(sim_pi, math.pi, abs_tol=1e-5):
    x = random.random()
    y = random.random()
    l = pow(x**2 + y**2, 0.5)
    total += 1
    if l <= 1:
        num_inside += 1
    sim_pi = 4 * num_inside / total
print(sim_pi)
print(total)

