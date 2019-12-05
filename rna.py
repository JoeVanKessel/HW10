allowed  = set(['AU','UA','CG','GC','GU','UG'])
from collections import defaultdict
def best(x):
    def _best(i, j):
        if (i, j) in opt:
            return opt[i, j]

        curr = 0
        for k in range(i, j):
            if _best(i, k) + _best(k+1, j) > curr:
                curr = _best(i, k) + _best(k+1, j)
                back[i, j] = k
        if x[i] + x[j] in allowed:
            if _best(i+1, j-1) + 1 > curr:
                curr =  _best(i+1, j-1) + 1
                back[i, j] = -1

        opt[i, j] = curr

        return curr


    def solution(i, j):
        if i == j:
            return '.'
        if i > j:
            return ''
        k = back[i, j]
        if k == -1:
            return '(%s)' % solution(i + 1, j-1)
        else:
            return solution(i, k) + solution(k+1, j)



    opt = defaultdict(int)
    back = {}
    n = len(x)
    for i in range(n):
        opt[i, i] = 0
        opt[i, i-1] = 0
    return _best(0, n-1), solution(0, n-1)
