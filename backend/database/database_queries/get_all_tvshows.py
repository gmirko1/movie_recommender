

from database import db_config
import mysql.connector

def _get_all_tvshows():
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        sql_login = "SELECT * FROM tv_shows "
        cursor.execute(sql_login)
        tv_shows = cursor.fetchall()
        db.commit()
        return tv_shows
    except Exception as ex:
        print(ex)
        return None
    finally:
        db.close()


    
    
