#Python - "One liner"

print(
'\n'.join(
    ''.join(
        ' *'[(z:=0, c:=x/50+y/50j, [z:=z*z+c for _ in range(99)], abs(z))[-1]<2]
        for x in range(-100,25)
    )
    for y in range(-50,50)
))

#Python - "Functional" Based on the "One liner" approach.

from functools import reduce

def mandelbrot(x, y, c): return ' *'[abs(reduce(lambda z, _: z*z + c, range(99), 0)) < 2]

print('\n'.join(''.join(mandelbrot(x, y, x/50 + y/50j) for x in range(-100, 25)) for y in range(-50, 50)))