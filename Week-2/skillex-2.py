#program 1
n=int(input("Enter a num:"))
res=1
for i in range(1,n+1):
    res *= i
print(f"The factorial of number {n} is {res}")

#program 2
for i in range(1,8):
    print(7,"*",i,"=",(7*i))


#program 3
s1,s2,s3=map(int,input("Enter the length of sides for triangle:").split())
hyp=0
if s1>s2:
    if s1>s3:
        hyp=s1
elif s2>s3:
    hyp=s2
else:
    hyp=s3
if hyp==s1:
    if s2**2 + s3**2 == hyp**2:
        print("It is Right Triangle")
    else:
        print("Not a Right Triangle")
elif hyp==s2:
    if s1**2 + s3**2 == hyp**2:
        print("It is Right Triangle")
    else:
        print("Not a Right Triangle")
else:
    if s1**2 + s2**2 == hyp**2:
        print("It is Right Triangle")
    else:
        print("Not a Right Triangle")



#program 4
n=int(input("Enter no of astriks needed:"))
x=0
for i in range (n):
    print("* "*x)
    x = x + 1
for i in range (n):
    print("* "*x)
    x = x - 1

#
#program 5
binary_sequence=input("Enter 4-binary digit numbers:")
binary_num=binary_sequence.split(",")
divisible_by_5=[binary for binary in binary_num if int(binary,2)%5==0]
print(",".join(divisible_by_5))