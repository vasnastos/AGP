import requests
from collections import Counter
from prettytable import PrettyTable,ALL

def character_show_rate(url:str):
    r=requests.get(url)
    lines=r.text
    s_rate=Counter(lines)
    s_rate=dict(reversed(sorted(s_rate.items(),key=lambda x:x[1])))
    s_rate.pop(' ')
    keys=list(s_rate.keys())[:3]
    tb=PrettyTable(['KEY','VALUE'])
    tb.hrules=ALL
    for k in keys:
        tb.add_row([k,s_rate[k]])
    print(tb)

if __name__ == '__main__':
    character_show_rate('https://www.gutenberg.org/files/5200/5200-0.txt')