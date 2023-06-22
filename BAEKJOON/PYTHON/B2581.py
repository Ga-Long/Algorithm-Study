# 소수

def PrimeNum(a): # 소수인지 아닌지 
    if a == 1 : return 0
    for i in range(2,int(a/2)+1):
        if(a % i == 0): #약수 있는 경우
            return 0
    
    else: return 1
            
M = int(input())
N = int(input())

PrimeNumber = []
for i in range(M, N+1):
    if PrimeNum(i) == 1: 
        PrimeNumber.append(i)

if len(PrimeNumber) == 0: print("-1")
else:
    sum = 0
    for i in PrimeNumber:
        sum += i

    print(sum)
    print(PrimeNumber[0])
