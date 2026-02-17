raw=input("Enter all the weights:")
words=raw.split()

weights=[]
for w in words:
    weights.append(int(w))

name=input("Enter your full name:")

name_len=0
for char in name:
    if char!=" ":
        name_len=name_len+1

pli=name_len%3

print(f"L={name_len}")
print(f"PLI={pli}")

light=[]
normal=[]
heavy=[]
overload=[]
invalid=[]

valid_cnt=0
affected_cnt=0

for w in weights:
    if w<0:
        invalid.append(w)

    elif w<=5:
        valid_cnt=valid_cnt+1
        if pli==1 or pli==2:
            affected_cnt=affected_cnt+1
        else:
            light.append(w)
        
    elif w<=25:
        valid_cnt=valid_cnt+1
        normal.append(w)
    
    elif w<=60:
        valid_cnt=valid_cnt+1
        heavy.append(w)

    else:
        valid_cnt=valid_cnt+1

        if pli==0:
            invalid.append(w)
            affected_cnt=affected_cnt+1
        elif pli==2:
            affected_cnt=affected_cnt+1
        else:
            overload.append(w)

print("Total valid weights=",valid_cnt)
print("Affected items=",affected_cnt)
print("Very Light:",light)
print("Normal Load:",normal)
print("Heavy Load:",heavy)
print("Overload:",overload)
print("Invalid:",invalid)
