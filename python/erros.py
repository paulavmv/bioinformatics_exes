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




def hamming_distance(s1,s2):
  return sum([1 if a!=b else 0 for (a,b) in zip(list(s1),list(s2))])



def trans(s):
  d = {'C':'G','A':'T','G':'C','T':'A'}
  return d[s]

def reverse_complement(s):
  s = s[::-1]
  return ''.join(map(trans,s))


aux = parseFile('rosalind.txt')
print len(aux)
acertos = []
erros = []
while True:
  r = aux.pop(0)
  r_comp = reverse_complement(r)
  if r not in aux and r_comp not in aux:
    erros.append(r)
  else:
      if r in aux: 
        aux.remove(r)
        aux = filter(lambda a: a != r, aux)
        acertos.append(r)
      if r_comp in aux: 
        aux.remove(r_comp)
        aux = filter(lambda a: a != r_comp, aux)
        acertos.append(r_comp)
  if len(aux) == 0: break

print len(erros)
print len(acertos)


res = ''
while True:
  st = 0
  t = erros.pop(0)
  for i in acertos:
    if hamming_distance(t,i) == 1:
      res += t+'->'+i+'\n'
      st = 1
      break
    elif hamming_distance(t,reverse_complement(i)) == 1:
      res += t+'->'+reverse_complement(i)+'\n'
      st = 1
      break
  if st == 0 : print t
    
  if len(erros) == 0: break


a = open('res.txt','w')
a.write(res)
#print res
