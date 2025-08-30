# Initializing the dictionary
car = { 
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964 
} 

# Copying the dictionary
x = car.copy() 
print(x) 
print("\n") 

# Getting a value by key
x = car.get("model") 
print("model:", x) 
print("\n") 

# Getting all items (key-value pairs)
x = car.items() 
print(x) 
print("\n") 

# Getting all keys
x = car.keys() 
print(x) 

# Adding a new key-value pair
car["color"] = "white" 
print(x) 
print("\n") 

# Removing the last inserted key-value pair
car.popitem() 
print(car) 
print("\n") 

# Updating the dictionary
car.update({"color": "Red"}) 
print(car) 
print("\n") 

# Getting all values
x = car.values() 
print(x) 
print("\n") 

# Getting the length of the dictionary
print("Length of car dictionary =", len(car)) 
print("\n") 

# Clearing the dictionary
car.clear() 
print(car)
