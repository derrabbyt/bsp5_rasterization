# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.

import numpy as np
from numpy.matlib import repmat

from MeshVertex import MeshVertex
from Framebuffer import Framebuffer
from MeshVertex import MeshVertex

def fill_rasterization(mesh : MeshVertex, framebuffer : Framebuffer):
    """ applies the fill rasterization algorithm. Draws a mesh to the Framebuffer."""

    for i in range(mesh.faces.shape[0]):
        v1 = mesh.get_face(i).get_vertex(0)
        for j in range(mesh.faces[i][0]-1):
            i, j = np.array(i).reshape(np.asarray(i).size), np.array(j).reshape(np.asarray(j).size)

            v2 = mesh.get_face(i).get_vertex(j)
            v3 = mesh.get_face(i).get_vertex(j+1)
            draw_triangle(framebuffer, v1, v2, v3)


def lineEq(A, B, C, x, y):
    print(len(A))
    
    if(len(A)== len(x)):
        return A*x+ B*y + C

    A = A[np.newaxis, :] 
    B = B[np.newaxis, :]  
    C = C[np.newaxis, :]  
    A = np.tile(A, (len(x), 1))  
    B = np.tile(B, (len(x), 1))  
    C = np.tile(C, (len(x), 1))  
    return A*x[:, None] + B*y[:, None] + C

def draw_triangle(framebuffer: Framebuffer, v1: MeshVertex, v2: MeshVertex, v3: MeshVertex):
    x1, y1, z1 = v1.get_screen_coordinates()
    x2, y2, z2 = v2.get_screen_coordinates()
    x3, y3, z3 = v3.get_screen_coordinates()
    x1, y1, z1 = x1[0], y1[0], z1[0]
    x2, y2, z2 = x2[0], y2[0], z2[0]
    x3, y3, z3 = x3[0], y3[0], z3[0]

    c1 = v1.get_color()
    c2 = v2.get_color()
    c3 = v3.get_color()

    # Calculate triangle area * 2
    rec = ((x3-x1)*(y2-y1) - (x2-x1)*(y3-y1))

    if rec != 0:
        # Swap order of clockwise triangle to make them counter-clockwise
        if rec < 0:
            x2, x3 = x3, x2
            y2, y3 = y3, y2
            z2, z3 = z3, z2
            c2, c3 = c3, c2

        v = np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])
        ve = v[[2, 0, 1]] - v[[1, 2, 0]]
        vn = ve[:, [1, 0, 2]] * [-1, 1, 1]

        c = np.sum(vn * v[[1, 2, 0]], axis=1) * -1
        d = lineEq(vn[:, 0], vn[:, 1], c, v[:, 0], v[:, 1])

        low = np.min(v, axis=0)
        hi = np.max(v, axis=0)
        dif = hi - low + 1

        print(hi)
        print("low")
        print(low)
        print("dif")
        print(dif)

        vx = np.repeat(np.arange(int(low[0]), int(hi[0])+1), int(dif[1]))
        vy = np.tile(np.arange(int(low[1]), int(hi[1])+1),  int(dif[0]))

        dtest = lineEq(vn[:, 0], vn[:, 1], c, vx, vy)
        enabled = np.max(dtest, axis=1) <= 0
        k = dtest[ enabled, :]
        abc =  k / d
        vx = vx[enabled]
        vy = vy[enabled]

        depth = MeshVertex.barycentric_mix(z1, z2, z3, abc[:, 0], abc[:, 1], abc[:, 2])
        color = np.transpose(MeshVertex.barycentric_mix(np.transpose(c1), np.transpose(c2), np.transpose(c3), abc[:, 0], abc[:, 1], abc[:, 2]))

        framebuffer.set_pixel(vx, vy, depth, color)
