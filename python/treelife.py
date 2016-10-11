def graph_min(n, edges):
  d = {}
  v = {}
  for i in range(1,n+1): d[i] = []
  for i in range(1,n+1): v[i] = False
  edges.sort()
  for (a,b) in edges:
    d[a].append(b)
    d[b].append(a)
  grafos_desconexos = []
  l = range(1,n+1)
  f = []
  while len(l) > 0:
    r = l.pop(0)
    if v[r] == False:
        v[r] = True
        k = caminho(d,r,v)
        f.append(k)

  print f, len(f)-1
    
    
  
def caminho(d, r, v):
    res = [r]
    for i in d[r]:
      if v[i] == False:
        v[i] = True
        res+=caminho(d,i, v)
    return res

f = open('input.txt')
c = f.read().split('\n')
n = int(c[0])

edges = []

for i in c[1:-1]:
  edges.append(map(int,i.split(' ')))
  
  
graph_min(n, edges)
