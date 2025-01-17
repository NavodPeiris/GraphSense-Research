

import numpy as np
import pytest

from data_structures.kd_tree.build_kdtree import build_kdtree
from data_structures.kd_tree.example.hypercube_points import hypercube_points
from data_structures.kd_tree.kd_node import KDNode
from data_structures.kd_tree.nearest_neighbour_search import nearest_neighbour_search


@pytest.mark.parametrize(
    ("num_points", "cube_size", "num_dimensions", "depth", "expected_result"),
    [
        (0, 10.0, 2, 0, None),  
        (10, 10.0, 2, 2, KDNode),  
        (10, 10.0, 3, -2, KDNode),  
    ],
)
def test_build_kdtree(num_points, cube_size, num_dimensions, depth, expected_result):
    
    points = (
        hypercube_points(num_points, cube_size, num_dimensions).tolist()
        if num_points > 0
        else []
    )

    kdtree = build_kdtree(points, depth=depth)

    if expected_result is None:
        
        assert kdtree is None, f"Expected None for empty points list, got {kdtree}"
    else:
        
        assert kdtree is not None, "Expected a KDNode, got None"

        
        assert len(kdtree.point) == num_dimensions, (
            f"Expected point dimension {num_dimensions}, got {len(kdtree.point)}"
        )

        
        assert isinstance(kdtree, KDNode), (
            f"Expected KDNode instance, got {type(kdtree)}"
        )


def test_nearest_neighbour_search():
    
    num_points = 10
    cube_size = 10.0
    num_dimensions = 2
    points = hypercube_points(num_points, cube_size, num_dimensions)
    kdtree = build_kdtree(points.tolist())

    rng = np.random.default_rng()
    query_point = rng.random(num_dimensions).tolist()

    nearest_point, nearest_dist, nodes_visited = nearest_neighbour_search(
        kdtree, query_point
    )

    
    assert nearest_point is not None

   
    assert nearest_dist >= 0

    
    assert nodes_visited >= 0


def test_edge_cases():
    
    empty_kdtree = build_kdtree([])
    query_point = [0.0] * 2  

    nearest_point, nearest_dist, nodes_visited = nearest_neighbour_search(
        empty_kdtree, query_point
    )

    
    assert nearest_point is None
    assert nearest_dist == float("inf")
    assert nodes_visited == 0


if __name__ == "__main__":
    import pytest

    pytest.main()
