# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.

from copy import copy
from typing import List

import numpy as np

from Mesh import Mesh
from MeshVertex import MeshVertex
from ClippingPlane import ClippingPlane


def clip(mesh : Mesh, planes : List[ClippingPlane]) -> Mesh:
    """ clip the mesh with the given planes."""
    clipped_mesh = copy(mesh)
    clipped_mesh.clear()

    for f in range(mesh.faces.shape[0]):
        vertices = mesh.get_face(f).get_vertex(np.arange(mesh.faces[f]))

        positions = vertices.get_position()
        colors = vertices.get_color()
        vertex_count = 3

        for plane in planes:
            vertex_count, positions, colors = clip_plane(vertex_count, positions, colors, plane)

        if vertex_count != 0:
                clipped_mesh.add_face(vertex_count, positions, colors)

    return clipped_mesh

def clip_plane(vertex_count: int, positions: np.ndarray, colors: np.ndarray, plane: ClippingPlane) -> List[np.ndarray]:
    """ clips all vertices defined in positions against the clipping
             plane clipping_plane. Clipping is done by using the Sutherland
             Hodgman algorithm.

        Input Parameter
            vertex_count          ... number of vertices of the face that is clipped
            positions             ... n x 4 matrix with positions of n vertices
                                    one row corresponds to one vertex position
            colors                ... n x 3 matrix with colors of n vertices
                                    one row corresponds to one vertex color
            plane                 ... plane to clip against

        Returns:
            vertex_count_clipped  ... number of resulting vertices after clipping;
                                    this number depends on how the plane intersects
                                    with the face and therefore is not constant
            pos_clipped           ... n x 4 matrix with positions of n clipped vertices
                                    one row corresponds to one vertex position
            col_clipped           ... n x 3 matrix with colors of n clipped vertices
                                    one row corresponds to one vertex color"""
 
  
    pos_clipped = np.zeros((vertex_count + 1, 4))
    col_clipped = np.zeros((vertex_count + 1, 3))
    vertex_count_clipped = 0

    if vertex_count > 0:
        p2 = positions[vertex_count - 1]
        c2 = colors[vertex_count - 1]
        i2 = plane.inside(p2)

    for i in range(vertex_count):
        p1 = p2
        c1 = c2
        i1 = i2
        p2 = positions[i]
        c2 = colors[i]
        i2 = plane.inside( p2)

        if i1 and i2:
            pos_clipped[vertex_count_clipped] = p2
            col_clipped[vertex_count_clipped] = c2
            vertex_count_clipped += 1
        elif i1:
            t = plane.intersect(p1, p2)
            t = t - 10**-6
            pos_clipped[vertex_count_clipped] = mix(p1, p2, t)
            col_clipped[vertex_count_clipped] = mix(c1, c2, t)
            vertex_count_clipped += 1
        elif i2:
            t = plane.intersect(p1, p2)
            t = t + 10**-6
            pos_clipped[vertex_count_clipped] = mix(p1, p2, t)
            col_clipped[vertex_count_clipped] = mix(c1, c2, t)
            vertex_count_clipped += 1
            pos_clipped[vertex_count_clipped] = p2
            col_clipped[vertex_count_clipped] = c2
            vertex_count_clipped += 1

    pos_clipped = pos_clipped[:vertex_count_clipped]
    col_clipped = col_clipped[:vertex_count_clipped]
    return vertex_count_clipped, pos_clipped, col_clipped

# amk wieso geht des nur so
def mix(p1, p2, t):
    c = p1 - p1 * t + p2* t
    return c
    
