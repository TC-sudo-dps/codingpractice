import sys

# 一定要用迴圈讀取輸入
for line in sys.stdin:
    if line.strip():
        # 把 "1 2" 變成 [1, 2]
        nums = list(map(int, line.split()))
        # 輸出 3
        print(sum(nums))
