




def calc_profit(profit: list, weight: list, max_weight: int) -> int:
    if len(profit) != len(weight):
        raise ValueError("The length of profit and weight must be same.")
    if max_weight <= 0:
        raise ValueError("max_weight must greater than zero.")
    if any(p < 0 for p in profit):
        raise ValueError("Profit can not be negative.")
    if any(w < 0 for w in weight):
        raise ValueError("Weight can not be negative.")

    
    
    profit_by_weight = [p / w for p, w in zip(profit, weight)]

    
    sorted_profit_by_weight = sorted(profit_by_weight)

    
    length = len(sorted_profit_by_weight)
    limit = 0
    gain = 0
    i = 0

    
    while limit <= max_weight and i < length:
        
        biggest_profit_by_weight = sorted_profit_by_weight[length - i - 1]
        index = profit_by_weight.index(biggest_profit_by_weight)
        profit_by_weight[index] = -1

        
        
        if max_weight - limit >= weight[index]:
            limit += weight[index]
            
            
            gain += 1 * profit[index]
        else:
            
            
            
            gain += (max_weight - limit) / weight[index] * profit[index]
            break
        i += 1
    return gain


if __name__ == "__main__":
    print(
        "Input profits, weights, and then max_weight (all positive ints) separated by "
        "spaces."
    )

    profit = [int(x) for x in input("Input profits separated by spaces: ").split()]
    weight = [int(x) for x in input("Input weights separated by spaces: ").split()]
    max_weight = int(input("Max weight allowed: "))

    
    calc_profit(profit, weight, max_weight)
