def get_even_number(lst):
    even=[]
    for i in lst:
        if i%2==0:
            even.append(i)
    return even
        
print(get_even_number([1,2,3,4,5,6]))