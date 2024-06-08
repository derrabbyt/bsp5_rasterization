# Copyright TU Wien (2022) - EVC: Task 5
# Institute of Computer Graphics and Algorithms.

import numpy as np
from numpy.matlib import repmat

from Mesh import Mesh
from Framebuffer import Framebuffer
from MeshVertex import MeshVertex
import math

def line_rasterization(mesh : Mesh, framebuffer : Framebuffer):
    """ iterates over all faces of mesh and draws lines between
        their vertices.
        mesh                  ... mesh object to rasterize
        framebuffer           ... framebuffer"""

    for i in range(mesh.faces.shape[0]):
        for j in range(mesh.faces[i][0]):
            i, j = np.array(i).reshape(np.asarray(i).size), np.array(j).reshape(np.asarray(j).size)

            v1 = mesh.get_face(i).get_vertex(j)
            v2 = mesh.get_face(i).get_vertex(np.remainder(j + 1, mesh.faces[i]))
            draw_line(framebuffer, v1, v2)

def draw_line(framebuffer : Framebuffer, v1 : MeshVertex, v2 : MeshVertex):
    """ draws a line between v1 and v2 into the framebuffer using the
        DDA algorithm.
        framebuffer           ... framebuffer
        v1                    ... vertex 1
        v2                    ... vertex 2"""
    
    x1, y1, depth1 = v1.get_screen_coordinates()
    x2, y2, depth2 = v2.get_screen_coordinates()
    if(x1[0] != "nan"): 
        c1 = v1.get_color()
        c2 = v2.get_color()

        # Calculate the differences
        dx = x2[0] - x1[0]
        dy = y2[0] - y1[0]
        if dx == 0:
            dx+=1
        
        if dy == 0:
            dy+=1
        # Determine the number of steps needed
        steps = int(max(abs(dx), abs(dy)))
        dx = dx/steps
        dy = dy/steps
        # Initialize starting point
        x = x1[0]
        y = y1[0]


        # Draw the line
        i = 0
        t = 0
        l = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if l == 0:
            l+=1
        while i<steps:
            t = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)/l
            c = c1 - c1 * t + c2* t
            framebuffer.set_pixel(np.array([x]), np.array([y]), np.array([1]), c )
            x = x + dx
            y = y + dy
            i = i + 1