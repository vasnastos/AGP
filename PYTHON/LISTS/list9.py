word="""Thirty minutes to Litchfield, sir," the first officer repeated, and
gave him the clipboard to check the luggage list. Valises, two;
trunks, two; microbook case, one. The last item fanned a small flicker
of anger, not at any person, not even at himself, but at the whole
infernal situation. He nodded.
"""

import re
words=re.split('[ ,.;:!,\n]',word)
counter=dict()
for word in words:
  if word in counter:
      counter[word]+=1
  else:
      counter[word]=1
print(counter)