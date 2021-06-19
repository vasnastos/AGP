#1.Given a list of numbers, write a list comprehension that produces a list of each number doubled.
def doubled(alist):
    """Doubled:
    >>doubled([1,2])
    [2,4]
    >>doubled([1,2,4,5])
    [1,4,16,25]
    >>doubled([])
    []
    """
    pass

#2.Given a list of numbers, find the precent of positive numbers using list comprehension.
def Positive(mylist):
    """Positive:
    >>Positive([1,2,-1,4])
    75.000
    >>Positive([-1,2])
    50.000
    """
    pass

#3.Given a sentence, produce a dictionaty of pairs word-length of word in the sentence, but only if the word is not 'the' or 'and'.
#Words split with ' ',',','.','-'
def words_not_the_and(sentence):
    """Words_not_the_and
    >>words_not_the_and('The quick brown fox')
    {'quick':5,'brown':5,'fox':3}
    """
    pass

#4.Given a string representing a word, write a list comprehension that finds all the distinct letters of the sentence.
def Distinct_Letters(word):
    """
    Distinct_Letters
    >>Distinct_Letters('Hello')
    ['H','e','l','l','o']
    """
    pass

#5.Given a sentence, return the sentence with all vowels removed,using list comprehension.
def Remove_vowels(sentence):
    """
    Remove_vowels
    >>Remove_vowels('Hello word')
    Hll wrd
    """
    pass

#6.Given a sentence, return the setence will all it's letter transposed by 1.Use List Comprehension
def Encrypt(word):
    """Encrypt
    >>Encrypt('aab')
    bbc
    >>Encrypt('aef')
    bfg
    """
    pass

def main1():
    mylist=[1,2,4,5,6,8]
    doubled(mylist)
    #Output->[2,3,16,25,36,64]

def main2():
    mylist=[25, 91, 22, -7, -20,-56,-12,-1,89,5,-9,56,1,-4]
    Positive(mylist)

def main3():
    sentence="""There are incredible things still
undiscovered; most of the important installations were built in
duplicate as a precaution against space attack. I know where all of
them are.But I could find nothing, not one single word, about any giant
strategic planning computer called Merlin! Nevertheless the leading men of the planet didn't believe him. They
couldn't, for the search for Merlin had become their abiding
obsession. Merlin meant everything to them: power, pleasures, and
profits unlimited.Conn had known they'd never believe him, and so he had a trick or two
up his space-trained sleeve that might outwit even their fabled Cosmic
Computer ... if they dared accept his challenge.
    """  
    words_not_the_and(sentence)  

def main4():
    word="""It may be stated that he lives in Williamsport,
Pennsylvania, that he is an expert on the history and use of hand
weapons, that he has been writing and selling science-fiction for many
years to the leading magazines, and that he is highly rated among
readers for his skill and imagination. He has had several novels
published, including mysteries and juveniles."""
    Distinct_Letters(word)

def main5():
    word="""It had been six months to Litchfield when the _Mizar_ lifted out of La
Plata Spaceport and he watched Terra dwindle away. It had been two
months to Litchfield when he boarded the _City of Asgard_ at the port
of the same name on Odin. It had been two hours to Litchfield when the
_Countess Dorothy_ rose from the airship dock at Storisende. He had
had all that time, and now it was gone, and he was still unprepared
for what he must face at home."""
    Remove_vowels(word)


def main6():
    en="the quick brown fox jumps over the lazy dog"
    Encrypt(en)

def Scenario_1():
    import doctest
    if doctest.testmod().failed==0:
        print('Tests passed')

def Scenario_2():
    main1()
    print('\n\n')
    main2()
    print('\n\n')
    main3()
    print('\n\n')
    main4()
    print('\n\n')
    main5()
    print('\n\n')
    main6()

if __name__=='__main__':
    choice=int(input('Select Scenario(1|2):'))
    if choice==1:
        Scenario_1()
    else:
        Scenario_2()