# Day 4b - defaults, keyword args, *args, **kwargs

# worked example: default + keyword args
def search(query, limit=3):
    return "searching '" + query + "' (limit " + str(limit) + ")"

print(search("AI jobs"))
print(search("AI jobs", 10))
print(search(limit=5, query="RAG"))

# written by me
def plan(goal, *steps, done=False):
    return f"{goal} | {len(steps)} steps | done={done}"


def tool(name, ** params):
     return f"{name} ({len(params)} params)"


print(plan("learn python", "loops", "functions"))
print(plan("ship", "commit", "push", done=True))
print(tool("search", query="RAG", limit=5))
