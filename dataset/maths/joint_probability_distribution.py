

def joint_probability_distribution(
    x_values: list[int],
    y_values: list[int],
    x_probabilities: list[float],
    y_probabilities: list[float],
) -> dict:
    return {
        (x, y): x_prob * y_prob
        for x, x_prob in zip(x_values, x_probabilities)
        for y, y_prob in zip(y_values, y_probabilities)
    }



def expectation(values: list, probabilities: list) -> float:
    return sum(x * p for x, p in zip(values, probabilities))



def variance(values: list[int], probabilities: list[float]) -> float:
    mean = expectation(values, probabilities)
    return sum((x - mean) ** 2 * p for x, p in zip(values, probabilities))



def covariance(
    x_values: list[int],
    y_values: list[int],
    x_probabilities: list[float],
    y_probabilities: list[float],
) -> float:
    mean_x = expectation(x_values, x_probabilities)
    mean_y = expectation(y_values, y_probabilities)
    return sum(
        (x - mean_x) * (y - mean_y) * px * py
        for x, px in zip(x_values, x_probabilities)
        for y, py in zip(y_values, y_probabilities)
    )



def standard_deviation(variance: float) -> float:
    return variance**0.5


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
    x_vals = input("Enter values of X separated by spaces: ").split()
    y_vals = input("Enter values of Y separated by spaces: ").split()

    
    x_values = [int(x) for x in x_vals]
    y_values = [int(y) for y in y_vals]

    
    x_probs = input("Enter probabilities for X separated by spaces: ").split()
    y_probs = input("Enter probabilities for Y separated by spaces: ").split()
    assert len(x_values) == len(x_probs)
    assert len(y_values) == len(y_probs)

    
    x_probabilities = [float(p) for p in x_probs]
    y_probabilities = [float(p) for p in y_probs]

    
    jpd = joint_probability_distribution(
        x_values, y_values, x_probabilities, y_probabilities
    )

    
    print(
        "\n".join(
            f"P(X={x}, Y={y}) = {probability}" for (x, y), probability in jpd.items()
        )
    )
    mean_xy = expectation(
        [x * y for x in x_values for y in y_values],
        [px * py for px in x_probabilities for py in y_probabilities],
    )
    print(f"x mean: {expectation(x_values, x_probabilities) = }")
    print(f"y mean: {expectation(y_values, y_probabilities) = }")
    print(f"xy mean: {mean_xy}")
    print(f"x: {variance(x_values, x_probabilities) = }")
    print(f"y: {variance(y_values, y_probabilities) = }")
    print(f"{covariance(x_values, y_values, x_probabilities, y_probabilities) = }")
    print(f"x: {standard_deviation(variance(x_values, x_probabilities)) = }")
    print(f"y: {standard_deviation(variance(y_values, y_probabilities)) = }")
