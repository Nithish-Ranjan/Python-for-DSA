str = input()
lst = list(str)
vow =0
cons=0
for i in lst:
    if i not in "AEIOUaeiou":
        cons+=1
    else:
        vow+=1
        
print("Vowels:",vow," Consonant:",cons)