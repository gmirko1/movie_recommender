import jwt
from . import g_keys

def _generate_token(email):
    try:
        jwt_payload = {'email': email}
        token = jwt.encode(jwt_payload, g_keys.SECRET_KEY, algorithm='HS256')
        return token

    except Exception as ex:
        print(ex)
        return None