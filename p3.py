try:
    term=65
    h=int(input("Enter no of Rows : "))
    if(h<1):
        print("Invalid input")
    else:
        for i in range(h):
            print(" "*(h-1-i),end="")
            for j in range(0,i+1):
                print(chr(term),"",end="")
                term+=1
            print()
except:
    print("ERROR: ONLY INTEGER INPUT ACCEPTED")
