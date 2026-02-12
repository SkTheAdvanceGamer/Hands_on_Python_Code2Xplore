digit = int(input("Enter last digit of your register number:"))

n = int(input("Enter number of elements in list:"))
data = []

for i in range(n):
    element = input("Enter element: ")

    if element.isdigit():
        data.append(int(element))
    else:
        data.append(element)
num=[]
str=[]

c1=0
c2=0

for item in data:
    if type(item)==int:
        num.append(item)
        c1+=1

    if type(item)==str:
        if item!="":
            str.append(item)
            c2+=1

result=digit%2

if result==0:
    print("Digit is even, reversing number")

    lst=[]
    idx=len(num)
    while idx>0:
        lst.append(num[idx-1])
        idx-=1

    num=lst

if result==1:
    print("Digit is odd, revering string")
    lst=[]
    idx=len(str)
    while(idx>0):
        lst.append(str[idx-1])
        idx-=1

    str=lst

print("Number List:",num)
print("String List:",str)
print("Total Numbers:",c1)
print("Total Strings:",c2)
print("My digit is", digit)
if digit % 2 == 0:
    print("Even so reversed numbers")
else:
    print("Odd so reversed strings")