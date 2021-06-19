import re 
# Εύρεση χαρακτήρων,ψηφίων,συμβόλων σε αλφαριθμητικό

strng="""Maybe you do. I've been away for six years. Tell me, are they having
labor trouble now?"."Labor trouble?" The mate was surprised. "You mean with the
farm-tramps? Ten of them for every job, if you call that trouble."
"Well, I noticed you have steel gratings over the gangway heads to the
lower deck, and all your crewmen are armed. Not just pistols, either."
"Oh. That's on account of pirates.
"""

print(strng)
print('--'*20)
print("String length:{}".format(len(strng)))
print('Digits:{}'.format(len(re.findall("\d",strng))))
print('Characters:{}'.format(len(re.findall("\w",strng))))
print("Symbols:{}".format(len(strng)-len(re.findall('\d',strng))-len(re.findall('\w',strng))))