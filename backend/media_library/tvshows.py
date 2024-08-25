from database.database_queries import get_all_tvshows
from helpers import user_validation

def _get_all_tvshows():
    try:
        check_user = user_validation._user_validation()
        
        if check_user:
            tv_shows = get_all_tvshows._get_all_tvshows()
           
            return tv_shows
        else:
            return None
    except Exception as ex:
        print(ex)
        return None
