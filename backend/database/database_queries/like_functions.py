
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

def _get_likes_movies(user_id):
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        sql_like = """
            SELECT movies.*, 1 AS is_favorite
            FROM movies
            WHERE movies.movie_id IN (
                SELECT movie_id FROM like_movie WHERE user_id = %s
            )
        """
        var = (user_id,)
        cursor.execute(sql_like, var)
        liked_movies = cursor.fetchall()
        print(liked_movies)
        return liked_movies

    except Exception as ex:
        print(ex)
        return None

def _get_likes_tvshows(user_id):
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        sql_like = """
            SELECT tv_shows.*, 1 AS is_favorite
            FROM tv_shows
            WHERE tv_shows.tvshow_id IN (
                SELECT tvshow_id FROM like_tvshow WHERE user_id = %s
            )
        """
        var = (user_id,)
        cursor.execute(sql_like, var)
        liked_tvshows = cursor.fetchall()
        print(liked_tvshows)
        return liked_tvshows

    except Exception as ex:
        print(ex)
        return None

def _get_likes_books(user_id):
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        sql_like = """
            SELECT books.*, 1 AS is_favorite
            FROM books
            WHERE books.book_id IN (
                SELECT book_id FROM like_books WHERE user_id = %s
            )
        """
        var = (user_id,)
        cursor.execute(sql_like, var)
        liked_books = cursor.fetchall()
        print(liked_books)
        return liked_books

    except Exception as ex:
        print(ex)
        return None
    

  





    
    
