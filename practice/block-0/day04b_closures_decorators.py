# Day 4b - closures + decorators (from Colab, written by me)

# --- closures ---
def make_greeter(greeting):          # outer function: takes the SETTING
    def greet(name):                 # inner function: takes the actual input
        return greeting + ", " + name    # uses the outer greeting
    return greet                     # hands back the inner FUNCTION (no brackets!)

hello = make_greeter("Hello")        # hello is now a greet that remembers "Hello"
hi = make_greeter("Hi")              # hi is a greet that remembers "Hi"

print(hello("Bhanu"))
print(hi("Shiva"))
print(hello("Ravi"))

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(5))

def two(n):
    def brt(m):
        return n*m
    return brt

br = two(2)

print(br(2))

# --- decorators ---
def log_calls(func):                  # takes a FUNCTION as input
    def wrapper(query):               # the new version
        print("LOG: calling", func.__name__)
        result = func(query)          # run the ORIGINAL function
        print("LOG: done")
        return result
    return wrapper                    # hand back the new version (a closure: it remembers func)

def search(query):
    return "results for " + query

search = log_calls(search)            # replace search with its logged version
print(search("RAG"))

def add_stars(func):
    def new_func():
        print("*****")     # paper on top
        func()             # the gift: the original hello
        print("*****")     # paper on the bottom
    return new_func

@add_stars                 # ← "wrap the next function with add_stars"
def hello():
    print("hello")

hello()

def tool(name, limit=3, **opts):
    return f"{name} {limit} {opts}"

print(tool("search", city="Goa"))

def can(func):
  def new():
    print("*****")
    func()
    print("*****")
  return new

@can
def hello():
  print("hello")

# my own decorator (written from scratch)
def ban(n):
  def car():
    print("----------")
    n()
    print("----------")
  return car


@ban
def menu():
    print("tea")
    print("coffee")


menu()

# gate Q3: decorator that runs a function twice
def twice(ou):
  def new_fun():
      ou()
      ou()
  return new_fun

@twice
def hi():
    print("hi")

hi()

# "another way" - works by accident: ou() runs twice while the f-string is built,
# but the string itself is ' None None' and gets thrown away.
def twice_fstring(ou):
  def new_fun():
     f" {ou()} {ou()}"
  return new_fun
