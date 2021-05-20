from ortools.linear_solver import pywraplp as pw

def main():
    solver=pw.Solver.CreateSolver('GLOP')
    #Glop Open Source Library for Solving Optimization Problems
    #0<=x<=1  && 0<=y<=2
    x=solver.NumVar(0,1,'x')
    y=solver.NumVar(0,2,'y')
    print('Number of Variables:'+str(solver.NumVariables()))
    
    #x+y<=2
    ct=solver.Constraint(0,2,'ct')
    ct.SetCoefficient(x,1)
    ct.SetCoefficient(y,1)
    print('Number of Constaints:'+str(solver.NumConstraints()))
    
    #3*x*y
    obj=solver.Objective()
    obj.SetCoefficient(x,3)
    obj.SetCoefficient(y,1)
    obj.SetMaximization()

    #Solve the problem
    solver.Solve()
    print('Solution Genarated')
    print(f'Objective value:{obj.Value()}')
    print(f'x={x.solution_value()}')
    print(f'y={y.solution_value()}')

if __name__=='__main__':
    main()

