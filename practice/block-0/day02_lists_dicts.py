# Day 2 - lists & dicts (from Colab, written by me)
# Lines marked "# BROKE:" were break-it exercises; commented out so the file runs.

tools = ["search", "apply", "find", "calcel"]
print(tools[3])

tools = ["search", "read_url", "save_note"]   # positions 0, 1, 2
# BROKE: print(tools[3])  -> IndexError: list index out of range

bro = { "name": "bhanu", "clas": "6th"}
print(bro["clas"])
bro['clas'] = "12th"
print(bro["clas"])

bro["age"] = 34
print(bro)

brek = ["name", "rask", "bring", "rsask", "oom", "hi"]
print(brek[0])
print(brek[-1])

tools = ["search", "read_url", "save_note"]
job = {"title": "AI Engineer", "city": "Hyderabad"}

last_tool = tools[len(tools) -1]
print("Last tool: " + last_tool)
print("City: " + job["city"])

conversation = [{"role": "user", "content": "find AI jobs"}, {"role": "assistant", "content": "searching..."}]
conversation.append({"role": "user", "content": "only Hyderabad"})
conversation[1]["content"] = "found 12 jobs"

print("Message: " + str(len(conversation)))
print("First role: " + conversation[0]["role"])
print("Last content: " + conversation[len(conversation) -1]["content"])
print("Updated: " + conversation[1]["content"])

response = {"choices": [{"message": {"content": "hi"}}]}
print(response["choices"][0]["message"]["content"])

response = {"choices": [{"message": {"content":{"name": "shiva"}}}]}
print(response["choices"][0]["message"]["content"]["name"])

data = {"jobs": [{"title": "AI Engineer", "skills": ["python", "rag"]}]}
print(data["jobs"][0]["skills"][1])

tools = ["a", "b"]
# BROKE: print(tools[2])  -> IndexError: list index out of range

a = [{"x": 1}, ["y"]]
print(a[1])
