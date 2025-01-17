def sum_of_geometric_progression(
    first_term: int, common_ratio: int, num_of_terms: int
) -> float:
    if common_ratio == 1:
        
        return num_of_terms * first_term

    
    return (first_term / (1 - common_ratio)) * (1 - common_ratio**num_of_terms)
