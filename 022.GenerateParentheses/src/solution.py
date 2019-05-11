class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gen(storage, sub_str, left_open, right_open):
            print(storage)
            if left_open > 0:
                gen(storage, sub_str + '(', left_open - 1, right_open)
            if left_open < right_open:
                gen(storage, sub_str +')', left_open, right_open - 1)
            if not left_open and not right_open:
                storage.append(sub_str)
                return storage
        result = []
        gen(result, '', n, n)
        return result        