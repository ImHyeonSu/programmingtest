class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num_mul = 0;
        detect_num = 0;
        while detect_num <= n:
            detect_num = 2 ** num_mul
            if(detect_num == n):
                return True
            num_mul += 1
        return False


