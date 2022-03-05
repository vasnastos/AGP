def is_pantogramma(source:str):
    greek_letters=['Α' ,'Β' ,'Γ' ,'Δ' ,'Ε' ,'Ζ' ,'Η' ,'Θ' ,'Ι' ,'Κ' ,'Λ' ,'Μ' ,'Ν' ,'Ξ' ,'Ο' ,'Π' ,'Ρ' ,'Σ' ,'Τ' ,'Υ' ,'Φ','Χ' ,'Ψ','Ω']
    sub_letters={'Ά':'Α','Ί':'Ι','Έ':'Ε','Ή':'Η','Ό':'Ο','Ώ':'Ω'}
    letters_showed=set()
    for letter in list(source):
        if letter.upper() in sub_letters:
            letters_showed.add(sub_letters[letter.upper()])
        else:
            letters_showed.add(letter.upper())

    return len([x for x in letters_showed if x in greek_letters])==len(greek_letters)

if __name__ == '__main__':
    print('Pantogramma:',is_pantogramma('Ξεσκεπάζω την ψυχοφθόρα βδελυγμία'))
    print('Pantogramma:',is_pantogramma('Φθηνό μπλε βράδυ, στο Γκάζι ξεψυχώ…'))
    print('Pantogramma:',is_pantogramma('Ζαφείρι δέξου πάγκαλο, βαθών ψυχής το σήμα'))