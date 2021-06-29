
food = ["pizza","hamburger","hotdog","spaghetti"]

food[0] = "sushi"

print(food[0])

food.append("ice cream") # adds an element
food.remove("hotdog") # removes an element
food.pop() # remove the last element
food.insert(0,"cake") # insert an element at given index
food.sort() # sort the list alphabetically
# food.clear() # remove all elements from the list

for i in food:
    print(i)