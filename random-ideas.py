# small utilities, no deps

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

def clamp(value, low, high):
    return max(low, min(value, high))

# cleanup later
