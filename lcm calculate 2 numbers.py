num1 = int(input('enter the 1st number: '))
num2 = int(input('enter the 2nd number: '))
count =1
while True:
    if count%num1==0:
        if count%num2==0:
            print(count)
            break
    count=count+1