def gS(str):
    c=str[::-1]
    del str[0]
    c.pop()
    if(str==c):
        print("This is already a good string. You have to delete 0 numbers")
    else:
        return 0

def repeatations(str):
    coun=0
    for j in range(0,len(asolInput)):
        if str==asolInput[j]:
            coun+=1
    return coun

asolInput=list(input("Enter string:"))
a=asolInput.copy()
count=gS(a)
cou=0
result=[]
for i in range(0,len(asolInput)):
    a1=asolInput[i]
    rr=repeatations(a1)
    result.append(rr)
mx=max(result)
f=0
if(mx>1):
    for k in range(0,len(asolInput)):
        if(result[k]==mx):
            cou+=1
            f=len(asolInput)-cou
    print(f)
else:
    f=len(asolInput)-2
    print(f)    