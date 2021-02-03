#3-2
math=[] #數學成績清單
total = 0 #總和
high = 0 #最高分
low = 100 #最低分
n = int(input('How many people in this class?')) #輸入班上有多少人

for i in range(n): #跑n個學生次迴圈
    score = int(input('Please input the score:')) #輸入成績
    total = total+score #總和
    if high < score: #比較最高分
        high = score
    if low > score: #比較最低分
        low = score
    math.append(score) #把成績新增到清單裡
    
average = total / n #算平均
print(math) #印出清單
print('average:',average) #印出平均
print('high:',high)
print('low:',low)
