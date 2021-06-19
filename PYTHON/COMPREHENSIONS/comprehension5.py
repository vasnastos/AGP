"""
sentences = ["a new world record was set", 
             "in the holy city of ayodhya", 
             "on the eve of diwali on tuesday", 
             "with over three lakh diya or earthen lamps", 
             "lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']
Comprehension which shows all the words which are not stopwords
"""

sentences = ["a new world record was set", 
             "in the holy city of ayodhya", 
             "on the eve of diwali on tuesday", 
             "with over three lakh diya or earthen lamps", 
             "lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']

print([word for word in sentences if word not in stopwords])


