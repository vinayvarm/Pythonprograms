# import random
import jwt

#
# game_images = ['rock', 'paper', 'scissors']
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])
#
# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# heights=input('enter list of heights').split(',')
# print(heights)
# count=0
# sum=0
# for i in heights:
#     print(i)
#     sum=sum+i
#     count=count + 1
# avg=sum/count
# print(avg)
#

# cname=input('enter city name')
# bname=input('enterbandname')
#
# comname=cname+bname
# print(comname)

code=jwt.encode({'pretty':'printed'},'dont tell anyone')
print(code)
