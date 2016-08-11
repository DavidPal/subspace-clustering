from math import sin
from math import pi

m = -100000.0
N = 300

for i in range(N):
	for j in range(N):
		L = sin(2*pi*(i+j) / N) ** 2
		R = 2*sin(2*pi*i/N)**2 + 2*sin(2*pi*j/N)**2
		m = max(m, L-R)
		print(i, j, L-R, m)
