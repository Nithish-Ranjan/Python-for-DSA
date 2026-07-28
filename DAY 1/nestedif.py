# name = input("enter username")
# user = "admin"
# pas = input("enter password")
# password = "NRJ1022"

# if user == name:
#     if pas == password:
#         print("Valid credentials")
#     else:
#         print("invalid password")
        
# else:
#     print("invalid username")



marks = int(input())
income = int(input())
if marks>=80:
    if income<200000:
        print("scholarship is provided")
    else:
        print("no scholarship")
else:
    print("no scholarship")