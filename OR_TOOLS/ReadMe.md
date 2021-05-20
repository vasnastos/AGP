# OR_TOOLS SOLVER USING PYTHON

**:point_right:pip install ortools**

**:point_right:[https://developers.google.com/optimization/cp/cp_solver#python_5](https://developers.google.com/optimization/cp/cp_solver#python_5)**

## LINEAR OPTIMIZATION

The name given to Computing the best solution to a problem modeled as a set of linear relationships

## NQUEENS
The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. The eight queens puzzle is an example of the more general n queens problem of placing n non-attacking queens on an n×n chessboard, for which solutions exist for all natural numbers n with the exception of n = 2 and n = 3.


## OR_TOOLS SOLUTION
* Linear Solver
```
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
```
[linearsolver.py](linearsolver.py)


* Cp_Model
  * nqueens problem
  ```
    from ortools.sat.python import cp_model
    import sys

    class SolutionPrinter(cp_model.CpSolverSolutionCallback):
        def __init__(self,vars):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self.__variables=vars
            self.__solution_count=0
        def OnSolutionCallback(self):
            self.__solution_count+=1
            for v in self.__variables:
                print(f'{v} = {self.Value(v)}',end=' ')
            print()
        def Total_Solutions(self):
            return self.__solution_count



    def main(size_chess_board):
        print('Is In')
        model=cp_model.CpModel()
        queens=[model.NewIntVar(0,size_chess_board-1,f'x{i}') for i in range(size_chess_board)]
        model.AddAllDifferent(queens)
        for i in range(size_chess_board):
            diag1=[]
            diag2=[]
            for j in range(size_chess_board):
                q1=model.NewIntVar(0,2*size_chess_board,f'diag1_{i}')
                diag1.append(q1)
                model.Add(q1==queens[j]+j)
                q2=model.NewIntVar(-size_chess_board,size_chess_board,f'diag2_{i}')
                diag2.append(q2)
                model.Add(q2==queens[j]-j)
            model.AddAllDifferent(diag1)
            model.AddAllDifferent(diag2)
        solver=cp_model.CpSolver()
        sprinter=SolutionPrinter(queens)
        solver.SearchForAllSolutions(model,sprinter)
        print(f'\nSolutions Found:{sprinter.Total_Solutions()}')


    if __name__=='__main__':
        print('N Queen Problem using Or_TOOLS')
        queens=8
        main(queens)

[nqueens.py](nquens)

