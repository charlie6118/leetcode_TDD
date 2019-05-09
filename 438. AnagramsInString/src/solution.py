class Solution(object):
    def findAnagrams(self, s: str, p: str):
        r = []
        if len(s) < len(p): return r

        d = {}
        for c in p:
            d[c] = d.get(c, 0) + 1
        counter = len(d)
        head, tail = 0, 0

        while tail < len(s):
            tmp = s[tail]
            if tmp in d:
                d[tmp] -= 1
                if d[tmp] == 0:
                    counter -= 1
            tail += 1

            print(d, head, tail, counter)

            while counter == 0:
                tmpc = s[head]
                if tmpc in d:
                    d[tmpc] += 1
                    if d[tmpc] > 0:
                        counter += 1
                
                if (tail - head) == len(p):
                    r.append(head)
                head += 1     
        print(r, head, tail, counter)
        return r