'''Implement the multiplication of two N-bit numbers (using Divide and Conquer Strategy) and naive multiplication method. Compare these methods in terms of time taken using N-bit
numbers where n=4, 8, 16, 32 and 64.'''

import time
def karatsuba(x,y):
    if x<10 or y<10 :
        return x*y
    else:
        n=max(len(str(x)),len(str(y)))
        half=n//2
        a=x//(10**(half))
        b=x%(10**(half))
        c=y//(10**(half))
        d=y%(10**(half))
        ac=karatsuba(a,c)
        bd=karatsuba(b,d)
        ad_plus_bc=karatsuba(a+b,c+d)-ac-bd
        return ac*(10**(2*half))+ad_plus_bc*(10**half)+bd
    
start=time.time()
print(karatsuba(12653,419626))
end=time.time()
print(f"Execution time :{end-start}")
