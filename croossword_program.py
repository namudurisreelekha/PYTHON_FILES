def across(l1,num):
    print("ACROSS")
    n=1
    count=0
    a=''
    for r in range(len(l1)):
        count=0
        for c in range(len(l1[r])):
            if (l1[r][c]=='*' or c==len(l1[r])-1) and a!='':
                if c==len(l1[r])-1 and l1[r][c]!='*':
                    a +=l1[r][c]
                print(str(n)+"."+a)
                a=''
                count=0
            elif l1[r][c]!='*':
                count += 1
                a += l1[r][c]
                if count==1:
                    n=num[r][c]
           
def down(l1,num,row,col):
    print("DOWN:")
    j,i=0,0
    while i<row:
        for c in range(col):
            s=''
            count=0
            if (i==0) or(i!=0 and l1[i-1][c]) == '*':
                for r in range(i,row):
                    if l1[r][c] !='*':
                        count+=1
                        s=s+l1[r][c]
                        if count==1:
                            n=num[r][c]
                    else:
                        break
                if s!='':
                    print(n,s,sep=".")
        i+=1
               
def numbering(k,row,col):
    num= [[0 for j in range(col)] for i in range(row)]
    count=0
    for r in range(row):
        for c in range(col):
                if k[r][c]!='*':
                    if r==0 :
                        if k[r][c].isalpha():
                                count+=1
                                num[r][c]=count
                        else:
                                num[r][c]=''
                    elif c==0:
                        count+=1
                        num[r][c]=count

                    elif c==col-1:
                        if k[r-1][c]=='*' or k[r][c-1]=='*':
                            count+=1
                            num[r][c]=count
                        else:
                            num[r][c]=''
                    else:
                        if k[r][c-1]=='*' or k[r-1][c]=='*':
                            count+=1
                            num[r][c]=count
                        else:
                            num[r][c]=''
                else:
                    num[r][c]='*'
    return num
    
row,col=int(input()),int(input())
l1=[]
for r in range(row):
    s=input()
    l1.append(list(s))
num=numbering(l1,row,col)
across(l1,num)
down(l1,num,row,col)
