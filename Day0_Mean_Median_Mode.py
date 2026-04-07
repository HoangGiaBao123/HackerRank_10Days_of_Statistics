import statistics
if __name__ == '__main__':
    length = int(input())
    nums = list(map(int, input().split()))
    mean = sum(nums) / length
    print(mean)
    median = 0
    sorted_nums = sorted(nums)
    if length % 2 != 0:
        median = sorted_nums[length // 2]
    else:
        median = (sorted_nums[length // 2] + sorted_nums[length // 2 - 1])/2
    print(median)
    mode = statistics.mode(sorted_nums)
    print(mode)
