from xml.dom import minidom
import os

from collections import defaultdict

class Feature:
    def __init__(self,a,b):
        self.teama=a
        self.teamb=b
        self.features=[]
    
    def add_feature(self,slot):
        self.features.append(int(slot))
    
    def __eq__(self,feat:tuple):
        return (self.teama==feat[0] and self.teamb==feat[1]) or (self.teama==feat[1] and self.teamb==feat[0])

    def __str__(self):
        msg="Team A:{}".format(self.teama)+"\n"
        msg+="Team B:{}".format(self.teamb)+"\n"
        msg+="Features:["+"-".join([str(f) for f in self.features])+']\n\n'
        return msg
    
    def slots_difference(self):
        return max(self.features)-min(self.features)

def load_sports_timetabling():
    scores=minidom.parse(os.path.join('..','Source','sports_timetabling.xml'))
    data=scores.getElementsByTagName('ScheduledMatch')

    championship=[]
    for i in range(len(data)):
        team_a=data[i].attributes['home'].value
        team_b=data[i].attributes['away'].value
        if (team_a,team_b) not in championship:
            championship.append(Feature(team_a,team_b))
        championship[championship.index((team_a,team_b))].add_feature(data[i].attributes['slot'].value)
    return championship

if __name__ == '__main__':
    championship=load_sports_timetabling()
    for f in championship:
        print(f'Team {f.teama}-Team {f.teamb}=>{f.slots_difference()}')