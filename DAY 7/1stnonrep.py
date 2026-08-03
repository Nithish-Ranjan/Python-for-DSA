b = [5, 10, 15, 5, 20, 30, 35]
for i in range(len(b)):
    if b.count(b[i]) == 1:
        print("First non-repeated element:", b[i])
        break