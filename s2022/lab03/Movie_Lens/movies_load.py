# Data -->u.item
# Movie Info->u.data
import os
from collections import namedtuple
from re import S
from sqlite3 import Error
from prettytable import PrettyTable,ALL
import mysql.connector as cnt
from statistics import mean

class Database:
    @staticmethod
    def establish_connection():
        return cnt.connect(
            host='myweb.dit.uoi.gr',
            database='movielen',
            user='root',
            password='@Nji90okm'
        )
    
    def __init__(self):
        self.connector=None
        self.movies=[]
        self.evaluations=[]

    def insert_movie(self,movie:tuple):
        query='INSERT INTO movie(id,name,release_date,imdb) VALUES(?,?,?,?)'
        try:
            self.connector=Database.establish_connection()
            cursor=self.connector.cursor(prepared=True)
            cursor.execute(query,movie)
            self.connector.commit()
            self.connector.close()
        except cnt.Error as e:
            print('Error on myweb.dit.uoi.gr/movielen db-->Insert Movie')
            print(e)
            print(e.msg)
    def insert_evaluation(self,evaluation:tuple):
        query='INSERT INTO evaluation(user_id,movie_id,evaluation_score) VALUES(?,?,?)'
        try:
            self.connector=Database.establish_connection()
            cursor=self.connector.cursor(prepared=True)
            cursor.execute(query,(evaluation[0],evaluation[1],evaluation[2]))
            self.connector.commit()
            self.connector.close()
        except cnt.Error as e:
            print('Error on myweb.dit.uoi.gr/movielen db-->Insert evaluation')
            print(e)
            print(e.msg)

    def movies(self):
        query='SELECT * FROM movie'
        try:
            self.connector=Database.establish_connection()
            cursor=self.connector.cursor()
            cursor.execute(query)
            records=cursor.fetchall()
            self.connector.close()
            return records
        except cnt.Error:
            print('Error on myweb.dit.uoi.gr/movielen db')
            return None 

    def evaluations(self):
        query='SELECT * FROM evaluation'
        try:
            self.connector=Database.establish_connection()
            cursor=self.connector.cursor()
            cursor.execute(query)
            records=cursor.fetchall()
            self.connector.close()
            return records
        except:
            print('Error on myweb.dit.uoi.gr/movielen db')
            return None


class MovieLen:
    def __init__(self):
        self.movies=[]
        self.movies_evaluation=[]
        with open(os.path.join('..','Source','ml-100k','ml-100k','u.data')) as RF:
            for row in RF:
                data=row.split()
                self.movies_evaluation.append((int(data[0]),int(data[1]),int(data[2]),data[3]))
        evaluation=namedtuple('evaluation','id,title,date,imdb')
        with open(os.path.join('..','Source','ml-100k','ml-100k','u.item')) as RF:
            for row in RF:
                data=row.split('|')
                self.movies.append(evaluation._make([int(data[0]),data[1],data[2],data[4]]))

        self.split__()
    

    def split__(self):
        distinct_movies=set([x[1] for x in self.movies_evaluation])
        self.mvdb={
            id:{} for id in distinct_movies
        }
        for record in self.movies_evaluation:
            self.mvdb[record[1]][record[0]]=int(record[2])
    
    def movie_name(self,id:int):
        for movie in self.movies:
            if movie.id==id:
                return movie.title
        return "NOT REGISTER"

    def top_10(self):
        smvdb=dict(reversed(sorted(self.mvdb.items(),key=lambda x:mean(x[1].values()))))
        table=PrettyTable(['MOVIE NAME','USERS EVALUATED','MEAN EVALUATION SCORE'])
        table.hrules=ALL
        tc=0
        for mid,registries in smvdb.items():
            if tc==10: break
            table.add_row([self.movie_name(mid),len(registries.keys()),mean(list(registries.values()))])
            tc+=1
        print(table)

    def info(self):
        table=PrettyTable(['MOVIE NAME','USERS EVALUATED','MEAN EVALUATION SCORE'])
        table.hrules=ALL
        for mid,registries in self.mvdb.items():
            table.add_row([self.movie_name(mid),len(registries.keys()),mean(list(registries.values()))])
        print(table)

    def filter_movies(self,users_minimum_number:int,evaluation_score):
        if users_minimum_number!=-1:
            self.mvdb=dict(filter(lambda x:len(list(x[1].keys()))>=users_minimum_number,self.mvdb.items()))
        if evaluation_score!=0:
            self.mvdb=dict(filter(lambda x:mean(x[1].values())>=evaluation_score,self.mvdb.items()))

    def upload(self):
        db=Database()
        for record in self.movies:
            db.insert_movie(tuple(record))
        
        for record in self.movies_evaluation:
            db.insert_evaluation(tuple(record))

