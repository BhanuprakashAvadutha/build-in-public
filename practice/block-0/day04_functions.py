# Day 4 - functions (from Colab, written by me)
# Lines marked "# BROKE:" crash; commented out so the file runs.

print("a:", 5)
print("a: " + str(5))
print("x", "y" + "z")

def greet(name):
    return "Hello, " + name

msg = greet("Bhanu")
print(msg)
print(greet("Shiva"))

def decide(job):
    if job["city"] == "Hyderabad" and job["salary"] >= 10:
        return "APPLY"
    return "SKIP"

jobs = [
    {"title": "AI Engineer", "city": "Hyderabad", "salary": 12},
    {"title": "Data Analyst", "city": "Pune", "salary": 7},
]
for job in jobs:
    print(job["title"] + " -> " + decide(job))

# BUG (works by accident): parameter is `a`, but the body uses the outer `job`.
def price(a):
  if job["salary"] > 9:
    return "we need to applt to this job " + job["title"]
  return "skip"
jobs = [
    {"title": "AI Engineer", "city": "Hyderabad", "salary": 12},
    {"title": "Data Analyst", "city": "Pune", "salary": 7},
]

for job in jobs:
 print(price(job))

def add(a, b):
    return (a + b)

x = add(2, 3)
print(x)

def dive(a, b):
    print(a - b)

x = dive(32,54)
print(x)

def add(a, b):
    print(a + b)

x = add(2, 3)
print(x)

def f():
    return "a"
    print("b")

print(f())

def check(score):
    if score >= 50:
        return "pass"
    return "fail"

print(check(50), check(49))

def double(n):
    return n * 2

print(double(4) + 1)

def greet(name):
    return "Hello, " + name

print(greet("Bhanu"))
# BROKE: print(greet())  -> TypeError: greet() missing 1 required positional argument: 'name'

jobs = [
    {"title": "AI Engineer", "city": "Hyderabad", "salary": 12},
    {"title": "Data Analyst", "city": "Pune", "salary": 7},
    {"title": "Agent Engineer", "city": "Hyderabad", "salary": 16},
    {"title": "ML Intern", "city": "Hyderabad", "salary": 4},
]

def no_apply(jobs):
    count = 0
    for job in jobs:
        if job["salary"] < 10:
            count += 1
    return count

print(no_apply(jobs))

# Step 6 - written from a blank file (pasted in chat)
def label(job):
    if job["salary"] >= 10:
        return "APPLY: " + job["title"]
    return "SKIP: " + job["title"]

def count_apply(jobs):
    count = 0
    for job in jobs:
        if job["salary"] >= 10:
            count += 1
    return count


for job in jobs:
    print(label(job))

print("apply count:", count_apply(jobs))

# Step 7 teach-back
# Q2 fix: price now uses its own parameter (job), not an outer variable
def price(job):
  if job["salary"] > 9:
    return "apply " + job["title"]
  else:
    return "skip"

print(price({"title": "Big Job", "salary": 50}))

# Q3: a tool-like function that returns a list (first try recursed forever:
#     return tool_names(tools)  -> RecursionError)
tools = [{"name": "search"}, {"name": "read_url"}]

def tool_names(tools):
   return [t["name"] for t in tools]
a = tool_names(tools)
print(a)
