import statistics

def quartiles(arr):
    nums = sorted(arr)
    q2 = statistics.median(nums)
    L = [n for n in nums if n < q2]
    U = [n for n in nums if n > q2]
    q1 = statistics.median(L)
    q3 = statistics.median(U)
    return [int(q1), int(q2), int(q3)]
