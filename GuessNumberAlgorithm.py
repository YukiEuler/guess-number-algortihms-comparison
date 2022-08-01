factor = [32, 16, 8, 4, 2, 1]
exponent = []
for y in range(1, 101):
    guess = 50
    count = 0
    for x in range(6):
        if guess > y:
            guess = guess-factor[x]
            count += 1
        elif guess < y:
            guess = guess+factor[x]
            count += 1
        elif guess == y:
            count += 1
            break
    exponent.append(count)

half = []
for t in range(1, 101):
    mid = 50
    up = 100
    low = 0
    count = 1
    data = [50]
    while mid != t:
        count += 1
        if mid > t:
            up = mid - 1
        elif mid < t:
            low = mid + 1
        mid = int((up + low)//2)
        data.append(mid)
    half.append(count)

exp = 0
same = 0
div = 0
for k in range(len(half)):
    if exponent[k] > half[k]:
        exp += 1
    elif exponent[k] == half[k]:
        same += 1
    else:
        div += 1
print(f"Exponent method faster for {exp} data")
print(f"Exponent method as fast as half method for {same} data")
print(f"Exponent method slower for {div} data")



