# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.

from typing import List
import numpy as np

class ClippingPlane:

    def __init__(self, plane : np.ndarray):
        """ plane     ... plane stored in Hessian normal form as a 1x4 vector"""
        self.plane = plane
    

    def inside(self, position):
        d = np.dot(position, self.plane)
        return d <= 0

    def intersect(self, pos1, pos2):
        la = np.dot(pos1, self.plane)
        lb = np.dot(pos2, self.plane)
        return la / (la - lb)
    
    @staticmethod
    def get_clipping_planes() -> List:
        """creates and returns a list of the six Clipping planes defined in the task description."""

        ### STUDENT CODE
        # TODO 2: Define the correct clip planes.
        # NOTE:   The following lines can be removed. They prevent the framework
        #         from crashing.
        return [
            ClippingPlane(np.array([1, 0, 0, -1])),
            ClippingPlane(np.array([-1, 0, 0, -1])),
            ClippingPlane(np.array([0, 1, 0, -1])),
            ClippingPlane(np.array([0, -1, 0, -1])),
            ClippingPlane(np.array([0, 0, 1, -1])),
            ClippingPlane(np.array([0, 0, -1, -1]))
        ]


        ### END STUDENT CODE

        
        return res

