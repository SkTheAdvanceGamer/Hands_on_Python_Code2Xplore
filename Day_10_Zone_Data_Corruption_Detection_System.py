import random
import math
import copy
import numpy as np
import pandas as pd

roll_last = int(input("Enter last digit of your roll number: "))
seed_val = int(input("Enter any seed number (try 10, 20, 30 for 3 test cases): "))
random.seed(seed_val)

def make_zones():
    zones = []
    for i in range(1, 16):
        z = {
            "zone": i,
            "metrics": {
                "traffic": random.randint(50, 300),
                "pollution": random.randint(20, 150),
                "energy": random.randint(30, 200)
            },
            "history": [random.randint(10, 90) for _ in range(5)]
        }
        zones.append(z)
    return zones

def personalize(zones, last_digit):
    if last_digit % 2 != 0:
        return zones[3:] + zones[:3]
    else:
        return zones[::-1]

def custom_risk_score(t, p, e, history):
    avg_h = sum(history) / len(history)
    weighted = (t * 0.40) + (p * 0.35) + (e * 0.25)
    score = math.log(weighted + 1) + math.sqrt(avg_h) / 10
    return round(score, 4)

def mutate(zones):
    for z in zones:
        z["metrics"]["traffic"] += random.randint(5, 25)
        z["metrics"]["pollution"] += random.randint(3, 15)
        z["metrics"]["energy"] += random.randint(2, 10)
        z["history"].append(random.randint(50, 120))
    return zones

def manual_corr(x, y):
    n = len(x)
    mx, my = sum(x)/n, sum(y)/n
    top = sum((x[i]-mx)*(y[i]-my) for i in range(n))
    bot = math.sqrt(sum((x[i]-mx)**2 for i in range(n)) * sum((y[i]-my)**2 for i in range(n)))
    return round(top/bot, 4) if bot != 0 else 0.0

def find_clusters(risky_set, total):
    clusters, streak = [], []
    for z in range(1, total+1):
        if z in risky_set:
            streak.append(z)
        else:
            if len(streak) >= 2:
                clusters.append(tuple(streak))
            streak = []
    if len(streak) >= 2:
        clusters.append(tuple(streak))
    return clusters

def get_status(max_r, min_r, stability, anomaly_count):
    if anomaly_count == 0 and stability > 0.05:
        return "System Stable"
    elif anomaly_count <= 3 and stability > 0.02:
        return "Moderate Risk"
    elif anomaly_count <= 6 or (max_r - min_r) > 3.0:
        return "High Corruption Risk"
    else:
        return "Critical Failure"


original = make_zones()
original = personalize(original, roll_last)

shallow = copy.copy(original)
deep = copy.deepcopy(original)

print("\nBEFORE mutation:")
print("original traffic zone[0]:", original[0]["metrics"]["traffic"])
print("shallow  traffic zone[0]:", shallow[0]["metrics"]["traffic"])
print("deep     traffic zone[0]:", deep[0]["metrics"]["traffic"])

mutate(shallow)

print("\nAFTER mutating shallow only:")
print("original traffic zone[0]:", original[0]["metrics"]["traffic"])
print("shallow  traffic zone[0]:", shallow[0]["metrics"]["traffic"])
print("deep     traffic zone[0]:", deep[0]["metrics"]["traffic"])

print("\nWhy shallow corrupts original:")
print("Shallow copy shares inner dicts with original.")
print("Changing shallow also changes original nested data.")
print("Deep copy is fully independent so original stays safe.")

traffic, pollution, energy, risk, zones_list = [], [], [], [], []

for z in shallow:
    t = z["metrics"]["traffic"]
    p = z["metrics"]["pollution"]
    e = z["metrics"]["energy"]
    h = z["history"]
    traffic.append(t)
    pollution.append(p)
    energy.append(e)
    risk.append(custom_risk_score(t, p, e, h))
    zones_list.append(z["zone"])

np_risk = np.array(risk)
mean_r = np.mean(np_risk)
var_r = np.var(np_risk)
std_r = np.std(np_risk)

print("\nMean Risk  :", round(float(mean_r), 4))
print("Variance   :", round(float(var_r), 4))
print("Std Dev    :", round(float(std_r), 4))
print("Corr T&P   :", manual_corr(traffic, pollution))
print("Corr T&E   :", manual_corr(traffic, energy))

df = pd.DataFrame({
    "Zone": zones_list,
    "Traffic": traffic,
    "Pollution": pollution,
    "Energy": energy,
    "Risk_Score": risk
})
print("\n", df.to_string(index=False))

threshold = float(mean_r) + float(std_r)
anomaly_zones = {zones_list[i] for i in range(len(risk)) if risk[i] > threshold}
print("\nAnomaly Zones:", sorted(anomaly_zones))

risky_set = {zones_list[i] for i in range(len(risk)) if risk[i] > float(mean_r)}
clusters = find_clusters(risky_set, 15)
stability = round(1 / float(var_r), 6) if var_r > 0 else 999.0
max_r = round(max(risk), 4)
min_r = round(min(risk), 4)

print("Risk Clusters     :", clusters)
print("Stability Index   :", stability)
print("Summary Tuple     :", (max_r, min_r, stability))

status = get_status(max_r, min_r, stability, len(anomaly_zones))
print("\nFINAL DECISION:", status)