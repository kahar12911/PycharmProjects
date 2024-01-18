def palindrome_s(str):
    i=0
    j=len(str)-1
    while i < j:
        #print(i,j)
        if str[i]!=str[j]:
            print("string is not palindrome")
            return 0
        i=i+1
        j=j-1

    print("string is palindrome")
    return 1

str="malayalam"

palindrome_s(str)

dict ={
    "f1": "first",
    "f2": "second"
};


