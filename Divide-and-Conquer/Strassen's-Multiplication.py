'''Implement the strassen’s multiplication method (using Divide and Conquer Strategy) and
naive multiplication method. Compare these methods in terms of time taken using the nXn
matrix where n=3, 4, 5, 6, 7 and 8 (compare in bar graph)'''

# Naive Method
def multiply(A, B, C):
    C=np.zeros((n,n))
    for i in range(n):
        for j in range( n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
                
# Stressen's Multiplication Method
def strassen_algorithm(x, y):
    if x.size == 1 or y.size == 1:
        return x * y

    n = x.shape[0]
    
    if n % 2 == 1:
        x = np.pad(x, (0, 1), mode='constant')
        y = np.pad(y, (0, 1), mode='constant')

    m = int(np.ceil(n / 2))
    a = x[: m, : m]
    b = x[: m, m:]
    c = x[m:, : m]
    d = x[m:, m:]
    e = y[: m, : m]
    f = y[: m, m:]
    g = y[m:, : m]
    h = y[m:, m:]
    p1 = strassen_algorithm(a, f - h)
    p2 = strassen_algorithm(a + b, h)
    p3 = strassen_algorithm(c + d, e)
    p4 = strassen_algorithm(d, g - e)
    p5 = strassen_algorithm(a + d, e + h)
    p6 = strassen_algorithm(b - d, g + h)
    p7 = strassen_algorithm(a - c, e + f)
    result = np.zeros((2 * m, 2 * m), dtype=np.int32)
    result[: m, : m] = p5 + p4 - p2 + p6
    result[: m, m:] = p1 + p2
    result[m:, : m] = p3 + p4
    result[m:, m:] = p1 + p5 - p3 - p7
    return result[: n, : n]

import numpy as np
import matplotlib.pyplot as plt
import time

if __name__ == "__main__":
    n=int(input("Enter size of matrix"))

    x = np.random.randint(1,9,size = (n,n))
    y = np.random.randint(1,9,size = (n,n))
    print("Matrix A:")
    print(x)
    print("Matrix B:")
    print(y)
    print('Matrix multiplication result strassen: ')
    start=time.perf_counter()
    print(strassen_algorithm(x, y))
    end = time.perf_counter()
    t1=end-start
    print("time=",end-start)
    
    print('Matrix multiplication result naive: ')
    start=time.perf_counter()
    print(multiply(x, y, n))
    end = time.perf_counter()
    t2=end-start
    print("time=",end-start)
    
    
    times=[t1,t2]
    method=["Strassens","Naive"]
    plt.bar(method, times,width = 0.4)
    plt.xlabel("Method")
    plt.ylabel("Time")
    plt.title(f"Comparison n={n}")
    plt.show()

