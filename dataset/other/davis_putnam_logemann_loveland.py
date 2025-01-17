


from __future__ import annotations

import random
from collections.abc import Iterable


class Clause:

    def __init__(self, literals: list[str]) -> None:
        
        self.literals: dict[str, bool | None] = {literal: None for literal in literals}

    def __str__(self) -> str:
        return "{" + " , ".join(self.literals) + "}"

    def __len__(self) -> int:
        return len(self.literals)

    def assign(self, model: dict[str, bool | None]) -> None:
        for literal in self.literals:
            symbol = literal[:2]
            if symbol in model:
                value = model[symbol]
            else:
                continue
            
            if value is not None and literal.endswith("'"):
                value = not value
            self.literals[literal] = value

    def evaluate(self, model: dict[str, bool | None]) -> bool | None:
        for literal in self.literals:
            symbol = literal.rstrip("'") if literal.endswith("'") else literal + "'"
            if symbol in self.literals:
                return True

        self.assign(model)
        for value in self.literals.values():
            if value in (True, None):
                return value
        return any(self.literals.values())


class Formula:

    def __init__(self, clauses: Iterable[Clause]) -> None:
        self.clauses = list(clauses)

    def __str__(self) -> str:
        return "{" + " , ".join(str(clause) for clause in self.clauses) + "}"


def generate_clause() -> Clause:
    literals = []
    no_of_literals = random.randint(1, 5)
    base_var = "A"
    i = 0
    while i < no_of_literals:
        var_no = random.randint(1, 5)
        var_name = base_var + str(var_no)
        var_complement = random.randint(0, 1)
        if var_complement == 1:
            var_name += "'"
        if var_name in literals:
            i -= 1
        else:
            literals.append(var_name)
        i += 1
    return Clause(literals)


def generate_formula() -> Formula:
    clauses: set[Clause] = set()
    no_of_clauses = random.randint(1, 10)
    while len(clauses) < no_of_clauses:
        clauses.add(generate_clause())
    return Formula(clauses)


def generate_parameters(formula: Formula) -> tuple[list[Clause], list[str]]:
    clauses = formula.clauses
    symbols_set = []
    for clause in formula.clauses:
        for literal in clause.literals:
            symbol = literal[:2]
            if symbol not in symbols_set:
                symbols_set.append(symbol)
    return clauses, symbols_set


def find_pure_symbols(
    clauses: list[Clause], symbols: list[str], model: dict[str, bool | None]
) -> tuple[list[str], dict[str, bool | None]]:
    pure_symbols = []
    assignment: dict[str, bool | None] = {}
    literals = []

    for clause in clauses:
        if clause.evaluate(model):
            continue
        for literal in clause.literals:
            literals.append(literal)

    for s in symbols:
        sym = s + "'"
        if (s in literals and sym not in literals) or (
            s not in literals and sym in literals
        ):
            pure_symbols.append(s)
    for p in pure_symbols:
        assignment[p] = None
    for s in pure_symbols:
        sym = s + "'"
        if s in literals:
            assignment[s] = True
        elif sym in literals:
            assignment[s] = False
    return pure_symbols, assignment


def find_unit_clauses(
    clauses: list[Clause],
    model: dict[str, bool | None],  
) -> tuple[list[str], dict[str, bool | None]]:
    unit_symbols = []
    for clause in clauses:
        if len(clause) == 1:
            unit_symbols.append(next(iter(clause.literals.keys())))
        else:
            f_count, n_count = 0, 0
            for literal, value in clause.literals.items():
                if value is False:
                    f_count += 1
                elif value is None:
                    sym = literal
                    n_count += 1
            if f_count == len(clause) - 1 and n_count == 1:
                unit_symbols.append(sym)
    assignment: dict[str, bool | None] = {}
    for i in unit_symbols:
        symbol = i[:2]
        assignment[symbol] = len(i) == 2
    unit_symbols = [i[:2] for i in unit_symbols]

    return unit_symbols, assignment


def dpll_algorithm(
    clauses: list[Clause], symbols: list[str], model: dict[str, bool | None]
) -> tuple[bool | None, dict[str, bool | None] | None]:
    check_clause_all_true = True
    for clause in clauses:
        clause_check = clause.evaluate(model)
        if clause_check is False:
            return False, None
        elif clause_check is None:
            check_clause_all_true = False
            continue

    if check_clause_all_true:
        return True, model

    try:
        pure_symbols, assignment = find_pure_symbols(clauses, symbols, model)
    except RecursionError:
        print("raises a RecursionError and is")
        return None, {}
    p = None
    if len(pure_symbols) > 0:
        p, value = pure_symbols[0], assignment[pure_symbols[0]]

    if p:
        tmp_model = model
        tmp_model[p] = value
        tmp_symbols = list(symbols)
        if p in tmp_symbols:
            tmp_symbols.remove(p)
        return dpll_algorithm(clauses, tmp_symbols, tmp_model)

    unit_symbols, assignment = find_unit_clauses(clauses, model)
    p = None
    if len(unit_symbols) > 0:
        p, value = unit_symbols[0], assignment[unit_symbols[0]]
    if p:
        tmp_model = model
        tmp_model[p] = value
        tmp_symbols = list(symbols)
        if p in tmp_symbols:
            tmp_symbols.remove(p)
        return dpll_algorithm(clauses, tmp_symbols, tmp_model)
    p = symbols[0]
    rest = symbols[1:]
    tmp1, tmp2 = model, model
    tmp1[p], tmp2[p] = True, False

    return dpll_algorithm(clauses, rest, tmp1) or dpll_algorithm(clauses, rest, tmp2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    formula = generate_formula()
    print(f"The formula {formula} is", end=" ")

    clauses, symbols = generate_parameters(formula)
    solution, model = dpll_algorithm(clauses, symbols, {})

    if solution:
        print(f"satisfiable with the assignment {model}.")
    else:
        print("not satisfiable.")
