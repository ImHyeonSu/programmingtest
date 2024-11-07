class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        result = "1"
        for _ in range(2, n + 1):
            temp = ""
            count = 1
            current = result[0]

            for i in range(1, len(result)):
                if result[i] == current:
                    count += 1
                else:
                    temp += str(count) + current
                    current = result[i]
                    count = 1
            temp += str(count) + current
            result = temp

        return result
