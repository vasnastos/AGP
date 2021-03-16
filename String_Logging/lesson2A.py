"""
Γράψτε μια συνάρτηση που να δέχεται δύο λεκτικά ίσου μήκους και 
να επιστρέφει την απόσταση Hamming (δηλαδή το πλήθος των αντίστοιχων χαρακτήρων που διαφέρουν στα δύο λεκτικά)
"""

def hamming(s,t):
    assert len(s)==len(t)
    hd=0
    for x in range(len(s)):
        if str(s[int(x)])!=str(t[int(x)]):
            hd+=1
    return hd

def main():
    d1="GAGCCTACTAACGGGAT"
    d2="CATCGTAATGACGGCCT"
    print(f'Phrase1:{d1}')
    print(f'Phrase2:{d2}')
    print(f'Hamming:{hamming(d1,d2)}')

if __name__=='__main__':
    main()