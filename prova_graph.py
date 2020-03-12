import networkx as nx

G = nx.Graph()
matrix = [['#','M'],['M','_']]
n_row = 2
n_column = 2

for i in range(n_row):
    for j in range(n_column):

        if matrix[i][j] != '#':

            if i+1 < n_row:
                if matrix[i + 1][j] != '#':
                    G.add_edge(str(i) + str(j) + str(matrix[i][j]), str(i+1) + str(j) + str(matrix[i + 1][j]))

            if i-1 >= 0:
                if matrix[i - 1][j] != '#':
                    G.add_edge(str(i) + str(j) + str(matrix[i][j]), str(i-1) + str(j) + str(matrix[i - 1][j]))

            if j+1 < n_column:
                if matrix[i][j + 1] != '#':
                    G.add_edge(str(i) + str(j) + str(matrix[i][j]), str(i) + str(j + 1) + str(matrix[i][j + 1]))

            if j-1 >= 0:
                if matrix[i][j - 1] != '#':
                    G.add_edge(str(i) + str(j) + str(matrix[i][j]), str(i) + str(j - 1) + str(matrix[i][j - 1]))


print(G.edges())
components = list(nx.connected_components(G))

for c in components:
    pass

