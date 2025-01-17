



def cramers_rule_2x2(equation1: list[int], equation2: list[int]) -> tuple[float, float]:

    
    if not len(equation1) == len(equation2) == 3:
        raise ValueError("Please enter a valid equation.")
    if equation1[0] == equation1[1] == equation2[0] == equation2[1] == 0:
        raise ValueError("Both a & b of two equations can't be zero.")

    
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2

    
    determinant = a1 * b2 - a2 * b1
    determinant_x = c1 * b2 - c2 * b1
    determinant_y = a1 * c2 - a2 * c1

    
    if determinant == 0:
        if determinant_x == determinant_y == 0:
            raise ValueError("Infinite solutions. (Consistent system)")
        else:
            raise ValueError("No solution. (Inconsistent system)")
    elif determinant_x == determinant_y == 0:
        
        return (0.0, 0.0)
    else:
        x = determinant_x / determinant
        y = determinant_y / determinant
        
        return (x, y)
