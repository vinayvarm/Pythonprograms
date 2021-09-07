username="vikram"
password="dell@90"

# Userlogin using while loop
# i=0
# n=3
# count=4
# chancesleft=3
# while i<=3:
#     name = input("enter username ")
#     if username==name:
#         print("welcome back to login enter password")
#         passw=input("enter password")
#         if password==passw:
#             print("welcomeback",username)
#             i=i+count
#
#         else:
#             print("wrong password, login again")
#             i=i+n
#     else:
#         print("invalid username you have",chancesleft,"chancesleft")
#         i=i+1
#         chancesleft=chancesleft-1
#         if i==count:
#             print("Account blocked visit tomorrow")
#############################     user login using break and continue                   ##################################################
i,n=0,3
count=4
chancesleft=3
while i<=n:
    name = input("enter username ")
    if username == name:
        print("welcome back, To login enter password")
        passw = input("enter password")
        if password == passw:
            print("welcomeback", username)
            i = i + count
        else:
            print("please enter correct password")
            break
    else:
        print("invalid username you have",chancesleft,"chancesleft")
        i=i+1
        chancesleft=chancesleft-1
        if i==count:
            print("limit exceed")
        continue






































