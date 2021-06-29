#logical operators - and, or, not(reverse True, False)

temp = float(input("What is the temperature outside? "))

if temp >= 0 and temp <=30:
    print("Temperature is good today.")

elif temp < 0 or temp > 30:
    print("Temperature is bad today.")

# elif not(temp < 0 or temp > 30):
#     print("Temperature is bad today.")

