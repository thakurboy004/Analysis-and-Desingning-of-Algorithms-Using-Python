'''Implement the algorithm (Algo_1) presented below and discuss which task this algorithm
performs. Also, analyse the time complexity and space complexity of the given algorithm.
Further, implement the algorithm with following modification: replace m = ⌈2n/3⌉ with m =
⌊2n/3⌋, and compare the tasks performed by the given algorithm and modified algorithm.
Algo_1(A [0 ... n-1])
{
if n = 2 and A[0] > A[1]
swap A[0] ↔ A[1]
else if n > 2
m = ⌈2n/3⌉
Algo_1 (A [0 .. m − 1])
Algo_1 (A [n – m .. n − 1])
Algo_1 (A [0 .. m − 1])
}
'''
import math
def Algo_1(A, left, right):
    n = right - left + 1
    if n == 2 and A[left] > A[left+1]:
        A[left], A[left+1] = A[left+1], A[left]
    elif n > 2:
        m = math.ceil(2 * n / 3)
        Algo_1(A, left, left+m-1)
        Algo_1(A, right-m+1, right)
        Algo_1(A, left, left+m-1) 

def Algo_2(A, left, right):
    n = right - left + 1
    if n == 2 and A[left] > A[left+1]:
        A[left], A[left+1] = A[left+1], A[left]
    elif n > 2:
        m = math.floor(2 * n / 3)
        Algo_2(A, left, left+m-1)
        Algo_2(A, right-m+1, right)
        Algo_2(A, left, left+m-1)
        
if __name__ == '__main__':
    a = [9, 7, 34, 645, 78, 23, 1, 70]
    Algo_2(a, 0, len(a)-1)
    print('Sorting the array using Algo_2', a)
    Algo_1(a, 0, len(a)-1)
    print('Sorting the array using Algo_1', a)
