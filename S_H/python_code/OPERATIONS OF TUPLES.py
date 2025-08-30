# Initializing the tuple
my_tuple = ("engine", "transmission", "battery", "steering", "Brakes", "FuelTank") 

# Printing the entire tuple
print(my_tuple)                  # Output: ('engine', 'transmission', 'battery', 'steering', 'Brakes', 'FuelTank')

# Accessing elements by index
print(my_tuple[0])               # Output: 'engine'
print(my_tuple[-1])              # Output: 'FuelTank'

# Slicing the tuple
print(my_tuple[1:4])             # Output: ('transmission', 'battery', 'steering')

# Tuple membership test
print('engine' in my_tuple)      # Output: True

# Iterate through the tuple
for component in my_tuple: 
    print("Car component:", component) 

# Finding the index of an element
print(my_tuple.index("engine"))  # Output: 0

# Counting the occurrence of an element
print(my_tuple.count("Brakes"))  # Output: 1
