class Solution:
    def smallestDiff(self, arr):
        min = sndMin = 2 ** 31
        for e in arr:
            if min > e:
                sndMin = min
                min = e
            elif sndMin > e > min:
                sndMin = e
        return sndMin - min
