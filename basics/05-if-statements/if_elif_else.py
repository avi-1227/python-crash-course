# Often, you'll need to test more than two possible situations and to evaluate these you can use Python's if-elif-else syntax.
'''for example
    1. Admission for anyone under age 4 is free.
    2. Admission for anyone between the ages of 4 and 18 is $25.
    3. Admission for anyone age 18 or older is $40.
'''
age = 12

if age < 4:
    print("Your admission cost is $0.")

elif age < 18:
     print("Your admission cost is $25.")

else:
    print("Your admission cost is $40.")