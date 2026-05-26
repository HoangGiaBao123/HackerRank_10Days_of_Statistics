def findMedian(arr):
    if len(arr) % 2 != 0:
        return arr[len(arr) // 2]
    return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2

def interQuartile(values, freqs):
    nums = []
    for num, freq in zip(values, freqs):
        nums.extend([num] * freq)
    nums.sort()
    lower_half = []
    upper_half = []
    if len(nums) % 2 == 0:
        lower_half = nums[:len(nums) // 2]
        upper_half = nums[len(nums) // 2:]
    else:
        lower_half = nums[:len(nums) // 2]
        upper_half = nums[len(nums) // 2 + 1:]
    q1 = findMedian(lower_half)
    q3 = findMedian(upper_half)
    print(f"{q3 - q1:.1f}")
    
if __name__ == '__main__':
    n = int(input().strip())
    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    interQuartile(val, freq)
