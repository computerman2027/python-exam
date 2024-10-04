name=input("Enter Name : ")
s1=name.split()
ans=""
for i in s1:
    ans=ans+i[0].capitalize()+'.'
print("Initials =",ans)
