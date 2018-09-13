def firstNotRepeatingCharacter(s):
    list_index=26*[0]
    count=1
    for c in s:
        ind=ord(c)-97
        if list_index[ind]>=100000:
            list_index[ind]=list_index[ind]+1
        else:
            list_index[ind]=count*100000
        count+=1
    print(list_index)
    help=100000
    letter="_"
    for i in range(len(list_index)):
        if list_index[i] % 100000==0 and list_index[i]!=0:
            num=list_index[i]/100000
            if num<help:
                help=num
                letter=chr(i+97)
    return letter
    