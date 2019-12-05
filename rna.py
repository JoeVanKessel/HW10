from collections import defaultdict
from heapq import *
import math
allowed  = set(['AU','UA','CG','GC','GU','UG'])

def best(x):
    #max = 0
    def _best(i, j):
        if (i ,j) in opt:

            return opt[i, j]
        curr = -1

        for s in range(i, j):
            if _best(i, j-1) > curr:
                curr = _best(i, j-1)
                back[i, j] = -1

            if x[s] + x[j] in allowed:

                if _best(i,s-1) + _best(s+1, j-1) + 1 > curr:
                    curr = _best(i,s-1) + _best(s+1, j-1) + 1
                    #if s == 0:
                    #    back[i, j] = [(s+1, j-1)]
                    #else:
                    back[s, j] = [(s, s), (s, j)]
                    back[i, j] = [(i, s), (s, j)]

                    #if j-s == s:
                        #back[i, j] = [(i, j-s-1), (s+1, j)]
                    #elif j-s == i:
                        #back[i, j] = [(i, s-1), (s, j)]
                    #else:
                        #back[i, j] = [(i, j-s), (s, j)]


        opt[i, j] = curr
    #    print("")
        print(back)
        return curr

    def solution(i, j):
        print(i, j)
        if i > j:
            return ""
        if i == j:
            return "."
        if back[i, j] == -1:
            return solution(i, j-1)
        if back[i, j] == [(i, i), (i, j)]:
            return "(%s)" % solution(i+1, j-1) + solution(i,i)
        else:
            return "(%s)" % solution(back[i, j][0][0], back[i, j][0][1]) + solution(back[i, j][1][0], back[i,j][1][1])


    def total():
        visited = []
        for i, j in back:
            if back[i, j] != -1:
                visited += [(back[i, j][0][0]), (back[i, j][0][1]), (back[i, j][1][0]), (back[i, j][1][1])]


                #break
        #for i, j in back:
            #if back[i, j] != -1:
                #if (back[i, j][0][1], back[i, j][0][0]) not in visited:
                #    visited += [(back[i, j][0][1], back[i, j][0][0])]
                #if (back[i, j][1][0], back[i, j][1][1]) not in visited:
                #    visited += [(back[i, j][1][0], back[i, j][1][1])]

        #for i in visited:
            #print(i)
        #print(len(visited)*2)

        return 1



    opt = defaultdict(int)
    back = {}
    n = len(x)
    for i in range(n):
        opt[i, i] = 0
        opt[i, i-1] = 0

    #max = 0

    return _best(0, n-1), solution(0, n-1), total()
