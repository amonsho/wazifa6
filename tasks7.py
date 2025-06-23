def remove_dublicates(lst):
    lst1=[]
    for i in lst:
        if i not in lst1:
            lst1.append(i)  
    return lst1

print(remove_dublicates([1,2,2,3,3,1]))