# Day 2b - tuples, sets, set comps, string methods + spaced-repetition reviews (from Colab, written by me)
# Lines marked '# BROKE:' / '# NOTE:' are commented out so the file runs.

# NOTE: R1, generator + continue (learned yesterday). An LLM stream sometimes sends empty pieces (""). Write a generator stream_tokens(parts) that yields each piece but skips the empty ones.

def stream_tokens(parts):
    for part in parts:
        if part == "":
            continue
        yield part

for t in stream_tokens(["Hi", "", "there", ""]):
    print(t)

# NOTE: closure (from 2 days ago). An agent is allowed only a limited number of tool calls. Write the exact output:

def make_limit(max_calls):
    def check(n):
        return n <= max_calls
    return check

ok = make_limit(3)
print(ok(2), ok(5))

# NOTE: functions, list comprehensions and dicts (from 3 days ago). Write a function last_user_message(msgs)
# NOTE: that returns the content of the last message whose role is "user". Use a list comprehension. This:

msgs = [
    {"role": "user", "content": "find AI jobs"},
    {"role": "assistant", "content": "searching..."},
    {"role": "user", "content": "only Hyderabad"},
    {"role": "assistant", "content": "found 3"},
]

def last_user_message(msgs):
   user_content = [a["content"] for a in msgs if a["role"] == "user"]
   return user_content[-1]


print(last_user_message(msgs))

msgs = [
    {"role": "user", "content": "find AI jobs"},
    {"role": "assistant", "content": "searching..."},
    {"role": "user", "content": "only Hyderabad"},
    {"role": "assistant", "content": "found 3"},
]

def last_user_message(msgs):
   user_content = [a["content"] for a in msgs if a["role"] == "user"]
   return user_content[-1]


print(last_user_message(msgs))

msg = [
    {"role": "user", "content": "find AI jobs"},
    {"role": "assistant", "content": "searching..."},
    {"role": "user", "content": "only Hyderabad"},
    {"role": "assistant", "content": "found 3"},
]

def roam(msgs):
    soap = [a["content"] for a in msgs if a["role"] == "user"]
    return soap[-1]

print(roam(msg))

point = (17.4, 78.5)
lat, lon = point
print(lat, lon)

bro = (12, 43)
a, b = bro
print(b, a)

roles = ("user", "assistant", "system")
print(roles[1], len(roles))
# BROKE: roles[2] = "rbing"   -> TypeError: 'tuple' object does not support item assignment (on purpose)

used = ["search", "read_url", "search", "search", "save_note", "bring", "brings"]

br = {a.lower() for a in used}
print(br)

ac = [a.lower() for a in used]
print(ac)

bc = (a.lower() for a in used)
print(bc)

bhanu = " this is so t alen nted and han dsome        "

a = bhanu.startswith(" this")

text = "this is the best time, im practicing the python, at daily with consistencey and ,i fee l very god and avong athe best i itme in life i thin,k its a thetime where i ,can ge tht 2. ,5 lask in mo,nth so this is the bes,t time"

print(text[-12:])

data = "plan;act;check"
parts = data.split(";")
print(parts)
print(" -> ".join(parts))
print(data[:4])

a = "bhanu is the good boy"

t = ("a", "b")
x, y = t
print(y + x)

tags = "ai, rag, AI , agents".split(",")
print(len({tag.strip().lower() for tag in tags}))

# NOTE: Write a function initials(text) that returns the first letter of each word, in uppercase, joined with .:

# BROKE: print(initials("machine learning engineer"))   -> NameError: initials not defined yet

# BROKE: def initials(text):
# BROKE:      words = ".". join(text)   -> first attempt: join before split -> dots between letters
# BROKE:      w = words.upper().split(" ")
# BROKE:      return w

# BROKE: print(initials("machine learning engineer"))

def initials(text):
    words = text.split()
    return ".".join(word[0].upper() for word in words)

print(initials("machine learning engineer"))

def initials(text):
    word = text.upper().split()
    b = [b[0] for b in word]
    return ".".join(b)

print(initials("machine learning engineer"))

