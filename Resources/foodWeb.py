from ortools.sat.python import cp_model  # CP-SAT επιλυτής


# Δημιουργία του μοντέλου
model = cp_model.CpModel()

# Μεταβλητές απόφασης
dragonfly = model.NewIntVar(0, 2, "dragonfly")
frog = model.NewIntVar(0, 2, "frog")
snake = model.NewIntVar(0, 2, "snake")
vulture = model.NewIntVar(0, 2, "vulture")
fox = model.NewIntVar(0, 2, "fox")
butterfly = model.NewIntVar(0, 2, "butterfly")
grasshopper = model.NewIntVar(0, 2, "grasshopper")
bird = model.NewIntVar(0, 2, "bird")
mouse = model.NewIntVar(0, 2, "mouse")
rabbit = model.NewIntVar(0, 2, "rabbit")

# Περιορισμοί
model.Add(dragonfly != frog)
model.Add(frog != snake)
model.Add(snake != vulture)
model.Add(frog != butterfly)
model.Add(frog != grasshopper)
model.Add(snake != bird)
model.Add(vulture != bird)
model.Add(vulture != fox)
model.Add(vulture != mouse)
model.Add(fox != mouse)
model.Add(rabbit != vulture)
model.Add(fox != rabbit)

# Κλήση του επιλυτή
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Εκτύπωση του αποτελέσματος
if status == cp_model.OPTIMAL:
    print(f"dragonfly = {solver.Value(dragonfly)}")
    print(f"frog = {solver.Value(frog)}")
    print(f"snake = {solver.Value(snake)}")
    print(f"vulture = {solver.Value(vulture)}")
    print(f"fox = {solver.Value(fox)}")
    print(f"butterfly = {solver.Value(butterfly)}")
    print(f"grasshopper = {solver.Value(grasshopper)}")
    print(f"bird = {solver.Value(bird)}")
    print(f"mouse = {solver.Value(mouse)}")
    print(f"rabbit = {solver.Value(rabbit)}")
