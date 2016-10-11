f = open('input.txt')
l = f.read()

l = l.split('\n')

n = int(l[0])


A =  set(map(int,l[1].replace('{','').replace('}','').split(',')))

B =  set(map(int,l[2].replace('{','').replace('}','').split(',')))

#uniao
print '{'+', '.join(map(str,A.union(B)))+'}'

#interseccao
print '{'+', '.join(map(str,A.intersection(B)))+'}'


#a - b
print '{'+', '.join(map(str,A-B))+'}'


#b - a

print '{'+', '.join(map(str,B-A))+'}'





#complemento de a
C = set(range(1,n+1))

print '{'+', '.join(map(str,C-A))+'}'


#complemento
C = set(range(1,n+1))

print '{'+', '.join(map(str,C-B))+'}'


