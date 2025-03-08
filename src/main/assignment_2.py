import numpy as np

def euler_method(f, t0, y0, h, n):
    for _ in range(n):
        y0 += h * f(t0, y0)
        t0 += h
    return y0

def runge_kutta_method(f, t0, y0, h, n):
    for _ in range(n):
        c1 = h * f(t0, y0)
        c2 = h * f(t0 + h/2, y0 + c1/2)
        c3 = h * f(t0 + h/2, y0 + c2/2)
        c4 = h * f(t0 + h, y0 + c3)
        y0 += (c1 + 2*c2 + 2*c3 + c4) / 6
        t0 += h
    return y0

def func(t, y):
    return t - y**2

if __name__ == "__main__":
    t0, y0, h, n = 0, 1, 2/10, 10

    euler_result = euler_method(func, t0, y0, h, n)
    runge_kutta_result = runge_kutta_method(func, t0, y0, h, n)

    print( euler_result )
    print()
    print( runge_kutta_result )
