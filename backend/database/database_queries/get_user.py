from database import db_config
import mysql.connector

def _get_user(user_email, password_hashed):
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        sql_login = "SELECT * FROM users WHERE user_email =%s AND user_password=%s  "
        var = (user_email, password_hashed)
        cursor.execute(sql_login, var)
        user = cursor.fetchone()
        db.commit()
        return user
    except Exception as ex:
        print(ex)
        return None
    finally:
        db.close()


    
    
