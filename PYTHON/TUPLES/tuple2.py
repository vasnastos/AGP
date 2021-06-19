#Convert a Tuple To A String
atuple=('VASILIS','NASTOS','\tARTA','6912345678')
header=['NAME','LASTNAME','LOCATION','PHONE']
print('\t'.join(header))
print("\t".join(atuple))