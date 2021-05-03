import re 
from termcolor import cprint
import pip._vendor.requests as reqs

"""
Ημερομηνίες της μορφής yyyy­mm­dd (έτος, μήνας, ημέρα) από 1900­01­01 έως και 2099­12­31. Ως διαχωριστικό ανάμεσα στους αριθμούς να μπορεί να χρησιμοποιηθεί οποιοδήποτε από τα σύμβολα ­ / . και το κενό.
Θεωρείστε ότι το έτος μπορεί να λάβει τιμή από το 1900 έως το 2099, ο μήνας τιμή από το 01 μέχρι το 12
και η ημέρα του μήνα μπορεί να λάβει τιμή από το 01 μέχρι το 31 (δηλαδή, για παράδειγμα η τιμή 30/02/2019
θεωρείται στα πλαίσια της άσκησης ως έγκυρη).
Obtained by:https://www.dit.uoi.gr/e-class/modules/document/?course=238
"""

pattern=re.compile('((19[0-9][0-9]|20[0-9][0-9])[ ,-/](0[1-9]|1[012])[ ,-/](0[1-9]|[12][0-9]|3[01]))')


def searchre(alist):
    occurences=[]
    for x in alist:
       if pattern.search(x):
           occurences.append(x)
    for l in occurences:
        cprint(l,'red')


def FindAllRe(alist):
    occurences=[]
    for x in alist:
        occurences+=pattern.findall(x)
    for l in occurences:
        cprint(l[0],'green')

def Iterator(alist):
    for x in alist:
        for k in pattern.finditer(x):
            cprint(x[k.start():k.end()],'blue')

def Match(alist):
    for x in alist:
        if pattern.match(x):
            cprint(x,'yellow')


mylist=['1999-21-07','2002-10-11','1888-13-90','1999-06-19','1921 09 21  2020-08-14','2080/10/24  2090-11-01']
print('\t Method 1')
searchre(mylist)
print('\n\n')

print('\t Method 2')
FindAllRe(mylist)
print('\n\n')


print('\t Method 3')
Iterator(mylist)
print('\n\n')

print('\t Method 4')
Match(mylist)
print('\n\n')


strng=reqs.get('https://www.gutenberg.org/cache/epub/51482/pg51482.txt').text
print(re.sub('_.*_','==',strng))
data=re.split('[ ,.\n]',strng)
for x in data:
    print(x)
