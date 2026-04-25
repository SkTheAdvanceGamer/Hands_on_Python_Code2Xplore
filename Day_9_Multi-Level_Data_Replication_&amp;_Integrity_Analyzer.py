def generate_data():
    roll = input("Enter your roll number: ")
    last_digit = int(roll[-1])

    users = [
        {
            "id": 1,
            "data": {"files": ["a.txt", "b.txt"], "usage": 500}
        },
        {
            "id": 2,
            "data": {"files": ["c.txt"], "usage": 300}
        }
    ]

    return users, last_digit


def replicate_data(original):
    assigned = original

    shallow = list(original)

    deep = []
    for user in original:
        new_user = {}
        new_user["id"] = user["id"]
        new_data = {}
        new_data["files"] = list(user["data"]["files"])
        new_data["usage"] = user["data"]["usage"]
        new_user["data"] = new_data
        deep.append(new_user)

    return assigned, shallow, deep


def modify_data(shallow, last_digit):
    for user in shallow:
        if last_digit % 2 == 0:
            user["data"]["files"].append("new_file.txt")
        else:
            if len(user["data"]["files"]) > 0:
                user["data"]["files"].pop(0)

        user["data"]["usage"] = user["data"]["usage"] + 200

    return shallow


def check_integrity(snapshot, original, shallow, deep):
    leakage_count = 0
    safe_count = 0
    overlap_count = 0

    for i in range(len(original)):

        uid = original[i]["id"]
        snap_files = set(snapshot[i])
        orig_files = set(original[i]["data"]["files"])
        deep_files = set(deep[i]["data"]["files"])
        shallow_files = set(shallow[i]["data"]["files"])

        print("--- User ID:", uid, "---")

        if snap_files != orig_files:
            print("Data Leakage: original data was changed unexpectedly")
            leakage_count = leakage_count + 1
        else:
            print("No Leakage: original data is safe")
            safe_count = safe_count + 1

        if snap_files == deep_files:
            print("Consistency: deep copy is unaffected")
            safe_count = safe_count + 1
        else:
            print("Consistency Issue: deep copy was changed")
            leakage_count = leakage_count + 1

        common_files = snap_files & shallow_files
        overlap_count = overlap_count + len(common_files)
        print("Overlap Detection (set):", common_files)

        if snap_files != orig_files:
            print("Mutation Depth: inner list was changed (deep level mutation)")
        else:
            print("Mutation Depth: no inner change detected")

        print()

    print("Integrity Report Tuple:")
    print("(leakage_count, safe_count, overlap_count) =", (leakage_count, safe_count, overlap_count))

    return (leakage_count, safe_count, overlap_count)


roll_input = input("Enter your roll number: ")
last_digit = int(roll_input[-1])

users, last_digit = generate_data()

snapshot = []
for user in users:
    snapshot.append(list(user["data"]["files"]))

print()
print("--- BEFORE ---")
print("Original Data:")
for user in users:
    print("id:", user["id"], "| files:", user["data"]["files"], "| usage:", user["data"]["usage"])

assigned, shallow, deep = replicate_data(users)

print()
print("Assignment (same object as original):")
for user in assigned:
    print("id:", user["id"], "| files:", user["data"]["files"], "| usage:", user["data"]["usage"])

modify_data(shallow, last_digit)

print()
print("--- AFTER ---")
print("Original Data (check if changed):")
for user in users:
    print("id:", user["id"], "| files:", user["data"]["files"], "| usage:", user["data"]["usage"])

print()
print("Shallow Copy Result:")
for user in shallow:
    print("id:", user["id"], "| files:", user["data"]["files"], "| usage:", user["data"]["usage"])

print()
print("Deep Copy Result:")
for user in deep:
    print("id:", user["id"], "| files:", user["data"]["files"], "| usage:", user["data"]["usage"])

print()
print("Why did the inner list get affected in original?")
print("Because shallow copy only copies the outer list.")
print("The inner data dictionary still points to the same memory location.")
print("So when we changed files inside shallow copy, the original also changed.")
print("Deep copy made a completely new copy at every level so it stayed unchanged.")

print()
print("--- INTEGRITY REPORT ---")
check_integrity(snapshot, users, shallow, deep)