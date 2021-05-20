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
