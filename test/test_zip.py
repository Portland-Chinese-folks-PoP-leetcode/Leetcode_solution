a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(dir(x))
print(list(x))


class Solution:
    def numberToWords(self, num: int) -> str:
        mp = {1: "One",   11: "Eleven",    10: "Ten",
              2: "Two",   12: "Twelve",    20: "Twenty",
              3: "Three", 13: "Thirteen",  30: "Thirty",
              4: "Four",  14: "Fourteen",  40: "Forty",
              5: "Five",  15: "Fifteen",   50: "Fifty",
              6: "Six",   16: "Sixteen",   60: "Sixty",
              7: "Seven", 17: "Seventeen", 70: "Seventy",
              8: "Eight", 18: "Eighteen",  80: "Eighty",
              9: "Nine",  19: "Nineteen",  90: "Ninety"}

        def fn(n):
            """Return English words of n (0-999) in array."""
            if not n:
                return []
            elif n < 20:
                return [mp[n]]
            elif n < 100:
                return [mp[n//10*10]] + fn(n % 10)
            else:
                return [mp[n//100], "Hundred"] + fn(n % 100)

        ans = []
        for i, unit in zip((9, 6, 3, 0), ("Billion", "Million", "Thousand", "")):
            n, num = divmod(num, 10**i)
            print(help(divmod))
            print(n,num)
            ans.extend(fn(n))
            if n and unit:
                ans.append(unit)
        return " ".join(ans) or "Zero"


sol = Solution()
print(sol.numberToWords(123))
