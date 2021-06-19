# Εύρεση email με χρήση κανονικής έκφρασης
import re

pattern=re.compile('\w+[@]\w+\.[a-z]{2,3}')


mails=['123@outlook.com','nvgit@uoi.gr','angol@hello.out','dilik@uoi.gr','cvb@hotmail.com','12244455','fhgjfdkglfd']
print(pattern.finditer(mails))