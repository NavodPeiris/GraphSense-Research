
import numpy as np


def validate_adjacency_list(graph: list[list[int | None]]) -> None:
    if not isinstance(graph, list):
        raise ValueError("Graph should be a list of lists.")

    for node_index, neighbors in enumerate(graph):
        if not isinstance(neighbors, list):
            no_neighbors_message: str = (
                f"Node {node_index} should have a list of neighbors."
            )
            raise ValueError(no_neighbors_message)
        for neighbor_index in neighbors:
            if (
                not isinstance(neighbor_index, int)
                or neighbor_index < 0
                or neighbor_index >= len(graph)
            ):
                invalid_neighbor_message: str = (
                    f"Invalid neighbor {neighbor_index} in node {node_index} "
                    f"adjacency list."
                )
                raise ValueError(invalid_neighbor_message)


def lanczos_iteration(
    graph: list[list[int | None]], num_eigenvectors: int
) -> tuple[np.ndarray, np.ndarray]:
    num_nodes: int = len(graph)
    if not (1 <= num_eigenvectors <= num_nodes):
        raise ValueError(
            "Number of eigenvectors must be between 1 and the number of "
            "nodes in the graph."
        )

    orthonormal_basis: np.ndarray = np.zeros((num_nodes, num_eigenvectors))
    tridiagonal_matrix: np.ndarray = np.zeros((num_eigenvectors, num_eigenvectors))

    rng = np.random.default_rng()
    initial_vector: np.ndarray = rng.random(num_nodes)
    initial_vector /= np.sqrt(np.dot(initial_vector, initial_vector))
    orthonormal_basis[:, 0] = initial_vector

    prev_beta: float = 0.0
    for iter_index in range(num_eigenvectors):
        result_vector: np.ndarray = multiply_matrix_vector(
            graph, orthonormal_basis[:, iter_index]
        )
        if iter_index > 0:
            result_vector -= prev_beta * orthonormal_basis[:, iter_index - 1]
        alpha_value: float = np.dot(orthonormal_basis[:, iter_index], result_vector)
        result_vector -= alpha_value * orthonormal_basis[:, iter_index]

        prev_beta = np.sqrt(np.dot(result_vector, result_vector))
        if iter_index < num_eigenvectors - 1 and prev_beta > 1e-10:
            orthonormal_basis[:, iter_index + 1] = result_vector / prev_beta
        tridiagonal_matrix[iter_index, iter_index] = alpha_value
        if iter_index < num_eigenvectors - 1:
            tridiagonal_matrix[iter_index, iter_index + 1] = prev_beta
            tridiagonal_matrix[iter_index + 1, iter_index] = prev_beta
    return tridiagonal_matrix, orthonormal_basis


def multiply_matrix_vector(
    graph: list[list[int | None]], vector: np.ndarray
) -> np.ndarray:
    num_nodes: int = len(graph)
    if vector.shape[0] != num_nodes:
        raise ValueError("Vector length must match the number of nodes in the graph.")

    result: np.ndarray = np.zeros(num_nodes)
    for node_index, neighbors in enumerate(graph):
        for neighbor_index in neighbors:
            result[node_index] += vector[neighbor_index]
    return result


def find_lanczos_eigenvectors(
    graph: list[list[int | None]], num_eigenvectors: int
) -> tuple[np.ndarray, np.ndarray]:
    validate_adjacency_list(graph)
    tridiagonal_matrix, orthonormal_basis = lanczos_iteration(graph, num_eigenvectors)
    eigenvalues, eigenvectors = np.linalg.eigh(tridiagonal_matrix)
    return eigenvalues[::-1], np.dot(orthonormal_basis, eigenvectors[:, ::-1])


def main() -> None:
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
