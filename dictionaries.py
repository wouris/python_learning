
capitals = {"USA":"Washington DC", 
            "India":"New Dehli", 
            "Russia":"Moscow", 
            "Slovakia":"Bratislava"}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('India')
# capitals.clear

print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for i in capitals.items():
    print(i)