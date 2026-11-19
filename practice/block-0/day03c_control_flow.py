# Day 3c - while, break/continue, range, enumerate, zip, dict comps, generators (from Colab, written by me)
# Lines marked '# BROKE:' crash; commented out so the file runs.

n = 10
while n > 7:
    print(n)
    n = n - 1
print("end", n)

n = 15
while n>5:
  print(n)
  n = n-1
print("end", n)

n = 0
while n < 12:
  print(n)
  n = n + 1
print(f"this is end {n}")

all = ["search", "drive", "kill", "bring", "size", "dash"]

for a in all:
   if a == "kill":
     break
     print("danger", a)
   print(a)

all = ["search", "drive", "kill", "bring", "size", "dash"]
# BROKE: for t in all  enumerate(i, t)   -> SyntaxError (enumerate written wrong)
# BROKE:   print(t)       # easy to forget, or put in the wrong place

# BROKE: for t in tools:   -> NameError: tools not defined yet
# BROKE:     if t == "DELETE_ALL":
# BROKE:         print("dangerous! stopping")
# BROKE:         break
# BROKE:     print("run", t)

n = 22
while n >= 0:
  if n == 18:
    n = n - 1
    continue
  if n == 12:
    print(n)
    break
  print(n)
  n = n - 1

n = 0
while n > 24:
  if n == 4:
    n = n - 1
    continue
    print(n)
  if n == 19:
    break
    print(n)
  print(n)
  n = n - 1

x = 1
while x < 20:
    x = x * 3
print(x)

x = 3
# BROKE: while y < 400:   -> NameError: y never defined (meant y = x?)
# BROKE:     y = x * 4
# BROKE: print(y)

# 1. Using a dictionary comprehension to map each number to its square:
print({i: i**2 for i in range(2, 13, 2)})

# 2. Using dict() and zip() to pair a range of keys with a range of values:
keys = range(2, 13, 2)
values = ["a", "b", "c", "d", "e", "f"]
print(dict(zip(keys, values)))

# BROKE: for i in t enumarate(i t))     # easy to forget, or put in the wrong place   -> SyntaxError (enumerate written wrong)

tools = ["search", "read_url", "save_note"]
for t, i in enumerate(tools):
    print(i, t)

brok = ["say", "drink", "ras", "br"]
for i, t in enumerate(brok, start=2):
 print(f"{i}. {t}")

steps = ["plan", "act", "check"]

for i, item in enumerate(steps, start=1):
    print(f"item {i}: {item}")

position = ["bris", "darling", 3, 4, 5, 6]
rule = ["desk", "runs", "fdsf", "fsaf", "bring", "desk"]

price = {position : rule for position, rule in zip(position, rule)}
print(price)

scores = {"Bhanu": 82, "Ravi": 45, "Shiva": 91}
passed = {name: s for name, s in scores.items() if s >= 50}
print(passed)

scores = {"Bhanu": 82, "Ravi": 45, "Shiva": 91}
print({a: b for a, b in scores.items() if b ==45})

position = ["bris", "darling", "sdas", "asd", "asd", "asd"]
rule = ["desk", "runs", "fdsf", "fsaf", "bring", "desk"]

a = {a: b for a, b in zip(position, rule) if a == "asd"}
print(a)

def stream():
    yield "Hello"
    yield "from"
    yield "the"
    yield "model"

for word in stream():
    print(word)

def stream2():
    print("  (making Hello)")
    yield "Hello"
    print("  (making from)")
    yield "from"

for word in stream2():
    print("got:", word)

def countdown():
    yield 3
    yield 2
    yield 1
    yield "go!"

for x in countdown():
    print(x)

def with_return():
    return 1
    return 2
    return 3

def with_yield():
    yield 1
    yield 2
    yield 3



for x in with_yield():
    print(x)

import time

def slow_return():
    words = []
    for w in ["Hello", "from", "the", "model"]:
        time.sleep(1)
        words.append(w)
    return words


print(slow_return())

def slow_yield():
    for w in ["Hello", "from", "the", "model"]:
        time.sleep(1)
        yield w
for w in slow_yield():
    print(w)

import time
def bring():
  for i in  ["i have to tell you", "its now or never"]:
      time.sleep(2)
      yield i


for i in bring():
  print(i)

def countdown():
    yield 3
    yield 2
    yield 1
    yield "go!"

for x in countdown():
    print(x)

import time

all_items = ["bring", "tewt", "sarsd", "tersds"]

def my_generator():
    for i in all_items:
        yield i
        time.sleep(1)

for i in my_generator():
    print(i)

squares = (n * n for n in [1, 2, 3])
print(squares)
for s in squares:
    print(s)

n = 0
while n < 6:
    n = n + 1
    if n == 2:
        continue
    if n == 5:
        break
    print(n)

n = 0
while n < 22:
  n = n + 1
  if n == 4:
     continue
  if n ==18:
     break
  print(n)

print({k: v for k, v in zip(["x", "y", "z"], range(1, 4)) if v != 2})

print({a: b for a, b in zip(["manu", "krish", "bring"], range(2, 12, 2)) if b != 4})

def numbered():
    for i, k in enumerate(["plan", "act", "check"], start=1):
        yield f"{i}. {k}"

# Call the generator and iterate through it to print each yielded string
for item in numbered():
    print(item)

def numbered(items):
    for i, item in enumerate(items, start=1):
        print("  kitchen makes", i)
        yield f"{i}. {item}"


g = numbered(["back", "fdsfss", "dsfsd"])
for i in g:
    print(i)

