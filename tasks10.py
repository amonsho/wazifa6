def find_first_capital(s):
    lst1=[]
    for i in s:
        if i.upper():
            return i
        else:
            return None
#nafamidm
print(find_first_capital(['hello','hi','why']))