"""
Δίνεται ο ακόλουθος κώδικας που ορίζει την κλάση Juice και υπερφορτώνει τον τελεστή +.
-Προσθέστε το επιπλέον πεδίο τιμή (price).
-Όταν εφαρμόζεται ο τελεστής πρόσθεσης ο νέος χυμός να έχει τιμή αναλογικά ίση με βάση την τιμή του κάθε χυμού.
-Προσθέστε τη μέθοδο pour() που να δέχεται ως παράμετρο μια τιμή από το 0% μέχρι το 100% και να επιστρέφει 
ένα νέο αντικείμενο Juice με το χυμό που προκύπτει αν ληφθεί το αντίστοιχο ποσοστό περιεχομένου από το 
καλών αντικείμενο.
"""

class Juice:
    def __init__(self, name, capacity,price):
        self.name = name
        self.capacity = capacity
        self.price=price

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)-->'+str(self.price))

    def __add__(self, other):
        newprice=(float(self.price)*float(self.capacity)+float(other.price)*float(other.capacity))/(float(self.price)+float(other.price))
        return Juice(self.name + '&' + other.name, self.capacity + other.capacity, newprice)
    
    def pour(self,pr):
        newcapacity=(float(pr)*float(self.capacity))/100
        self.capacity-=newcapacity
        newprice=(float(pr)*float(self.price))/100
        self.price-=newprice
        print(f'New Capacity:{newcapacity}-New Price:{newprice}')
        return Juice(self.name,newcapacity,newprice)

def main():
    j1=Juice('Orange',1.5,2)
    j2=Juice('Apple',3.5,1.5)
    print(j1+j2)
    print(j1.pour(50))
    print(j2.pour(70))

if __name__=='__main__':
    main()