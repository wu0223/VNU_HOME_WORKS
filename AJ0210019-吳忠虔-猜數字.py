# 請上傳你的程式碼
import random

# 產生密碼（範圍1~100之間的整數）
passcode = random.randint(1, 100)
# print(f'答案為:{passcode}')

# 建立存放範圍最新範圍的變數
min = 1     # 存放比答案小的範圍
max = 100   # 存放比答案大的範圍

# 玩家開始猜
while True:
    guess = int(input(f'請猜密碼, 範圍為{min}~{max}之間的數字:'))

    # 判斷猜測的數字有沒有在範圍內
    if guess > max or guess < min:
        print('Ooops, 這數字有問題，請重新輸入。')

    # 猜對離開遊戲
    elif guess == passcode:
        # 跳離迴圈
        break

    # 數字比答案大，則更新max變數
    elif guess > passcode:
        max = guess

    # 數字比答案小，則更新min變數
    else:
        min = guess
