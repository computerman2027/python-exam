name=input("Enter Name : ")
name=name.strip()
if(len(name)==0):
    print("EMPTY NAME. NO INITIALS CAN BE PRINTED")
else:
    s1=name.split()
    ans=""
    for i in s1:
        ans=ans+i[0].capitalize()+'.'
    print("Initials =",ans)
