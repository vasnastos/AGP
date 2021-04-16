import pip._vendor.requests as req
from lxml import html 
import pickle
import bs4
def Decode(response):
    soup=bs4.BeautifulSoup(response.text,features='lxml')
    table=soup.findAll('table')
    for x in table:
        cells=x.findAll('tr')
        for tr in cells:
            for td in tr.findAll('td'):
               tddec=str(td).replace('<br/>',' ')
               print(html.fromstring(tddec).text_content(),end=' ')
            print(end='\n')

def scrap_table(response):
    soup=bs4.BeautifulSoup(response.text,features='lxml')
    table=soup.findAll('table')
    contents=[]
    for x in table:
        cells=x.findAll('tr')
        for tr in cells:
            msg=''
            for td in tr.findAll('td'):
               tddec=str(td).replace('<br/>',' ')
               msg+=html.fromstring(tddec).text_content()+' '
            contents.append(msg)
    with open('staff','wb') as f:
        pickle.dump(contents,f)

resp=req.get('https://www.dit.uoi.gr/members.php')
Decode(resp)
scrap_table(resp)
print('===================================================')
print('\t\tLoading from file')
with open('staff','rb') as pickleload:
    data=pickle.load(pickleload)
#print(data)