




def pigeonhole_sort(a):
    

    min_val = min(a)  
    max_val = max(a)  

    size = max_val - min_val + 1  

    
    holes = [0] * size

    
    for x in a:
        assert isinstance(x, int), "integers only please"
        holes[x - min_val] += 1

    
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + min_val
            i += 1


def main():
    a = [8, 3, 2, 7, 4, 6, 8]
    pigeonhole_sort(a)
    print("Sorted order is:", " ".join(a))


if __name__ == "__main__":
    main()
