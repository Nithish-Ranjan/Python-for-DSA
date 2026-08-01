n = input("enter password: ")
al = 0
num = 0
spe = 0
nc = len(n)
for i in range(nc):
    if n[i].isalpha():
        al += 1
    elif n[i].isdigit():
        num += 1
    else:
        spe += 1
        
if al >= 1 and num >= 1 and spe >= 1:
    print("Strong Password")
else:
    print("Weak Password")