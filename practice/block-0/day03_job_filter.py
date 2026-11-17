# Day 3 - loops + conditions (from Colab, written by me)
# Lines marked "# BROKE:" had bugs; commented out so the file runs.

conversation = [
    {"role": "user", "content": "find AI jobs"},
    {"role": "assistant", "content": "searching..."},
    {"role": "user", "content": "only Hyderabad"},
]

for message in conversation:
    print(message["role"] + ": " + message["content"])

print("---")

for message in conversation:
    if message["role"] == "user":
        print("USER said: " + message["content"])
    else:
        print("(skipping assistant)")

print("---")
count = 0
for message in conversation:
    count = count + 1
print("Total messages: " + str(count))

count = 0
for message in conversation:
    count = count + 1
    print("Total messages: " + str(count))

scores = [45, 82, 67, 91]
passed = 0
for s in scores:
    if s >= 80:
        print(str(s) + " strong")
        passed = passed + 1
    elif s >= 60:
        print(str(s) + " ok")
    else:
        print(str(s) + " retry")
print("Passed: " + str(passed))
print(5 == 5, 5 == "5")

age = [23, 43, 14, 32, 42, 24, 32, 13 , 24 , 24 , 35, 53]
now = 0
for i in age:
    if i >=40:
      now = now + 1
      print(f"{i} is the old age")
    elif i > 30:
        print(f"{i}: this is the best age group")
    else:
        print(f" {i} these are all children")
# BROKE: print(f"{age_above_40}: these are above 40")  -> NameError (never defined; the counter is `now`)
# BROKE: print(f"{age_above_30}: these are above 30")  -> NameError

count = 0
ne = 0
cla = [23, 12, 412, 122, 11, 54, 52, 13]
for i in cla:
    if i > 100:
        count = count + 1
        print("handed to agent", i)
    elif i < 100:
        ne = ne + 1
        print("ignored to agent", i)
print(count, " + these are the old")
# BROKE: print(new, " + these are the new")  -> NameError (typo: variable is `ne`)

tools = ["search", "read_url", "save_note"]
blocked = 0
for t in tools:
    if t == "read_url":
        print("BLOCKED: " + t)
        blocked = blocked + 1
    else:
        print("ok: " + t)
print("Blocked count: " + str(blocked))

# Job filter (step 6):
# For each job in Hyderabad: salary >= 10 -> APPLY, otherwise SKIP. Count APPLY.
now = 0
jobs = [
    {"title": "AI Engineer", "city": "Hyderabad", "salary": 12},
    {"title": "Data Analyst", "city": "Pune", "salary": 7},
    {"title": "Agent Engineer", "city": "Hyderabad", "salary": 16},
    {"title": "ML Intern", "city": "Hyderabad", "salary": 4},
]
for job in jobs:
    if job["city"] == "Hyderabad":
        if job["salary"] >= 10:
            print(f"APPLY: {job['title']} ({job['salary']} L)")
            now = now + 1
        else:
            print(f"SKIP: {job['title']} ({job['salary']} L)")
print("Apply count: " + str(now))
