u = [2,2]
v = [2,3]
z = [3,5]

result = [sum(t) for t in zip(u,v,z)]
print(result)

u = [1,2,3]
v = [4,4,4]
alpha = 2

result = [alpha*sum(t) for t in zip(u,v)]
print(result)

matrix_a = [[3,6],[4,5]]
matrix_b = [[5,8],[6,7]]
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a,matrix_b)]
print(result)

matrix_a = [[3,6],[4,5]]
alpha = 4
result = [[alpha*element for element in t] for t in matrix_a]
print(result)

matrix_a = [[1,2,3],[4,5,6]]
result = [[element for element in t] for t in zip (*matrix_a)]
print(result)

matrix_a = [[1,1,2],[2,1,1]]
matrix_b = [[1,1],[2,1],[1,3]]
result = [[sum(a*b for a,b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)