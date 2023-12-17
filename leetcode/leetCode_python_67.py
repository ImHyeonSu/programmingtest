class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        result = ""
        last = 0
        counter = 0

        while counter < min(len(a), len(b)):
            if a[counter] == "1" and b[counter] == "1":
                counter += 1
                if last == 1:
                    result += "1"
                else:
                    result += "0"
                last = 1
            elif a[counter] == "1" or b[counter] == "1":
                counter += 1
                if last == 1:
                    last = 1
                    result += "0"
                else:
                    result += "1"
            else:
                counter += 1
                if last == 1:
                    last = 0
                    result += "1"
                else:
                    result += "0"
        if (max(len(a), len(b)) - min(len(a), len(b))) != 0:
            for i in range(min(len(a), len(b)), max(len(a), len(b)), 1):
                if len(a) > len(b):
                    if last == 1 and a[i] == "1":
                        print("6")
                        last = 1
                        result += "0"
                    elif last == 1 and a[i] == "0":
                        last = 0
                        result += "1"
                    elif last == 0 and a[i] == "0":
                        result += "0"
                    else:
                        last = 0
                        result += "1"
                else:
                    if last == 1 and b[i] == "1":
                        last = 1
                        result += "0"
                    elif last == 1 and b[i] == "0":
                        last = 0
                        result += "1"
                    elif last == 0 and b[i] == "0":
                        result += "0"
                    else:
                        last = 0
                        result += "1"
        if last == 1:
            result += "1"
            return result[::-1]
        else:
            return result[::-1]


a = Solution()
print(a.addBinary("100", "110010"))
