
class temperature:
    def __init__(self,d,t):
        self.date=d
        self.temp=t
    def fahreheit(self):
        return float(self.temp)*(9/5)+32
    def Kelvin(self):
        return float(self.temp)+273.15
    def rankine(self):
        return float(self.temp)+273.15*(9/5)
    def toBoardRow(self):
        return "<tr><td>"+str(self.date)+'</td><td>'+str(self.temp)+'C</td><td>'+str(self.fahreheit())+'F</td><td>'+str(self.Kelvin())+'K</td><td>'+str(self.rankine())+'R</td></tr>'