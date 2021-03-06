#!/usr/bin/env python
"""
The basic test of the UGrid object.

more speicifc functionaily is other test modules.
"""


from pyugrid import UGrid
from pyugrid.ugrid import IND_DT, NODE_DT

from pyugrid.test_examples import two_triangles


# Some sample grid data: about the simplest triangle grid possible

# 4 nodes, two triangles, five edges
nodes = [(0.1, 0.1),
         (2.1, 0.1),
         (1.1, 2.1),
         (3.1, 2.1)]

faces = [(0, 1, 2),
         (1, 3, 2),]

edges = [(0, 1),
         (1, 3),
         (3, 2),
         (2, 0),
         (1, 2)]

boundaries = [(0,1),
              (0,2),
              (1,3),
              (2,3),
              ]

def test_full_set():
    grid = UGrid(nodes=nodes,
                 faces=faces,
                 edges=edges,
                 boundaries=boundaries,
                 )

    # check the dtype of key objects
    # mplicitly makes sure they are numpy arrays (or array-like)

    assert grid.num_vertices == 3

    assert grid.nodes.dtype == NODE_DT
    assert grid.faces.dtype == IND_DT
    assert grid.edges.dtype == IND_DT
    assert grid.boundaries.dtype == IND_DT

    # check shape of grid arrays
    assert len(grid.nodes.shape) == 2
    assert len(grid.faces.shape) == 2
    assert len(grid.edges.shape) == 2
    assert len(grid.boundaries.shape) == 2

    assert grid.nodes.shape[1] == 2
    assert grid.faces.shape[1] == 3
    assert grid.edges.shape[1] == 2
    assert grid.boundaries.shape[1] == 2


