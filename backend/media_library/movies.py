from database.database_queries import get_all_movies
from helpers import user_validation

def _get_all_movies():
    try:
        check_user = user_validation._user_validation()
        
        if check_user:
            movies = get_all_movies._get_all_movies()
           
            return movies
        else:
            return None
    except Exception as ex:
        print(ex)
        return None
