def retGC(s):
  sTot = len(s)
  sGC = sTot - len(s.replace('G','').replace('C',''))
  tGC = (sGC/float(sTot))*100
  return tGC


def parseFile(file):
  f = open(file,'r')
  content = f.read().split('>')
  dic = {}
  for i in content:
    i = i.split('\n')
    if i[0] != '':
      dic[i[0]] = "".join(i[1:])
  f.close()
  return dic


d = parseFile('rosalind_gc.txt')

(MaxRes, MaxStr) = (0,'')

for key in d:
  taxGC = retGC(d[key])
  if MaxRes < taxGC: (MaxRes, MaxStr) = (taxGC,key)


print MaxStr
print MaxRes



#print("%.6f" % sGC)



