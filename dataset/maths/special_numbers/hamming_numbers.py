

def hamming(n_element: int) -> list:
    n_element = int(n_element)
    if n_element < 1:
        my_error = ValueError("n_element should be a positive number")
        raise my_error

    hamming_list = [1]
    i, j, k = (0, 0, 0)
    index = 1
    while index < n_element:
        while hamming_list[i] * 2 <= hamming_list[-1]:
            i += 1
        while hamming_list[j] * 3 <= hamming_list[-1]:
            j += 1
        while hamming_list[k] * 5 <= hamming_list[-1]:
            k += 1
        hamming_list.append(
            min(hamming_list[i] * 2, hamming_list[j] * 3, hamming_list[k] * 5)
        )
        index += 1
    return hamming_list


if __name__ == "__main__":
    n = input("Enter the last number (nth term) of the Hamming Number Series: ")
    print("Formula of Hamming Number Series => 2^i * 3^j * 5^k")
    hamming_numbers = hamming(int(n))
    print("-----------------------------------------------------")
    print(f"The list with nth numbers is: {hamming_numbers}")
    print("-----------------------------------------------------")
