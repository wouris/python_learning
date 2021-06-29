# create a substring by extracting elements from another string
# fisrt_name[start:stop:step]

name = "Samuel Mrazik"

first_name = name[:6]
last_name = name[7:]
funky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website = "https://google.com"
website2 = "https://youtube.com"

slice = slice(8,-4)
print(website[slice] + " " + website2[slice])