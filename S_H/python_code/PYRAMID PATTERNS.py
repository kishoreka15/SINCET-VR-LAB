rows = int(input("Enter Pyramid Pattern Rows = ")) 
print("Pyramid Star Pattern")

for i in range(0, rows): 
    for j in range(0, rows - i - 1): 
        print(end=' ') 
    for k in range(0, i + 1): 
        print('*', end=' ') 
    print()
