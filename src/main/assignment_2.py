import numpy as np

def neville(x_vals, y_vals, x):
    n = len(x_vals)
    Q = np.zeros((n, n))
    Q[:, 0] = y_vals
    
    for j in range(1, n):
        for i in range(n - j):
            Q[i, j] = ((x - x_vals[i + j]) * Q[i, j - 1] + (x_vals[i] - x) * Q[i + 1, j - 1]) / (x_vals[i] - x_vals[i + j])
    
    return Q[0, n - 1]

def newton_forward_diff_table(x_vals, y_vals):
    n = len(x_vals)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_vals
    
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = (diff_table[i + 1, j - 1] - diff_table[i, j - 1]) / (x_vals[i + j] - x_vals[i])
    
    return diff_table

def newton_interpolation(x_vals, y_vals, x):
    diff_table = newton_forward_diff_table(x_vals, y_vals)
    n = len(x_vals)
    approx = y_vals[0]
    term = 1
    
    for i in range(1, n):
        term *= (x - x_vals[i - 1])
        approx += diff_table[0, i] * term
    
    return approx

def hermite_interpolation(x_vals, y_vals, dy_vals):
    n = len(x_vals)
    z = np.zeros(2 * n)
    Q = np.zeros((2 * n, 2 * n))
    
    for i in range(n):
        z[2 * i] = z[2 * i + 1] = x_vals[i]
        Q[2 * i, 0] = Q[2 * i + 1, 0] = y_vals[i]
        Q[2 * i + 1, 1] = dy_vals[i]
        if i != 0:
            Q[2 * i, 1] = (Q[2 * i, 0] - Q[2 * i - 1, 0]) / (z[2 * i] - z[2 * i - 1])
    
    for j in range(2, 2 * n):
        for i in range(j, 2 * n):
            Q[i, j] = (Q[i, j - 1] - Q[i - 1, j - 1]) / (z[i] - z[i - j])
    
    return Q

def cubic_spline_matrix(x_vals, y_vals):
    n = len(x_vals) - 1
    h = np.diff(x_vals)
    A = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)
    
    A[0, 0] = 1
    A[n, n] = 1
    
    for i in range(1, n):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = (3 / h[i]) * (y_vals[i + 1] - y_vals[i]) - (3 / h[i - 1]) * (y_vals[i] - y_vals[i - 1])
    
    return A, b, np.linalg.solve(A, b)

if __name__ == "__main__":
    pass
