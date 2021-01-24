import math

g = 9.81
v0 = 44
deg = 80
x = 0.5
yO = 1

theta = deg * (math.pi / 180)

print(theta)

y = yO + x * math.tan(theta) - (g * x **2) / (2 * (v0 * math.cos(theta)) **2)
print(y)
