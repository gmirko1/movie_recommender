from database.database_queries import get_all_books
from helpers import user_validation

def _get_all_books():
    try:
        check_user = user_validation._user_validation()
        
        if check_user:
            books = get_all_books._get_all_books()
           
            return books
        else:
            return None
    except Exception as ex:
        print(ex)
        return None
