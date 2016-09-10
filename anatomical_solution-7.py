#- Find candidate pairs for I, J
pairs = []
for candidate in candidates:
    pair = [candidate, P // candidate]
    pairs.append(pair)
pairs
# [[120, 221.0], [130, 204.0], [136, 195.0], [156, 170.0], [170, 156.0], [195, 136.0]]
