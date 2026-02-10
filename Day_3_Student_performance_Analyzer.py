name=input("Enter your name:")
letter_count=0

for i in name:
    letter_count+=1

pin=int(input("Enter PIN(based on your name):"))

if pin==letter_count:
    print("Welcome ",name," Access granted\n")

    n=int(input("Enter number of studentd:"))

    marks=[]

    snum=1
    while snum<=n:
        m=int(input("Enter marks of student:"))
        marks.append(m)
        snum+=1

    valid_students=0
    failed_students=0

    for m in marks:
        if m<0 or m>100:
            print(m," ->Invalid")
        elif m>=90:
            print(m," -> Excellent")
            valid_students+=1
        elif m>=75:
            print(m,"-> Very Good")
            valid_students+=1
        elif m>=60:
            print(m,"-> Good")
            valid_students+=1
        elif m>=40:
            print(m,"->Average")
            valid_students+=1
        elif m>=0:
            print(m,"->Fail")
            valid_students+=1
            failed_students+=1

    invalid_students=n-valid_students

    print("Total Valid Students:",valid_students)
    print("Total Failed Students:",failed_students)
    print("Total Invalid Studnets:",invalid_students)

else:
    print("Wrong pin access denied")
    print("Pin is the number of letters in your name")