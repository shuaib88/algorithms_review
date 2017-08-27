class Fib:

    def __init__(self):
        self.memo = {}


    def fib(self,n):

        if n in [0,1]:
            return n

        if n < 0:
            raise Exception("negative input not allowed")

        if self.memo[n]:
            return self.memo[n]

        result = self.fib(n-1) + self.fib(n-2)

        self.memo[n] = result

        return result