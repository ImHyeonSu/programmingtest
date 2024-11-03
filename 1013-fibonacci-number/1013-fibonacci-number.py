class Solution:
    def fib(self, n: int) -> int:
        fib_list = [0, 1]
        if n == 0 or n == 1:
            return fib_list[n]
        tmp_n = 1
        while tmp_n <= n:
            tmp_n += 1
            append_num = fib_list[tmp_n - 2] + fib_list[tmp_n - 1]
            fib_list.append(append_num)
        return fib_list[n]