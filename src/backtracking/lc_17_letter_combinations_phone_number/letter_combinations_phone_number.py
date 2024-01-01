class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        numbers = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], 
        '6': ['m','n','o'], '7': ['p','q','r', 's'], '8': ['t','u','v'], '9': ['w','x','y','z']}

        def backtrack(i, comb):
            if len(comb) > len(digits):
                return
            if len(comb) == len(digits):
                if ''.join(comb) not in res:
                    res.append(''.join(comb))
            for j in range(i, len(digits)):
                num = digits[j]
                if num in numbers:
                    for number in numbers[num]:
                        comb.append(number)
                        backtrack(j+1, comb)
                        comb.pop()
        if digits == '':
            return res
        backtrack(0, [])
        return res