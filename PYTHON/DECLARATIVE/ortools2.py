def LineDifferent():
   from ortools.sat.python import cp_model
   model=cp_model.CpModel()
   board1=[model.NewIntVar(1,10,'var{}'.format(i+1)) for i in range(10)]
   board2=[model.NewIntVar(1,10,'var{}'.format(i+1)) for i in range(10)]
   model.AddAllDifferent(board1)
   model.AddAllDifferent(board2)
   for i in range(10):
       model.Add(board1[i]!=board2[i])

   solver=cp_model.CpSolver()
   status=solver.Solve(model)
   print(solver.StatusName(status))
   if status==cp_model.OPTIMAL:
       b1=''
       b2=''
       for i in range(len(board1)):
        b1+=str(solver.Value(board1[i]))+'\t'
        b2+=str(solver.Value(board2[i]))+'\t'
       print('Solutions')
       print('Board1:'+b1)
       print('Board2:'+b2)
   print('Exec Time:{}'.format(solver.WallTime()))

LineDifferent()
       
    
