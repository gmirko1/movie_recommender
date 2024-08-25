

from database import db_config
import mysql.connector

def _get_all_movies():
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        sql_login = "SELECT * FROM movies "
        cursor.execute(sql_login)
        movies = cursor.fetchall()
        db.commit()
        return movies
    except Exception as ex:
        print(ex)
        return None
    finally:
        db.close()


    
    
