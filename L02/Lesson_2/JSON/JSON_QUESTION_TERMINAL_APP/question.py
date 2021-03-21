import json as j
import random as r
#pip install termcolor
import termcolor as tc

#question,options,answer

r.seed()

class question:
   def __init__(self):
       self.categories={}
       self.cats=list([])
       self.questions={}
   def Open(self):
       self.categories.clear()
       self.questions.clear()
       with open('JSON/questions.json','r') as f:
           self.categories=j.load(f)
       self.questions=self.categories['quiz']
       self.cats=list(self.questions.keys())
   def  get_Question(self):
       category=r.randint(0,len(self.cats)-1)
       available_questions=self.questions[self.cats[int(category)]]
       qst=list(available_questions.keys())
       option=r.randint(0,len(qst)-1)
       print(available_questions[qst[int(option)]]['question'])
       options=list(available_questions[qst[int(option)]]['options'])
       answer=available_questions[qst[int(option)]]['answer']
       counter=1
       for x in options:
          print(str(counter)+'.'+str(x))
          counter+=1
       print('---------------------------------------')
       x=input('Select the correct answer:')
       correctindex=options.index(answer)
       if int(x)-1==int(correctindex):
           print(tc.colored('!!!!!You select the correct answer-->'+str(answer),'green'))
       else:
           print(tc.colored('XXXXX  -->The correct answer is '+str(answer),'red'))
def main():
    q=question()
    q.Open()
    q.get_Question()

if __name__=='__main__':
    main()