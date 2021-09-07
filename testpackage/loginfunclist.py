# names=["vinay","mouli","siva","asish","vishnu"]
# passwords=["dell","asus","lenova","hp","rog"]
#
# i=1
# j=1
# chancesleft=3
# while(i<chancesleft):
#     username = input("enter username")
#     for name in names:
#         if name==username:
#             print(name)
#
#     break


name=input("enter username ")
psw=input("enter password ")



def login(username,password):
    un="vinay"
    pw="dell"
    if username==un:

        if password == pw:
            print("welcome back", username)
        else:
            print("wrong password")
    else:
        print("wrong username")

# login(name,psw)





























        # if username == name:
        #     print("welcome back, now please enter password")
        #     passw = input("enter password")
        #     for password in passwords:
        #         if passw == password:
        #             print("welcome back", username)
        #             i=i+n




















