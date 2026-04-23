import math
import nump1y as np
import pandas as pd


def classify(t, a, e):
    if a > 200 or t > 80:
        return "High Risk"
    elif e > 400:
        return "Energy Critical"
    elif t < 30 and a < 100:
        return "Safe Zone"
    else:
        return "Moderate"


def risk_score(t, a, e):
    base = (t * 0.35) + (a * 0.45) + (e * 0.20)
    bonus = 0
    if t > 70 and a > 150:
        bonus = math.sqrt(t * a) * 0.10
    return round(base + bonus, 2)


def bubble_sort(lst):
    arr = lst.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j]["risk_score"] < arr[j+1]["risk_score"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def city_decision(avg):
    if avg < 60:
        return "City Stable"
    elif avg < 100:
        return "Moderate Risk"
    elif avg < 140:
        return "High Alert"
    else:
        return "Critical Emergency"


def input_zone(zone_number):
    print("Zone", zone_number)
    t = int(input("traffic: "))
    a = int(input("air quality: "))
    e = int(input("energy: "))
    return {"zone": zone_number, "traffic": t, "air_quality": a, "energy": e}


num_zones = int(input("how many zones: "))

data = []
for i in range(1, num_zones + 1):
    zone = input_zone(i)
    data.append(zone)

for z in data:
    z["risk_score"] = risk_score(z["traffic"], z["air_quality"], z["energy"])
    z["log_risk"] = round(math.log(z["risk_score"] + 1), 3)

categories = {}
for z in data:
    categories[z["zone"]] = classify(z["traffic"], z["air_quality"], z["energy"])

df = pd.DataFrame(data)
df["category"] = df["zone"].map(categories)

print(df[["zone", "traffic", "air_quality", "energy", "risk_score", "category"]].to_string(index=False))

risks = np.array(df["risk_score"].tolist())
traffs = np.array(df["traffic"].tolist())

print("avg traffic:", round(np.mean(np.array(df["traffic"].tolist())), 2))
print("avg aqi:", round(np.mean(np.array(df["air_quality"].tolist())), 2))
print("avg energy:", round(np.mean(np.array(df["energy"].tolist())), 2))
print("avg risk:", round(np.mean(risks), 2))

sorted_data = bubble_sort(data)
print("top 3 worst zones")
for i in range(min(3, len(sorted_data))):
    z = sorted_data[i]
    print("zone", z["zone"], "risk", z["risk_score"], categories[z["zone"]])

risk_tuple = (round(float(np.max(risks)), 2), round(float(np.mean(risks)), 2), round(float(np.min(risks)), 2))
print("risk tuple (max avg min):", risk_tuple)

category_set = set(categories.values())
print("categories found:", category_set)

streak = 0
for z in data:
    if categories[z["zone"]] == "High Risk":
        streak += 1
        if streak >= 2:
            print("high risk cluster at zone", z["zone"])
    else:
        streak = 0

variance = round(float(np.var(traffs)), 2)
if variance < 600:
    print("traffic is stable, variance:", variance)
else:
    print("traffic is unstable, variance:", variance)

avg_risk = round(float(np.mean(risks)), 2)
print("final decision:", city_decision(avg_risk))

safe_count = list(categories.values()).count("Safe Zone")
total = len(categories)
pct = round(safe_count / total * 100, 1)
print("safe zones:", safe_count, "out of", total, "(", pct, "%)")
if pct >= 50:
    print("this is a smart city")
else:
    print("this is not a smart city yet")


print("test cases")

test_cases = [
    {"name": "extreme pollution", "traffic": 20,  "air_quality": 295, "energy": 150},
    {"name": "zero traffic",      "traffic": 0,   "air_quality": 80,  "energy": 200},
    {"name": "random spike",      "traffic": 95,  "air_quality": 270, "energy": 490},
]

for tc in test_cases:
    t = tc["traffic"]
    a = tc["air_quality"]
    e = tc["energy"]
    cat = classify(t, a, e)
    score = risk_score(t, a, e)
    print(tc["name"], "-> category:", cat, "| risk score:", score)