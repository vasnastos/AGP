import json as j
import random as r
#random Json Genarator Username and Codes

r.seed()
startchar=48
finishchar=125

def genarate_UserName():
    user=""
    length=r.randint(5,14)
    for x in range(length):
        user+=chr(r.randint(int(startchar),int(finishchar)))
    return user

def genarate_PassWord():
    length=r.randint(8,16)
    password=""
    for x in range(length):
        password+=chr(r.randint(int(startchar),int(finishchar)))
    return password

def saveJSon(names):
    file=input("Give filename you want to save the JSon arguments:")
    file+=".json"
    with open(file,'w') as f:
        data=[]
        for x in names:
            jsondict={}
            jsondict.update({"name":x})
            jsondict.update({"password":names[x]})
            data.append(jsondict)
        
        jsonfinalized={'credentials':data}
        j.dump(jsonfinalized,f,indent=len(data))

def main():
    x=input('Give number of pseudocreadentials you want to genarate:')
    creds={}
    for i in range(int(x)):
        creds.update({genarate_UserName():genarate_PassWord()})
    print(len(creds))
    saveJSon(creds)

if __name__=='__main__':
    main()


