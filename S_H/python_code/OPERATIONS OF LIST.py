# Initializing the list
my_list = ['cement', 'bricks', 'sand', 'steel bar']

# Accessing elements
print(my_list[0])        # Output: 'cement'
print(my_list[2])        # Output: 'sand'
print(my_list[-3])       # Output: 'bricks'
print(my_list[1:3])      # Output: ['bricks', 'sand']
print(my_list[0:])       # Output: ['cement', 'bricks', 'sand', 'steel bar']

# Modifying elements
my_list[1] = 'concrete'  
print(my_list)           # Output: ['cement', 'concrete', 'sand', 'steel bar']

# Appending an element
my_list.append('paint')  
print(my_list)           # Output: ['cement', 'concrete', 'sand', 'steel bar', 'paint']

# Deleting an element by index
del my_list[2]           
print(my_list)           # Output: ['cement', 'concrete', 'steel bar', 'paint']

# Removing an element by value
my_list.remove('steel bar')  
print(my_list)           # Output: ['cement', 'concrete', 'paint']

# Inserting elements at a specific index
my_list[2:2] = ['wiring', 'pipes']  
print(my_list)           # Output: ['cement', 'concrete', 'wiring', 'pipes', 'paint']

# Popping an element by index
my_list.pop(1)          
print(my_list)           # Output: ['cement', 'wiring', 'pipes', 'paint']

# Multiplying list
print(my_list * 3)       # Output: ['cement', 'wiring', 'pipes', 'paint', 'cement', 'wiring', 'pipes', 'paint', 'cement', 'wiring', 'pipes', 'paint']

# Adding two lists
j = ["Water", "Wood"]
print(my_list + j)       # Output: ['cement', 'wiring', 'pipes', 'paint', 'Water', 'Wood']
