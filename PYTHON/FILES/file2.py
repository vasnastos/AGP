import pickle 
import os

def Random_Records():
    return {chr(i):i for i in range(65,91)}

if __name__=='__main__':
   file=os.path.join('..','DATA','serializeD')
   with open(file,'wb') as F:
       pickle.dump(Random_Records(),F)

   with open(file,'rb') as RF:
       print(pickle.load(RF))
   
   fp=os.path.join('..','DATA','SD.sol')
   with open(fp,'w') as F:
       nkl=Random_Records()
       for n in nkl:
            F.write(f'LETTER:{n}\tVALUE:{nkl[n]}\n')
