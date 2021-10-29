from typing import Dict
import jwt 
import time

jwt_secret = b'deff1952d59f883ece260e8683fed21ab0ad9a53323eca4f'
jwt_algorithm = "HS256"

def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(user_id : str) -> Dict[str,str]:
    payload = {
        "id" : user_id,
        "expires" : time.time() + 18000
    }
    token = jwt.encode(payload , jwt_secret , algorithm = jwt_algorithm)
    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, jwt_secret, algorithms=[jwt_algorithm])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
