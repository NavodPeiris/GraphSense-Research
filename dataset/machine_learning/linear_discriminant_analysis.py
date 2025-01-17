
from collections.abc import Callable
from math import log
from os import name, system
from random import gauss, seed
from typing import TypeVar



def gaussian_distribution(mean: float, std_dev: float, instance_count: int) -> list:
    seed(1)
    return [gauss(mean, std_dev) for _ in range(instance_count)]



def y_generator(class_count: int, instance_count: list) -> list:

    return [k for k in range(class_count) for _ in range(instance_count[k])]



def calculate_mean(instance_count: int, items: list) -> float:
    
    return sum(items) / instance_count



def calculate_probabilities(instance_count: int, total_count: int) -> float:
    
    return instance_count / total_count



def calculate_variance(items: list, means: list, total_count: int) -> float:
    squared_diff = []  
    
    for i in range(len(items)):
        
        for j in range(len(items[i])):
            
            squared_diff.append((items[i][j] - means[i]) ** 2)

    
    
    n_classes = len(means)  
    return 1 / (total_count - n_classes) * sum(squared_diff)



def predict_y_values(
    x_items: list, means: list, variance: float, probabilities: list
) -> list:
    
    
    results = []
    
    for i in range(len(x_items)):
        
        for j in range(len(x_items[i])):
            temp = []  
            
            for k in range(len(x_items)):
                
                temp.append(
                    x_items[i][j] * (means[k] / variance)
                    - (means[k] ** 2 / (2 * variance))
                    + log(probabilities[k])
                )
            
            results.append(temp)

    return [result.index(max(result)) for result in results]



def accuracy(actual_y: list, predicted_y: list) -> float:
    
    
    correct = sum(1 for i, j in zip(actual_y, predicted_y) if i == j)
    
    
    return (correct / len(actual_y)) * 100


num = TypeVar("num")


def valid_input(
    input_type: Callable[[object], num],  
    input_msg: str,
    err_msg: str,
    condition: Callable[[num], bool] = lambda _: True,
    default: str | None = None,
) -> num:
    while True:
        try:
            user_input = input_type(input(input_msg).strip() or default)
            if condition(user_input):
                return user_input
            else:
                print(f"{user_input}: {err_msg}")
                continue
        except ValueError:
            print(
                f"{user_input}: Incorrect input type, expected {input_type.__name__!r}"
            )



def main():
    while True:
        print(" Linear Discriminant Analysis ".center(50, "*"))
        print("*" * 50, "\n")
        print("First of all we should specify the number of classes that")
        print("we want to generate as training dataset")
        
        n_classes = valid_input(
            input_type=int,
            condition=lambda x: x > 0,
            input_msg="Enter the number of classes (Data Groupings): ",
            err_msg="Number of classes should be positive!",
        )

        print("-" * 100)

        
        std_dev = valid_input(
            input_type=float,
            condition=lambda x: x >= 0,
            input_msg=(
                "Enter the value of standard deviation"
                "(Default value is 1.0 for all classes): "
            ),
            err_msg="Standard deviation should not be negative!",
            default="1.0",
        )

        print("-" * 100)

        
        
        counts = []  
        for i in range(n_classes):
            user_count = valid_input(
                input_type=int,
                condition=lambda x: x > 0,
                input_msg=(f"Enter The number of instances for class_{i + 1}: "),
                err_msg="Number of instances should be positive!",
            )
            counts.append(user_count)
        print("-" * 100)

        
        user_means = []
        for a in range(n_classes):
            user_mean = valid_input(
                input_type=float,
                input_msg=(f"Enter the value of mean for class_{a + 1}: "),
                err_msg="This is an invalid value.",
            )
            user_means.append(user_mean)
        print("-" * 100)

        print("Standard deviation: ", std_dev)
        
        for i, count in enumerate(counts, 1):
            print(f"Number of instances in class_{i} is: {count}")
        print("-" * 100)

        
        for i, user_mean in enumerate(user_means, 1):
            print(f"Mean of class_{i} is: {user_mean}")
        print("-" * 100)

        
        x = [
            gaussian_distribution(user_means[j], std_dev, counts[j])
            for j in range(n_classes)
        ]
        print("Generated Normal Distribution: \n", x)
        print("-" * 100)

        
        y = y_generator(n_classes, counts)
        print("Generated Corresponding Ys: \n", y)
        print("-" * 100)

        
        actual_means = [calculate_mean(counts[k], x[k]) for k in range(n_classes)]
        
        
        for i, actual_mean in enumerate(actual_means, 1):
            print(f"Actual(Real) mean of class_{i} is: {actual_mean}")
        print("-" * 100)

        
        probabilities = [
            calculate_probabilities(counts[i], sum(counts)) for i in range(n_classes)
        ]

        
        
        for i, probability in enumerate(probabilities, 1):
            print(f"Probability of class_{i} is: {probability}")
        print("-" * 100)

        
        variance = calculate_variance(x, actual_means, sum(counts))
        print("Variance: ", variance)
        print("-" * 100)

        
        
        pre_indexes = predict_y_values(x, actual_means, variance, probabilities)
        print("-" * 100)

        
        print(f"Accuracy: {accuracy(y, pre_indexes)}")
        print("-" * 100)
        print(" DONE ".center(100, "+"))

        if input("Press any key to restart or 'q' for quit: ").strip().lower() == "q":
            print("\n" + "GoodBye!".center(100, "-") + "\n")
            break
        system("cls" if name == "nt" else "clear")  


if __name__ == "__main__":
    main()
