id=input("Enter your Student ID:")
email=input("Enter your Email:")
password=input("Enter your password:")
ref=input("Enter Referral code:")
approve=True

if " " in id or len(id)!=7:
    approve=False

if approve==True:
    if id[0]!="C" or id[1]!="S" or id[2]!="E" or id[3]!="-" or id[4].isdigit()==False or id[5].isdigit()==False or id[6].isdigit()==False:
        approve=False

if approve==True:
    if " " in email or "." not in email or email.count("@")!=1:
        approve=False

if approve==True:
    if email[0]=="@" or email[len(email)-1]=="@":
        approve=False
    if len(email)>=4:
        if email[len(email)-4]!="." or email[len(email)-3]!="e" or email[len(email)-2]!="d" or email[len(email)-1]!="u":
            approve=False
    else:
        approve=False

if approve==True:
    pos=email.find("@")
    dot=email.find(".",pos+1)
    if dot==-1 or dot<=pos:
        approve=False

if " " in password or len(password)<8:
    approve=False

if approve==True:
    if password[0].isupper()==False or password[0].isalpha()==False:
        approve=False
    digit=False
    if "0"in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
        digit=True
    if digit==False:
        approve=False

if " " in ref or len(ref)!=6:
    approve=False

if approve==True:
    if ref[0]!="R" or ref[1]!="E" or ref[2]!="F" or ref[3].isdigit()==False or ref[4].isdigit()==False or ref[5]!="@":
        approve=False

if approve==True:
    print("APPROVED")
else:
    print("REJECTED")