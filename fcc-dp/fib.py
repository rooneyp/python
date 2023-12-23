

def fib_recursive(n, first=0, second=1, loop=0):
    # n+1 iterations
    if loop > n - 1:
        return first
    else:
        return fib_recursive(n, second, first + second, loop + 1)

def fib_ex1(n):
    #2^n iter: 25 iter for n=7
    if n <= 2: return 1
    return fib_ex1(n - 1) + fib_ex1(n - 2)

if __name__ == '__main__':
    #https://www.youtube.com/watch?v=oBt53YbR9Kk
    print(fib_ex1(7))
    # for n in range(1,8+1):
    #     # print(f'n={n}, Xn={fib_recursive(n)}\tdo_fib_recursive')
    #     print(f'n={n}, Xn={fib_ex1(n)}\tfib_ex1')
