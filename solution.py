import sys

# 讀取標準輸入中的每一行
for line in sys.stdin:
    # 確保這一行不是空的（避免讀到檔案結尾的空白行）
    if line.strip():
        try:
            # 將讀入的字串拆開，並轉換成整數
            a, b = map(int, line.split())
            # 輸出計算結果
            print(a + b)
        except ValueError:
            # 如果這行資料格式不對，就跳過
            continue
