#Άνοιγμα αρχείου και εύρεση μέσου όρου βαθμολογιών

def write(avg):
    y=open('file(txt)/students.txt','a')
    y.write('\nAverage:'+str(avg))
    y.close()

#Δήλωση συνάρτησης
def main():
    ln=0
    y=open('file(txt)/students.txt','r')
    summary=0
    for k in y:
       summary+=float(k)
       ln+=1
    y.close()
    print('Average grade is:%.3f' % (summary/ln))
    write(summary/ln)

if __name__=='__main__':
    main()
