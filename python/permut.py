import itertools

n = 6
tot = 0
t = itertools.permutations(['P', 'L' ,'R', 'H', 'K', 'U', 'S', 'Y', 'X', 'F', 'J','P', 'L' ,'R', 'H', 'K', 'U', 'S', 'Y', 'X', 'F', 'J','P', 'L' ,'R', 'H', 'K', 'U', 'S', 'Y', 'X', 'F', 'J',' ',' ',' '],3)




d = {' ':0,'P':1, 'L':2 ,'R':3, 'H':4, 'K':5, 'U':6, 'S':7, 'Y':8, 'X':9, 'F':10, 'J':11}

f = open("per.txt","w")

l = []

#for i in t:
#  tot+=1
#  f.write(" ".join(map(str,i)) + '\n')


#for i in t:
#    a = False
#    for j in i:
#        if (-1)*j in i: a = True
#    if a == False:
#        f.write(" ".join(map(str,i)) + '\n')
#
#        tot+=1

for i in t:
  if i[0] == ' ' or  (i[1] == ' ' and i[2] != ' ') :  
    None  
  else: l.append(i[0]+i[1]+i[2])

l = set(l)
l2 = sorted(l, key=lambda x: (d[x[0]],d[x[1]],d[x[2]]) )

l2 =map(lambda p:p.replace(' ',''),l2)
#l2 = set(l2)
for i in l2:
  f.write(i.replace(' ','')+'\n')

#f.write(str(tot))
