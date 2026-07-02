# Day 1 - Python script practice
# Goal : check whether particle sizes are acceptable

particle_sizes = [120, 180, 250, 90]

for size in particle_sizes:
    if size < 200:
        print(size, "OK")
    else:
        print(size, "Too large")