
# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("What is your name? - ")
    if name != "":
        break

phone_num = "+421-929-384-928"

for i in phone_num:
    if i == "-":
        continue
    print(i, end="")

for i in range(0, 10+1):
    if i == 6:
        pass
    else:
        print(i)