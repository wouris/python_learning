
name = "samuel mrazik"

print(name)

print("The length of your name is: " + str(len(name)))

print("Your letter 'm' is in position " + str(name.find("m")) + " in your name")

print("Capitalize function: " + str(name.capitalize())) # Only the first letter ( index 0 [column] )

print("Upper function will make your string all uppercase: " + str(name.upper()))

print("Lower function will make your string all lowercase: " + str(name.lower()))

print("Is the string a digit? - " + str(name.isdigit()))

print("Is the string only made of only from aplhabetical letters? - " + str(name.isalpha())) # False, if there's a space in the string

print("There are " + str(name.count("a")) + " 'a' letters in the string") 

print("Letter 'a' has been replaced with 'e': " + str(name.replace("a","e")))

print("Printing string multiple times: " + str(name * 3)) 