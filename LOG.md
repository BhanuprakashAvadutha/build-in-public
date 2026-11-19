# LOG
One line per day, newest first: `date · block · what I built · what broke · commit`

- 2026-11-19 · Block 0 · while, break/continue, range, enumerate, zip, dict comps, generators (row 2 L2) · broke: range step read as multiples (1,10,3); generator first written without a parameter · <hash>
- 2026-11-18 · Block 0 · defaults, keyword args, *args, **kwargs, scope, closures, decorators (row 3 L2) · broke: count = count + 1 inside a function → UnboundLocalError · 1aecfcb
- 2026-11-17 · Block 0 · functions: def, return vs print, None, scope, label() + count_apply() · broke: price(a) used outer `job` not its parameter; tool_names() called itself → RecursionError · ac64282
- 2026-11-17 · Block 0 · comprehensions: [expr for x in items if cond], and, len · broke: print("a: ", x) gave a double space · 97303ce
- 2026-11-17 · Block 0 · loops + if/elif/else, counters, job filter · broke: indentation · 41fbbf5
- 2026-11-16 · Block 0 · lists & dicts, nested response["choices"][0] · broke: KeyError vs IndexError · 91fb0de
- 2026-11-16 · Block 0 · types: str/int/float/bool, conversion, / vs // · broke: "7"+str(1) gave 71, not 8 · 1d03cc7
- 2026-11-16 · P · set up build-in-public repo + coach · — · 66e7eca
