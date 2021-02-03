#3-4
math=[] #數學成績清單
total = 0 #總和
high = 0 #最高分
low = 100 #最低分
n = int(input('How many people in this class?')) #輸入班上有多少人

for i in range(n): #跑n個學生次迴圈
    stuname = input('Please input the name:')
    score = int(input('Please input the score:')) #輸入成績
    total = total+score #總和
    math.append(stuname)
    math.append(score) #把成績新增到清單裡

for i in range(1,n*2,2): #比較最高分
    if math[i] > high:
        high = math[i]
        highname = math[i-1]
        
for i in range(1,n*2,2): #比較最低分
    if math[i] < low:
        low = math[i]
        lowname = math[i-1]
    
average = total / n #算平均
print(math) #印出清單
print('average:',average) #印出平均
print('high:',high,highname)
print('low:',low,lowname)

'''
3-4
我只有一個清單，要同時存成績和姓名，
並且計算平均最大值最小值，並顯示出誰最高分 誰最低分
'''