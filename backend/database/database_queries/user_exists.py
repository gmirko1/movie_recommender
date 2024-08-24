from database import db_config
import mysql.connector


def _user_exist(user_email):
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        sql_user_exist = """ SELECT * FROM users WHERE user_email = %s"""
        var = (user_email,)
        cursor.execute(sql_user_exist, var)
        user_exist = cursor.fetchone()
        db.commit()
        return user_exist
    except Exception as ex:
        print(ex)
        return str(ex)
    finally:
        db.close()