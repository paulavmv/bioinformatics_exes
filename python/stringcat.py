
def find_metade(di,dj):
  lmin = len(di)
  if len(dj) < len(di): lmin = len(dj)
  i = lmin
  while i >= lmin/2:
    if di[(-1)*i:] == dj[:i]:
      return di[:(-1)*i] + dj
    i-=1
  return 0


def parseFile(file):
  f = open(file,'r')
  content = f.read().split('>')
  dic = []
  for i in content:
    i = i.split('\n')
    if i[0] != '':
      dic.append("".join(i[1:]))
  f.close()
  return dic


aux = parseFile('rosalind.txt')


teste = 0
res = aux[0]
aux.pop(0)
while True:
    j = 0
    while j < len(aux):
      t = find_metade(res,aux[j])
      if t !=0: 
          res=t
          aux.pop(j)
          break
      else:
          t = find_metade(aux[j],res)
          if t !=0: 
              res=t
              aux.pop(j)
              break
      j+=1
    teste += 1
    if len(aux) == 0: break
    if teste > 10000: break

print res, aux
  






