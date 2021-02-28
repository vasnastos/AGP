import random as r
import webbrowser as wb
import os

class product:
    def __init__(self,n,id,pr):
        self.productname=n
        self.id=id
        self.price=pr
    def SetName(self,n):
        self.productname=n
    def GetName(self):
        return self.productname
    def SetProductID(self,i):
        self.id=i
    def GetProductID(self):
        return self.id
    def SetPrice(self,pr):
        self.price=pr
    def GetPrice(self):
        return self.price
    def __str__(self):
        return str(self.productname)+','+str(self.id)+','+str(self.price)
    def __lt__(self, value):
        return float(self.price)<float(value.price)

def saveToFile(table):
    file=os.getcwd()+'\\products.html'
    y=open(file,'w')
    y.write('<html><head><title>Products</title><style>table{background-color:gray; color:blue; text-align:center; font-size:18px; font-weight:bold; width:65%; border:1px solid green;} th{background-color:red; color:gray; font-size:21px;}</style></head><body><center><caption style=\"color:purple;\"><h1><u>PRODUCTS TABLE</u></h1></caption><table border=\"1\"><tr><th>NAME</th><th>ID</th><th>PRICE</th></tr>')
    for k in table:
        y.write('<tr><td>'+str(k.GetName())+'</td><td>'+str(k.GetProductID())+'</td><td>'+str(k.GetPrice())+'</td></tr>')
    y.write('</table><br><br></center></body></html>')
    y.close()
    output=input('Open html file(y/n):')
    if output.upper()=='Y':
        wb.open_new_tab(file)
def main():
    products=[]
    for x in range(30):
        products.append(product('Productname_'+str(x+1),r.randint(1000,5000),r.random()+r.randint(800,1200)))
    print('\t\tProducts')
    print('-----------------------------------------------')
    products.sort()
    for y in products:
        print(y)
    saveToFile(products)

if __name__=='__main__':
    main()