n = int(input("Enter the number of words: "))
words = []
for i in range(n):  
    word = input(f"Enter word {i + 1}: ")
    words.append(word)
d = {}
for word in words:
    key = ''.join(sorted(word))
    if key not in d:
        d[key] = []
    d[key].append(word)
    
print(list(d.values()))