n=int(input("How many buildings? "))
readings=[]
for i in range(n):
    val=int(input("Enter reading for building "+str(i+1)+":"))
    readings.append(val)

print("Readings you entered:", readings)
usage_groups={}
usage_groups["efficient"]=[]
usage_groups["moderate"]=[]
usage_groups["high"]=[]
usage_groups["invalid"]=[]

for e in readings:
    if e<0:
        usage_groups["invalid"].append(e)
    elif e>150:
        usage_groups["high"].append(e)
    elif e>50:
        usage_groups["moderate"].append(e)
    else:
        usage_groups["efficient"].append(e)

total=0
for e in readings:
    if e>=0:
        total=total+e

highest=0
for e in readings:
    if e>=0:
        if e>highest:
            highest=e

lowest=highest
for e in readings:
    if e>=0:
        if e<lowest:
            lowest=e

summary=(total, n, highest, lowest)

print("Efficient (0 to 50):", usage_groups["efficient"])
print("Moderate (51 to 150):", usage_groups["moderate"])
print("High (above 150):", usage_groups["high"])
print("Invalid (below 0):", usage_groups["invalid"])

print("Total Consumption:", summary[0], "units")
print("Number of Buildings:", summary[1])
print("Highest Reading:", summary[2], "units")
print("Lowest Reading:", summary[3], "units")

high_count=len(usage_groups["high"])
efficient_count=len(usage_groups["efficient"])
moderate_count=len(usage_groups["moderate"])

if high_count>3:
    print("WARNING: Overconsumption Detected!")

if summary[0]>600:
    print("WARNING: Energy Waste Detected!")

difference=efficient_count-moderate_count
if difference<0:
    difference=difference*-1
if difference<=1:
    print("Balanced Usage Detected")
if high_count <= 3 and summary[0] <= 600:
    print("Efficient Campus - Everything looks good!")
