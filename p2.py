st=input("Enter a sentence : ")
st=st.strip()
st1=st.split()
ans=""
for i in st1:
    ans=ans+i[::-1]+' '
print("Ans =",ans)
