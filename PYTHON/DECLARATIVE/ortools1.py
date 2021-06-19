from ortools.sat.python import cp_model

#Problem
#x + 7 * y <= 50.
#3<=x <= 15.
#X+y=14
#2<=y<=5

model=cp_model.CpModel()
x=model.NewIntVar(3,15,'X')
y=model.NewIntVar(2,5,'Y')
model.Add(x+7*y==50)
model.Add(x+y==20)

solver=cp_model.CpSolver()
status=solver.Solve(model)
print('Status:{}'.format(solver.StatusName(status)))
if status==cp_model.OPTIMAL:
    print('X={}\nY={}\n'.format(solver.Value(x),solver.Value(y)))
print('Execution Time:{}'.format(solver.WallTime()))