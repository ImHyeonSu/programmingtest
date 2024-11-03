class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result_list = []
        for i in range(n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                result_list.append("FizzBuzz")
            elif (i + 1) % 3 == 0:
                result_list.append("Fizz")
            elif (i + 1) % 5 == 0:
                result_list.append("Buzz")
            else:
                result_list.append(str(i + 1))
        return result_list
