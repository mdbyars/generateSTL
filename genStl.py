import numpy as np
from stl import mesh
from random import randint
#from facify import facize

#I have used algebra to determine resonable ranges to ensure that the faces and 
#vertices are compatable and that the shape will be printable 
vertices = np.array([
    [randint(0,2),randint(0,2),randint(0, 2)], #0
    [randint(0,2),randint(0,2),randint(0, 2)], #1
    [randint(0,2),randint(0,2),randint(0, 2)], #2
    [randint(0,2),randint(0,2),randint(0, 2)], #3
    [randint(0,2),randint(0,2),randint(0, 2)], #4
    [randint(0,2),randint(0,2),randint(0, 2)], #5
    [randint(0,2),randint(0,2),randint(0, 2)], #6
    [randint(0,2),randint(0,2),randint(0, 2)], #7
    [randint(0,3),randint(0,3),randint(0, 3)], #8
    [randint(0,3),randint(0,3),randint(0, 3)], #9
    [randint(-3,3),randint(-3,3),randint(-3, 3)], #10
    [randint(-3,3),randint(-3,3),randint(-3, 3)], #11
    [randint(-3,4),randint(-3,4),randint(-3, 4)], #12
    [randint(-3,3),randint(-3,3),randint(-3, 3)], #13
    [randint(-3,3),randint(-3,3),randint(-3, 3)], #14
    [randint(-3,3),randint(-3,3),randint(-3, 3)], #15
    [randint(-3,3),randint(-3,3),randint(-3, 3)], #16
    [randint(-3,3),randint(-3,3),randint(-3, 3)], #17
    [randint(-3,4),randint(-3,4),randint(-3, 4)], #18
])
#faces = facize(vertices)

faces = np.array([
    [randint(0,5),randint(0,5),randint(0, 5)], 
    [randint(0,3),randint(0,3),randint(0, 3)], 
    
    [randint(0,5),randint(0,5),randint(0, 5)], 
    [randint(0,5),randint(0,5),randint(0, 5)], 
    
    [randint(0,6),randint(0,6),randint(0, 6)], 
    [randint(0,6),randint(0,6),randint(0, 6)], 
   
    [randint(3,7),randint(3,7),randint(3, 7)], 
    [randint(3,7),randint(3,7),randint(3, 7)], 
    
    [randint(3,7),randint(3,7),randint(3, 7)], 
    [randint(3,7),randint(3,7),randint(3, 7)], 
    
    [randint(3,8),randint(3,8),randint(3, 8)], 
    [randint(3,8),randint(3,8),randint(3, 8)], 
    
    [randint(9,11),randint(9,11),randint(9, 11)], 
    [randint(9,11),randint(9,11),randint(9, 11)], 
    
    [randint(6,12),randint(6,12),randint(6, 12)], 
    [randint(6,12),randint(6,12),randint(6, 12)], 
    
    [randint(4,14),randint(4,14),randint(4, 14)], 
    [randint(4,14),randint(4,14),randint(4, 14)], 
    
    [randint(4,15),randint(4,15),randint(4, 15)], 
    [randint(4,15),randint(4,15),randint(4, 15)], 
    
    [randint(5,16),randint(5,16),randint(5, 16)], 
    [randint(5,16),randint(5,16),randint(5, 16)], 
    
    [randint(9,18),randint(9,18),randint(9, 18)], 
    [randint(9,18),randint(9,18),randint(9, 18)], 
    
    [randint(11,18),randint(11,18),randint(11, 18)], 
    [randint(11,18),randint(11,18),randint(11, 18)], 
    
    [randint(11,18),randint(11,18),randint(11, 18)], 
    [randint(11,18),randint(11,18),randint(11, 18)], 
    
    [randint(11,18),randint(11,18),randint(11, 18)], 
    [randint(11,18),randint(11,18),randint(11, 18)], 
    
    [randint(11,18),randint(11,18),randint(11, 18)], 
    [randint(11,18),randint(11,18),randint(11, 18)], 
])


#here we export the mesh created. Fortunately, the numpy package is very good at this 
shape = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        shape.vectors[i][j] = vertices[f[j], :]

shape.save("testingRecovered.stl")
