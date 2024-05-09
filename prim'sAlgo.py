inf = 9999999
N = 5
G = [[0, 4, 0, 3, 5],
     [4, 0, 2, 0, 0],
     [0, 2, 0, 1, 0],
     [3, 0, 1, 0, 0],
     [5, 0, 0, 0, 0]]
selected_node = [0,0,0,0,0]
no_edges = 0

selected_node[0] = True
print("Edges : Weight \n")
while(no_edges < N-1):
  minimum = inf
  a=0
  b=0

for m in range(N):
  if selected_node[m]:
    for n in range(N):
      if ((not selected_node[n]) and G[m][n]):
        if minimum< G[m][n]:
          minimum = G[m][n]
          a=m
          b=n
  print(str(a)+"-"+str(b)+":"+str(G[a][b]))
  selected_node[b] = True
  no_edges +=1
