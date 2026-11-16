vocab = {"hel": 1, "lo": 2, " wor": 3, "ld": 4,
         "h": 5, "e": 6, "l": 7, "o": 8, " ": 9, "w": 10, "r": 11, "d": 12}

def tokenize(text):
    ids = []
    i = 0
    while i < len(text):
        for size in range(len(text) - i, 0, -1):
            piece = text[i:i + size]
            if piece in vocab:
                ids.append(vocab[piece])
                i += size
                break
        else:
            raise ValueError("unknown character: " + text[i])
    return ids

for t in ["hello world", "hello", "held", "world"]:
    ids = tokenize(t)
    print(repr(t), "->", ids, " tokens:", len(ids), " characters:", len(t))
