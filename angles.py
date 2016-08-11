from math import sin
from math import pi

def square(x):
    return x * x

angles = [1.0, 2.0, 2.0]

normalization = 0.0
for a in angles:
    normalization += square(sin(a))

print('normalization', normalization)

s = 0.0
for a in angles:
    for b in angles:
        s += square(sin(a)) * min(square(sin(b)), square(sin(a-b)))

s /= normalization

print('s', s)

opt = 987654321.0
for i in range(0, 10000):
	ss = 0.0
	for a in angles:
		ss += square(sin(a - (2*pi*i / 10000.0)))
	opt = min(opt, ss)

print('opt', opt)

print('ratio', s / opt)
