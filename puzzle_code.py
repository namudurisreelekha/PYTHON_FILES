def valid_move(row,col,dire):
    if dire == 'A':
        return row != 0
    elif dire == 'B':
        return row != 4
    elif dire == 'L':
        return col != 0
    elif dire == 'R':
        return col != 4
l,count=[],0
for i in range(5):
    l.append(list(input()))
dire=list(input())
for d in dire:
    if d != 'O':
        for i in range(5):
            if ' ' in l[i]:
                pos=l[i].index(' ')
                t1=pos
                break
        if valid_move(i,pos,d):
            t=i    
            t=i-1 if d=='A' else (i+1 if d=='B' else t)
            t1=pos+1  if d=='R' else (pos-1  if d=='L'  else t1)
            l[i][pos]=l[t][t1]
            l[t][t1]=' '
        else:
            count=1
            break
    else:
        break
if count==0:
    for i in range(5):
        print(' '.join(l[i]))
else:
    print("No final configuration")
