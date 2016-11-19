new_data = data.copy()
new_data[new_data > top_95_thresh] = top_95_thresh
new_data.max()
# memmap(722.0, dtype=float32)
