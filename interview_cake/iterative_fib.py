def fib(n):

    if n==0:
        return 0

    if n==1:
        return 1

    previous_fib = 0
    current_fib = 1

    while (n-1)>0:

        old_previous = current_fib
        current_fib = current_fib + previous_fib
        previous_fib = old_previous
        n -= 1

    return current_fib

#test
print fib(4)