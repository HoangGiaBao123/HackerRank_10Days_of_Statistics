import os
import sys

def weightedMean(X, W):
    weightSum = sum(W)
    valWithWeight = sum([x * w for x, w in zip(X, W)])
    print(round(valWithWeight / weightSum, 1))

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))
    weightedMean(vals, weights)
