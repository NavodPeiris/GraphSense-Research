

def compute_transform_tables(
    source_string: str,
    destination_string: str,
    copy_cost: int,
    replace_cost: int,
    delete_cost: int,
    insert_cost: int,
) -> tuple[list[list[int]], list[list[str]]]:
    source_seq = list(source_string)
    destination_seq = list(destination_string)
    len_source_seq = len(source_seq)
    len_destination_seq = len(destination_seq)
    costs = [
        [0 for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)
    ]
    ops = [
        ["0" for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)
    ]

    for i in range(1, len_source_seq + 1):
        costs[i][0] = i * delete_cost
        ops[i][0] = f"D{source_seq[i - 1]}"

    for i in range(1, len_destination_seq + 1):
        costs[0][i] = i * insert_cost
        ops[0][i] = f"I{destination_seq[i - 1]}"

    for i in range(1, len_source_seq + 1):
        for j in range(1, len_destination_seq + 1):
            if source_seq[i - 1] == destination_seq[j - 1]:
                costs[i][j] = costs[i - 1][j - 1] + copy_cost
                ops[i][j] = f"C{source_seq[i - 1]}"
            else:
                costs[i][j] = costs[i - 1][j - 1] + replace_cost
                ops[i][j] = f"R{source_seq[i - 1]}" + str(destination_seq[j - 1])

            if costs[i - 1][j] + delete_cost < costs[i][j]:
                costs[i][j] = costs[i - 1][j] + delete_cost
                ops[i][j] = f"D{source_seq[i - 1]}"

            if costs[i][j - 1] + insert_cost < costs[i][j]:
                costs[i][j] = costs[i][j - 1] + insert_cost
                ops[i][j] = f"I{destination_seq[j - 1]}"

    return costs, ops


def assemble_transformation(ops: list[list[str]], i: int, j: int) -> list[str]:
    if i == 0 and j == 0:
        return []
    elif ops[i][j][0] in {"C", "R"}:
        seq = assemble_transformation(ops, i - 1, j - 1)
        seq.append(ops[i][j])
        return seq
    elif ops[i][j][0] == "D":
        seq = assemble_transformation(ops, i - 1, j)
        seq.append(ops[i][j])
        return seq
    else:
        seq = assemble_transformation(ops, i, j - 1)
        seq.append(ops[i][j])
        return seq


if __name__ == "__main__":
    _, operations = compute_transform_tables("Python", "Algorithms", -1, 1, 2, 2)

    m = len(operations)
    n = len(operations[0])
    sequence = assemble_transformation(operations, m - 1, n - 1)

    string = list("Python")
    i = 0
    cost = 0

    with open("min_cost.txt", "w") as file:
        for op in sequence:
            print("".join(string))

            if op[0] == "C":
                file.write("%-16s" % "Copy %c" % op[1])  
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost -= 1
            elif op[0] == "R":
                string[i] = op[2]

                file.write("%-16s" % ("Replace %c" % op[1] + " with " + str(op[2])))  
                file.write("\t\t" + "".join(string))
                file.write("\r\n")

                cost += 1
            elif op[0] == "D":
                string.pop(i)

                file.write("%-16s" % "Delete %c" % op[1])  
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost += 2
            else:
                string.insert(i, op[1])

                file.write("%-16s" % "Insert %c" % op[1])  
                file.write("\t\t\t" + "".join(string))
                file.write("\r\n")

                cost += 2

            i += 1

        print("".join(string))
        print("Cost: ", cost)

        file.write("\r\nMinimum cost: " + str(cost))
