# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1+name2
combined_name = combined_name.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
true = t+r+u+e

l = combined_name.count("t")
o = combined_name.count("r")
v = combined_name.count("u")
e = combined_name.count("e")

love = l+o+v+e

final = int(str(true) + str(love))
if (final<10) or (final>90):
    print(f"Your love is {final}, you go together like coke and mentos.")
elif(final>40) and (final<50):
    print(f"Your score is {final}, you are alright together.")
else:
    print(f"Your score is {final}")