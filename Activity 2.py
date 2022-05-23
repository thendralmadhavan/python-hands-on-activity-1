'''num1=float(input("enter a num:"))
if(num1>0):
    print("the number is postive")
elif(num1<0):
    print("the number is negative")
else:
    print("the number is zero")'''

'''num=int(input("enter a number:"))
if(num%2==0):
    print("even")
else:
    print("odd")'''

'''year=int(input("enter a year:"))
if(year%400==0)and(year%100==0):
    print(year,"is a leap year")
elif(year%4==0)and(year%100!=0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")'''

'''a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
print(max(a,b,c))'''


'''a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if(a>b)and(a>c):
    print("a is the largest number")
elif(b>a)and(b>c):
    print("b is the largest number")
else:
    print("c is the largest number")'''

'''flag=False
num=int(input("enter a number:"))
if num>1:
    for i in range(2,num):
        if(num%i==0):
            flag=True
            break
if flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")'''

'''lower=int(input("enter lower:"))
upper=int(input("enter upper:"))
print("prime numbers between",lower,"and",upper,"are")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)'''

'''num=int(input("enter a num:"))
factorial=1
if num<0:
    print("factorial does not exist for negative numbers")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial of",num,"is",factorial)'''

'''num=int(input("enter a number:"))
for i in range(1,11):
    print(num,"X",i,"=",num*i)'''

'''num=int(input("enter a num:"))
n1,n2=0,1
count=0
if num<=0:
    print("Please enter a positive number")
elif num==1:
    print("fibonacci sequence upto",num)
else:
    print("fibonacci sequence")
    while count<num:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1'''

'''num=int(input("enter a num:"))
sum=0
a=num
while a>0:
    digit=a%10
    sum += digit**3
    a//=10
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")'''


'''lower=int(input("enter lower:"))
upper=int(input("enter upper:"))
for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    a=num
    while a>0:
        digit=a%10
        sum += digit**order
        a//=10
    if num==sum:
        print(num)'''

'''rows=int(input("enter number of rows:"))
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")'''

'''dict={'a':'juice','b':'grill','c':'corn'}
for key,value in dict.items():
    print(key,value)'''

'''num=9207
rev_num=0
while num!=0:
    digit=num%10
    rev_num=rev_num*10+digit
    num//=10
print("reversed number is:",str(rev_num))'''

'''base=int(input("enter"))
exponent=int(input("enter"))
result=1
while exponent!=0:
    result*=base
    exponent-=1
print(result)'''
    
    



