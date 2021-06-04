from ortools.sat.python import cp_model


def rooks(n):
    # Initialize
    model = cp_model.CpModel()

    # Decision Variables
    xs = []
    ys = []
    for i in range(0, n):
        x = model.NewIntVar(0, n - 1, f"x{i}")
        y = model.NewIntVar(0, n - 1, f"y{i}")
        xs.append(x)
        ys.append(y)

    # Constraints
    model.AddAllDifferent(xs)
    model.AddAllDifferent(ys)

    # Solution
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    resultDictionary = dict()
    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        for i in range(0, n):
            x = solver.Value(xs[i])
            y = solver.Value(ys[i])
            resultDictionary[(x, y)] = True

    print(resultDictionary)

    for i in range(0, n):
        for j in range(0, n):
            if (i, j) in resultDictionary:
                print(" R ", end="")
            else:
                print(" _ ", end="")
        print("\n")


if __name__ == "__main__":
    n = 8
    rooks(n)
