#pontuacao

Match_point = 1
Mismatch_point = -10
Gap_point = -10




#inicializa matriz com sequencias
def matriz_inicial(seq1,seq2)
  m = []
  m.insert(-1,[0,0]+seq1.split(""))

  gap_lines = [*((Gap_point*seq1.length)..(Gap_point)).step(10)].reverse
  m.insert(-1,[0,0]+gap_lines)

  gap_lines = [*((Gap_point*seq2.length)..(Gap_point)).step(10)].reverse
  seq2.split("").zip(gap_lines).each{ |x,y|
    m.insert(-1,[x,y]+[0]*seq1.length)
  }
  m
end

def pontua(m,i,j)
  print i,' ',j,' ',m,' '
  if m[i][0] == m[0][j]
    return Match_point + m[i-1][j-1]
  end
  #vertical gap, horizontal_gap, mismatch
  return [m[i][j-1]+Gap_point,m[i-1][j]+Gap_point,m[i-1][j-1]+Mismatch_point].sort()[-1]
end


def antecessor(m,i,j)
  if m[i][j] == (m[i-1][j-1] + Match_point)
    return [i-1,j-1,m[i][0]]
  elsif m[i][j] == (m[i-1][j-1] + Mismatch_point)
    return [i-1,j-1,'']   
  elsif m[i][j] == (m[i-1][j] + Gap_point)
    return [i-1,j,''] 
  elsif m[i][j] == (m[i][j-1] + Gap_point)
    return [i,j-1,'']   
  end 
end

def monta_palavra(m)
  i = m.length-1
  j = m[0].length-1
  palavra = ''
  while  i != 1 and j!= 1
    print i,j
    r = antecessor(m,i,j)
    i = r[0]
    j = r[1]
    palavra = r[2] + palavra
  end
  palavra
end


def alignment(seq1,seq2)
  m = matriz_inicial(seq1,seq2)
  (2..(seq2.length+1)).each{ |i|
    (2..(seq1.length+1)).each{ |j|
      m[i][j] = pontua(m,i,j)
    }
  }
  m
end

def ret_sequencia_alinhada(seq1,seq2)
  m = alignment(seq1,seq2)
  print m
  p = monta_palavra(m)
  p
end


puts ret_sequencia_alinhada('GCATGCU','GATTACA')
