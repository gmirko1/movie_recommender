from . import database_connection


def _db_config():
    
    db_config = database_connection.DEVELOPMENT_CONN
    return db_config