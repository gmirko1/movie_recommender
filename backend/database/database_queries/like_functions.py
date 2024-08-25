
from database import db_config
import mysql.connector


def _like_tvshow(user_id, media_id):
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        sql_like = "INSERT INTO like_tvshow (user_id, tvshow_id) VALUES (%s,%s)"
        var = (user_id, media_id,)
        cursor.execute(sql_like, var)
        db.commit()
    except Exception as ex:
        print(ex)
        return None

def _like_movie(user_id, media_id):
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        sql_like = "INSERT INTO like_movie (user_id, movie_id) VALUES (%s,%s)"
        var = (user_id, media_id,)
        cursor.execute(sql_like, var)
        db.commit()
    except Exception as ex:
        print(ex)
        return None

def _like_book(user_id, media_id):
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        sql_like = "INSERT INTO like_books (user_id, book_id) VALUES (%s,%s)"
        var = (user_id, media_id,)
        cursor.execute(sql_like, var)
        db.commit()
    except Exception as ex:
        print(ex)
        return None
    





    
    
