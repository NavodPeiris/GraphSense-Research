

def find_minimum_change(denominations: list[int], value: str) -> list[int]:
    total_value = int(value)

    
    answer = []

    
    for denomination in reversed(denominations):
        
        while int(total_value) >= int(denomination):
            total_value -= int(denomination)
            answer.append(denomination)  

    return answer



if __name__ == "__main__":
    denominations = []
    value = "0"

    if (
        input("Do you want to enter your denominations ? (yY/n): ").strip().lower()
        == "y"
    ):
        n = int(input("Enter the number of denominations you want to add: ").strip())

        for i in range(n):
            denominations.append(int(input(f"Denomination {i}: ").strip()))
        value = input("Enter the change you want to make in Indian Currency: ").strip()
    else:
        
        denominations = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
        value = input("Enter the change you want to make: ").strip()

    if int(value) == 0 or int(value) < 0:
        print("The total value cannot be zero or negative.")

    else:
        print(f"Following is minimal change for {value}: ")
        answer = find_minimum_change(denominations, value)
        
        for i in range(len(answer)):
            print(answer[i], end=" ")
