#program 1
n=int(input("Enter the no of elements:"))
total=0
for i in range(n):
    num=float(input("Enter number:"))
    total += num
avg=total/n
print("The average is:",avg)

#program 2
a=input("Enter the Integer:")
a=int(a)
print(a,type(a))

#Program-3
b1=complex(input("Enter one complex number:"))
b2=complex(input("Enter another complex number:"))
b3=float(input("Enter a float number:"))
b4=float(input("Enter another float number:"))
b5=int(input("Enter a num:"))
b6=int(input("Enter another num:"))
print(f"Sum of two complex numbers {b1} and {b2} is {b1+b2}")
print(f"Sum of two float numbers {b3} and {b4} is {b3+b4}")
print(f"Sum of two integer numbers {b5} and {b6} is {b5+b6}")


#program 4
a=input("Enter the Integer:")
b=float(a)
print(b,type(b))

#program 5
a=input("Enter the num:")
b=int(input("Enter another num:"))
#c=a+str(b)
print(a+str(b))
#
#
#
#
#
#
#
#
#
#
# # example 1
#
# n = int(input("Enter a number:"))
# if n == 0:
#     print("Wrong input")
# else:
#     for i in range(n,n+1):
#         val = n*(n*1)
#         print(val)
#
# # example 2
#
# x = 0
# str1="thisismycountryindia"
# for i in str1:
#     x=x-1
#     print(str1[0:x])
# for i in str1:
#     x = x + 1
#     print(str1[0:x])
#
# n=int(input("Enter a num:"))
# x=0
# for i in range (n):
#     x=x+1
#     print("* "*x)
# for i in range (n):
#     x=x-1
#     print("* "*x)
#
# #example -3
#
# a1=1045
# a2 = format(a1,'b')
# print(a2)
# print(format(a1,'o'))
# print(format(a1,'x'))
# a3="100100101"
# a4=int(format(int(a3,2),'d'))
# print(a4)