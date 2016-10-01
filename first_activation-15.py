# Create the mean volume across all the task volumes
# Then create the mean volume across all the rest volumes
# Hint: remember the `axis` keyword.
on_mean = on_volumes.mean(axis=-1)
off_mean = off_volumes.mean(axis=-1)
