import math

def stdDev(arr):
    squared = 0
    length = len(arr)
    total = sum(arr)
    mean = total / length
    for n in arr:
        squared += pow(n - mean, 2)
    print(f"{math.sqrt(squared / length):.1f}")

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    stdDev(vals)
