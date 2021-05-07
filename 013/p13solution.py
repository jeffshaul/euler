total = 0
with open('numbers.txt') as f:
    for line in f:
        total += int(line)
print(total) # Full sum
print(str(total)[0:10]) # First 10 digits