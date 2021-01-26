import math
g = 9.81
v0 = 44
deg = 80
x = 0.5
y0 = 1

print(math.pi)

theta = deg * (math.pi / 180)
print(theta)

y= y0 + x * math.tan(theta) - (g * x ** 2) / (2 * (v0 * math.cos(theta))** 2)
print(y)






