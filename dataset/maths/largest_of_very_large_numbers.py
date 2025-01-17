

import math


def res(x, y):
    if 0 not in (x, y):
        
        return y * math.log10(x)
    elif x == 0:  
        return 0
    elif y == 0:
        return 1  
    raise AssertionError("This should never happen")


if __name__ == "__main__":  
    
    
    prompt = "Enter the base and the power separated by a comma: "
    x1, y1 = map(int, input(prompt).split(","))
    x2, y2 = map(int, input(prompt).split(","))

    
    
    res1 = res(x1, y1)
    res2 = res(x2, y2)

    
    if res1 > res2:
        print("Largest number is", x1, "^", y1)
    elif res2 > res1:
        print("Largest number is", x2, "^", y2)
    else:
        print("Both are equal")
