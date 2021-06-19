from ortools.sat.python import cp_model

# Δημιουργία μοντέλου
model = cp_model.CpModel()

# Μεταβλητές απόφασης
x = model.NewIntVar(0, 9, "x")
y = model.NewIntVar(0, 9, "y")
z = model.NewIntVar(0, 9, "z")

# Περιορισμοί
model.Add(x + y + z == 15)
model.Add(x > y)
model.Add(z != 0)
model.AddAllDifferent([x, y, z])

# Δημιουργία του επιλυτή
solver = cp_model.CpSolver()

# Κλήση του επιλυτή
status = solver.Solve(model)

# Εμφάνιση λύσης
if status == cp_model.OPTIMAL:
    for decisionVariable in [x, y, z]:
        print(f"{decisionVariable}={solver.Value(decisionVariable)}")