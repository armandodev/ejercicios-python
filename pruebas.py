ren = 1
col = 1
while ren < 2 and col < 2:
    ren = int(input("Ingrese el renglón: "))
    col = int(input("Ingrese las columnas: "))
    
mat = [[0 for _ in range(col)] for _ in range(ren)]

for ren in range(len(mat)):
    for col in range(len(mat[ren])):
        num = mat[ren][col]
        
# vec = [1, 2, 3]
# vec[0]

# 0 0 0
# 0 0 0
# 0 0 0
# mat[0][0]