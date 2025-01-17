
def binomial_coefficient(n: int, k: int) -> int:
    
    result = 1  
    
    k = min(k, n - k)
    
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result


def catalan_number(node_count: int) -> int:
    
    return binomial_coefficient(2 * node_count, node_count) // (node_count + 1)


def factorial(n: int) -> int:
    
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def binary_tree_count(node_count: int) -> int:
    
    return catalan_number(node_count) * factorial(node_count)


if __name__ == "__main__":
    node_count = int(input("Enter the number of nodes: ").strip() or 0)
    if node_count <= 0:
        raise ValueError("We need some nodes to work with.")
    print(
        f"Given {node_count} nodes, there are {binary_tree_count(node_count)} "
        f"binary trees and {catalan_number(node_count)} binary search trees."
    )
