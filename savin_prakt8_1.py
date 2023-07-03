print("Введите натуральное число не более 10 000")
n=int(input())
m=[]

for i in range(1,n+1):
    print("Введите",i,"-е число")
    m.append(int(input()))

m.reverse()
print(m)
