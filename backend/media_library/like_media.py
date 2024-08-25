from flask import request, make_response
from database.database_queries import like_functions
from helpers import user_validation

def _like_tvshow():
    try:
        check_user = user_validation._user_validation()
        user_id = check_user[0]
        request_media_id = request.json
        media_id = request_media_id["tvShowID"]
        
        like_functions._like_tvshow(user_id, media_id)
        resp = make_response('Tv show is liked')
        return resp
    except Exception as ex:
        print(ex)
        return None

def _like_movie():
    try:
        check_user = user_validation._user_validation()
        user_id = check_user[0]
        request_media_id = request.json
        media_id = request_media_id["movieID"]
        
        like_functions._like_movie(user_id, media_id)
        resp = make_response('Movie is liked')
        return resp
    except Exception as ex:
        print(ex)
        return None
    


def _like_book():
    try:
        check_user = user_validation._user_validation()
        user_id = check_user[0]
        request_media_id = request.json
        media_id = request_media_id["bookID"]
        
        like_functions._like_book(user_id, media_id)
        resp = make_response('Book is liked')
        return resp
    except Exception as ex:
        print(ex)
        return None