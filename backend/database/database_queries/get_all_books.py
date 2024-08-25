

from database import db_config
import mysql.connector

def _get_all_books():
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        sql_login = "SELECT * FROM books "
        cursor.execute(sql_login)
        books = cursor.fetchall()
        db.commit()
        return books
    except Exception as ex:
        print(ex)
        return None
    finally:
        db.close()


    
    
