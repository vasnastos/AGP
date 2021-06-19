import re
import os
# Εύρεση όλων των txt αρχείων στον Φάκελο DATA
path=os.path.join('..','DATA')
for file in os.listdir(path):
    if re.match('.*\.txt$',file):
        print(file)

# PassWord που περιέχουν τουλάχιστον ένα γραμμα και έναν αριθμό με μήκος 
# 8 ψηφία

y=open(os.path.join('..','DATA','passwords.txt'),'r')
for password in y.readlines():
    password=password.strip()
    if re.search('^((?=.*\d.[A-za-z].[@!$%*>!;])|(?=.*[@!$%*>!;]\d.[A-za-z])|(?=.*[@!$%*>!;].[A-za-z].\d)|(?=.*[A-za-z].[@!$%*>!;].\d)).{8,}',password):
        print(password)
y.close()

