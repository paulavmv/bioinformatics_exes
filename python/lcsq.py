
a = list('AACCTTGG')
b = list('ACACTGTGA')

res = ''
print a,b
while len(a) != 0 and len(b) != 0:
  la = a.pop(0)
  lb = b.pop(0)
  print la, lb
  while lb != la and len(b) != 0:
      lb = b.pop(0)
  if la == lb:
    res += la
  print len(b), len(a)


res2 = ''

a = list('AACCTTGG')
b = list('ACACTGTGA')

while len(a) != 0 and len(b) != 0:
  la = a.pop(0)
  lb = b.pop(0)
  while lb != la and len(a) != 0:
      la = a.pop(0)
  if la == lb:
    res2 += la


print res
print res2
