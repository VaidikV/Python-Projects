# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

check1 = year % 4
check2 = year % 100
check3 = year % 400

print(check1)
print(check2)
print(check3)


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.") 
else:
    print("Not leap year.")

  
