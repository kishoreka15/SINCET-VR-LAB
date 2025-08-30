def myMax(): 
    list1 = [] 
    n = int(input("Enter the number of elements in the list: ")) 
    for i in range(n): 
        a = int(input("Enter the value: ")) 
        list1.append(a) 
    list1.sort() 
    max_value = list1[n - 1] 
    return max_value 

print("Largest element is:", myMax())
