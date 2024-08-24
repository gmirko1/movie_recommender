from flask import make_response

from database import db_config
import mysql.connector
 
def _save_user(user_id,user_email, user_password ):
    try:
        db_config_get = db_config._db_config()
        db = mysql.connector.connect(**db_config_get)
        cursor = db.cursor()
        
        sql_save_user  = "INSERT INTO users (user_id, user_email, user_password) VALUES ( %s, %s, %s)"
        var = (user_id, user_email, user_password,)
        cursor.execute(sql_save_user, var)
        
        db.commit()
        

    except Exception as ex:
        print(ex)
        return None
   
    
                                
            
