def prob(hzD,ht,hzR):
  total = 2*float(hzD+ht+hzR)
  p1 = ( (2*hzD)/(total) ) * 1
  p2 = ( (ht) / (total)  ) * 1
  p3 = ( (ht) / (total) ) * ( (2*hzD + (ht - 1) ) / (total - 2) )
  p4 = ( (2*hzR) / total ) * ( (2*hzD + ht) / (total - 2) )
  return (p1 + p2 + p3 + p4)




