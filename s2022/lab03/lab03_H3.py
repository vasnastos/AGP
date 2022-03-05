# Movielens
from Movie_Lens.movies_load import MovieLen

if __name__=='__main__':
    movielen=MovieLen()

    # upload to mysql database
    # movielen.upload()
    
    # Users evaluate the movie must be above 10 and evaluation score of movie must be over 2.6
    movielen.filter_movies(users_minimum_number=10,evaluation_score=2.6)
   
    # Print movie info
    movielen.info()
    print('\n\nTop 10 Movies')

    # Print top 10 movies
    movielen.top_10()