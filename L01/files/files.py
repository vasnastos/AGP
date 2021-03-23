
#Άνοιγμα αρχείου
y=open('./files/file1.txt','r')
nums=[int(x) for x in y]
y.close()

#Εκτύπωση σε αρχείο
x=input('Δώσε όνομα αρχείου:')
y=open(x,'w')
y.write('\t\tResults\n')
y.write('******************************************************\n')
y.write('Summary:'+str(sum(nums))+'\n')
y.write('Average:'+str(sum(nums)/len(nums))+'\n')
y.write('Min:'+str(min(nums))+'\n')
y.write('Max:'+str(max(nums))+'\n')