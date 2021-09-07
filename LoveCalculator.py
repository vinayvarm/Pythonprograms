print('enter first name and last name without spaces')
name1=input('enter name ')
name2=input('enter name ')
combined_string=name1 + " " +  name2
lowercase_string=combined_string.lower()

print(lowercase_string)

t=lowercase_string.count("t")
r=lowercase_string.count("r")
u=lowercase_string.count("u")
e=lowercase_string.count("e")

count_true=t+r+u+e

print(count_true)

l=lowercase_string.count("l")
o=lowercase_string.count("o")
v=lowercase_string.count("v")
e=lowercase_string.count("e")
count_love=l+o+v+e
print(count_love)
scor=str(count_true) + str( count_love)
print('your score is',scor)
score=int(scor)


if score<10 or score>90:
    print(f'your score is {score}', 'yo go like coke and mentos')
elif score<40 and score>50:
    print(f'your score is{score}','u are alright together')
else:
    print(f'your score is {score}',' --------')