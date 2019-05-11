class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 0: return []
        if len(digits) == 1: return dic[digits]
        
        result = [dic[digits[0]]]
        i = 1
        while i < len(digits):
            fst = result.pop()
            snd = dic[digits[i]]
            tmp = []
            for charF in fst:
                for charJ in snd:
                    tmp.append(charF + charJ)
            result.append(tmp)
            print(result)
            i += 1
        return result.pop()