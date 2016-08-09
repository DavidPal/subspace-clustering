import math

def square(x):
    return x * x

angles = [1.0]

normalization = 0.0
for a in angles:
    normalization += square(math.sin(a))

print('normalization', normalization)

s = 0.0
for a in agles:
    for b in angles:
        s += square(math.sin(), ) 
