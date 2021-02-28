import unittest as un

def Parag(i):
    s=1
    for x in range(1,i+1):
       s*=int(x)
    return s

def sum(i):
    j=1
    s=0
    while j<=i:
      s+=int(j)
      j+=1
    return s

def max(a,b):
    if float(a)>float(b):
        return a
    return b

class test(un.TestCase):
    def test_page(self):
        self.assertTrue(int(Parag(3))==6)
        self.assertEqual(int(Parag(4)),24)
    def test_max(self):
        self.assertTrue(int(max(12,6))==12)
        self.assertTrue(int(max(15,16))==16)
        self.assertGreater(8,2)
    def test_sum(self):
        self.assertTrue(int(sum(3))==6)
        self.assertTrue(int(sum(6))==21)
    def len_test(self):
        self.assertEqual(4*'a','aaaa')
        self.assertEqual(len('Hello_world'),11)
        self.assertTrue('heLLo'.toupper()=='HELLO')
if __name__=='__main__':
    un.main()

#assertEqual(a,b)-->Ελέγχει αν το a==b
#assertTrue(condition)-->Ελέγχει αν η συνθήκη είναι αληθής για
# να περάσει το τεστ. 