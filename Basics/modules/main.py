import temperature as t
import database as d
import os
import webbrowser as wb

def html_Preview(list):
    html="<html><head><title>Database Temps</title><style>table{background-color:blue; color:white; font-size:21px; font-wieght:18px; text-align:center; width:70%; height:auto; border:1px solid white;} th{background-color:gray; color:darkgreen; font-size:21px;} hr{border-top:2px solid red;}</style></head><body><center><h1>Temperatures By Database Project</h1><hr><table border=\"1\"><tr><th>Date</th><th>Celsium</th><th>Fahrenheit</th><th>Kelvin</th><th>Rankine</th></tr>"
    for x in list:
      html+=x.toBoardRow()
    html+='</table></center></body></html>'
    print(html)
    y=open('modules/preview.html','w')
    y.write(html)
    y.close()
    file=os.getcwd()+'\\modules\\preview.html'
    k=input('Do you want to open the file(y/n):')
    if k.upper()=='Y':
       wb.open_new_tab(file)

def main():
    db=d.database()
    temps=db.getTemperatures()
    db.Close()
    html_Preview(temps)

if __name__=='__main__':
    main()