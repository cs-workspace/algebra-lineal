import numpy as np

# Ejercicio a

v1 = [[1, 1, 1]]
v2 = [[1, -1, 0]]
v3 = [[1, 1, -2]]

# Verificando si son ortonormales
mult = np.dot(v2, np.transpose(v1))
if(mult[0][0] == 0):
    print("V1 y V2 son ortogonales")
else:
    print("V1 y V2 no son ortogonales")

mult = np.dot(v3, np.transpose(v1))
if(mult[0][0] == 0):
    print("V1 y V3 son ortogonales")
else:
    print("V1 y V3 no son ortogonales")

mult = np.dot(v3, np.transpose(v2))
if(mult[0][0] == 0):
    print("V2 y V3 son ortogonales")
else:
    print("V2 y V3 no son ortogonales")


# Generando conjunto  ortonormal

V1n = (v1/np.linalg.norm(v1))
V2n = (v2/np.linalg.norm(v2))
V3n = (v3/np.linalg.norm(v3))

print(V1n)
print(V2n)
print(V3n)


# Ejercicio b

v1 = [[1, 1, -1, -1]]
v2 = [[1, 1, 1, 1]]
v3 = [[1, -1, 0, 0]]
v4 = [[0, 0, -1, 1]]

# Verificando si son ortonormales
mult = np.dot(v2, np.transpose(v1))
if(mult[0][0] == 0):
    print("V1 y V2 son ortogonales")
else:
    print("V1 y V2 no son ortogonales")

mult = np.dot(v3, np.transpose(v1))
if(mult[0][0] == 0):
    print("V1 y V3 son ortogonales")
else:
    print("V1 y V3 no son ortogonales")

mult = np.dot(v4, np.transpose(v1))
if(mult[0][0] == 0):
    print("V1 y V4 son ortogonales")
else:
    print("V1 y V4 no son ortogonales")

mult = np.dot(v3, np.transpose(v2))
if(mult[0][0] == 0):
    print("V2 y V3 son ortogonales")
else:
    print("V2 y V3 no son ortogonales")

mult = np.dot(v4, np.transpose(v2))
if(mult[0][0] == 0):
    print("V2 y V4 son ortogonales")
else:
    print("V2 y V4 no son ortogonales")

mult = np.dot(v4, np.transpose(v3))
if(mult[0][0] == 0):
    print("V3 y V4 son ortogonales")
else:
    print("V3 y V4 no son ortogonales")


# Generando conjunto  ortonormal

V1n = (v1/np.linalg.norm(v1))
V2n = (v2/np.linalg.norm(v2))
V3n = (v3/np.linalg.norm(v3))
V4n = (v4/np.linalg.norm(v4))

print(V1n)
print(V2n)
print(V3n)
print(V4n)
