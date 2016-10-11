def expected_value(v):
  v = map(int,v.split(' '))  
  p = {0:1,1:1,2:1,3:(3/4.),4:0.5,5:0}
  res = 0
  for i in range(6):
    res += v[i]*p[i]
  return 2 * res
