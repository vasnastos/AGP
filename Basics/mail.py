import re
import unittest as un

def mail_regex(ml):
    if re.match('[A-Za-z][A-Za-z0-9]*@[A-Za-z0-9]*\.[a-z]{2,3}',ml):
        return str(ml)+' is valid'
    else:
        return str(ml)+' is not valid'

def mails():
    y=open('mails.txt','r')
    for x in y:
        print(mail_regex(x.strip()))
    y.close()

def main():
    mails()

class test(un.TestCase):
    def mailchecker(self):
        self.assertTrue(mail_regex('email@vnas.com'))
        self.assertFalse(mail_regex('1)1ghl.@com'))
        self.assertTrue('nastosvasileios99@gmail.com')
        self.assertTrue('cgogos@uoi.gr')

if __name__=='__main__':
    main()
    print('----------------------------')
    print('Tests running')
    un.main()