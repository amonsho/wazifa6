def count_vowels(s):
    cnt=0
    vow='a','e','i','o','u','A','E','I','O','U'
    for i in s:
        if i in vow:
            cnt+=1
    return cnt
    
print(count_vowels('Hello'))