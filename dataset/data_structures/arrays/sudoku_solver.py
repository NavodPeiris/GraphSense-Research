
import random
import time


def cross(items_a, items_b):
    
    return [a + b for a in items_a for b in items_b]


digits = "123456789"
rows = "ABCDEFGHI"
cols = digits
squares = cross(rows, cols)
unitlist = (
    [cross(rows, c) for c in cols]
    + [cross(r, cols) for r in rows]
    + [cross(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")]
)
units = {s: [u for u in unitlist if s in u] for s in squares}
peers = {s: {x for u in units[s] for x in u} - {s} for s in squares}


def test():
    "A set of unit tests."
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units["C2"] == [
        ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2"],
        ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
        ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"],
    ]
    
    assert peers["C2"] == {
        "A2", "B2", "D2", "E2", "F2", "G2", "H2", "I2", "C1", "C3",
        "C4", "C5", "C6", "C7", "C8", "C9", "A1", "A3", "B1", "B3"
    }
    
    print("All tests pass.")


def parse_grid(grid):
    
    values = {s: digits for s in squares}
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False  
    return values


def grid_values(grid):
    
    chars = [c for c in grid if c in digits or c in "0."]
    assert len(chars) == 81
    return dict(zip(squares, chars))


def assign(values, s, d):
    
    other_values = values[s].replace(d, "")
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d):
    
    if d not in values[s]:
        return values  
    values[s] = values[s].replace(d, "")
    
    if len(values[s]) == 0:
        return False 
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False  
        
        elif len(dplaces) == 1 and not assign(values, dplaces[0], d):
            return False
    return values


def display(values):
    
    width = 1 + max(len(values[s]) for s in squares)
    line = "+".join(["-" * (width * 3)] * 3)
    for r in rows:
        print(
            "".join(
                values[r + c].center(width) + ("|" if c in "36" else "") for c in cols
            )
        )
        if r in "CF":
            print(line)
    print()


def solve(grid):
    return search(parse_grid(grid))


def some(seq):
    
    for e in seq:
        if e:
            return e
    return False


def search(values):
    
    if values is False:
        return False  
    if all(len(values[s]) == 1 for s in squares):
        return values  
   
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])


def solve_all(grids, name="", showif=0.0):
    

    def time_solve(grid):
        start = time.monotonic()
        values = solve(grid)
        t = time.monotonic() - start
        
        if showif is not None and t > showif:
            display(grid_values(grid))
            if values:
                display(values)
            print(f"({t:.5f} seconds)\n")
        return (t, solved(values))

    times, results = zip(*[time_solve(grid) for grid in grids])
    if (n := len(grids)) > 1:
        print(
            "Solved %d of %d %s puzzles (avg %.2f secs (%d Hz), max %.2f secs)."  
            % (sum(results), n, name, sum(times) / n, n / sum(times), max(times))
        )


def solved(values):
    
    def unitsolved(unit):
        return {values[s] for s in unit} == set(digits)

    return values is not False and all(unitsolved(unit) for unit in unitlist)


def from_file(filename, sep="\n"):
    
    with open(filename) as file:
        return file.read().strip().split(sep)


def random_puzzle(assignments=17):
    
    values = {s: digits for s in squares}
    for s in shuffled(squares):
        if not assign(values, s, random.choice(values[s])):
            break
        ds = [values[s] for s in squares if len(values[s]) == 1]
        if len(ds) >= assignments and len(set(ds)) >= 8:
            return "".join(values[s] if len(values[s]) == 1 else "." for s in squares)
    return random_puzzle(assignments)  ## Give up and make a new puzzle


def shuffled(seq):
    
    seq = list(seq)
    random.shuffle(seq)
    return seq


grid1 = (
    "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
)
grid2 = (
    "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
)
hard1 = (
    ".....6....59.....82....8....45........3........6..3.54...325..6.................."
)

if __name__ == "__main__":
    test()
   
    solve_all([random_puzzle() for _ in range(99)], "random", 100.0)
    for puzzle in (grid1, grid2):  
        display(parse_grid(puzzle))
        start = time.monotonic()
        solve(puzzle)
        t = time.monotonic() - start
        print(f"Solved: {t:.5f} sec")
