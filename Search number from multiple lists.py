numlist=int(input("Enter number list"))
lis=[]
for i in range(numlist):
    lis.append(list(map(int, input("Enter the numbers of array").rstrip().split())))
n=int(input("Enter number to search"))
for j in lis:
    for i in j:
        if i==n:
            print(1)
            break
    else:
        print(0)