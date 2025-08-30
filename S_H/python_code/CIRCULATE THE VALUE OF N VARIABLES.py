def rotate(l, n): 
    new_list = l[n:] + l[:n] 
    return new_list 

e1 = [4, 5, 2, 3, 6, 7, 8] 
print("Original list =", e1) 

m1 = rotate(e1, 1) 
print("List rotated clockwise by 1:", m1) 

m1 = rotate(e1, 2) 
print("List rotated clockwise by 2:", m1) 

m1 = rotate(e1, -2) 
print("List rotated counterclockwise by 2:", m1)
