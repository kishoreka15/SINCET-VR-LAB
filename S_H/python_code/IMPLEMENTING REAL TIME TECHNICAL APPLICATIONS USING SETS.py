# Initializing the sets
set1 = {"Python", "Java", "C"} 
set2 = {"Java", "Php", "Python"} 

# Display the sets
print("Set1 =", set1) 
print("Set2 =", set2) 
print("\n") 

# Union of sets
set3 = set1 | set2 
print("Union of Set1 & Set2: Set3 =", set3) 

# Intersection of sets
set4 = set1 & set2 
print("Intersection of Set1 & Set2: Set4 =", set4) 
print("\n") 

# Superset and subset check
if set3 > set4: 
    print("Set3 is superset of Set4") 
elif set3 < set4: 
    print("Set3 is subset of Set4") 
else: 
    print("Set3 is same as Set4") 

# Difference of sets
set5 = set1 - set2 
print("Elements in Set1 and not in Set2: Set5 =", set5) 
print("\n") 

# Clearing the set
set5.clear() 
print("After applying clear on sets Set5:") 
print("Set5 =", set5)
