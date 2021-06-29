
rows = int(input("How many rows? - "))
columns = int(input("How many columns? - "))
symbol = input("What symbol do you want to use? - ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #end="" to eliminate adding new line to the end of print
    print()