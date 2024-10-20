class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return_num = 0
        for i in range(left, right + 1):
            binary_count = format(i, "b").count("1")
            if binary_count == 1:
                continue

            is_prime = True
            if binary_count > 2:
                for num in range(2, int(binary_count**0.5) + 1):
                    if binary_count % num == 0:
                        is_prime = False
                        break
            if is_prime:
                return_num += 1
        return return_num