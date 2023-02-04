'''
https://www.youtube.com/watch?v=OQ5jsbhAv_M

Niave recursive algorithm
'''

mem_recursive = {}
def fib(n):
    if mem_recursive.get(n): return mem_recursive[n]
    if n <=2: f = 1
    else:
        f = fib(n-1) + fib(n-2)
        mem_recursive[n] = f
    return f

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(25))
print("\n")


'''
Actually,I need only remember the "last" two values!!
'''

fib2_bottom_up = {}
def f2(k):
    for k in range(1, k+1):
        if k <=2: f = 1
        else: f = fib2_bottom_up[k-2] + fib2_bottom_up[k-1]

        fib2_bottom_up[k] = f
    return fib2_bottom_up[k]

print(f2(25))



