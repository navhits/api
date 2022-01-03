import os
import abc

from fastapi.security import APIKeyHeader
from fastapi import Security
from fastapi.exceptions import HTTPException
from starlette import status

API_TOKEN = os.getenv('API_TOKEN')

api_key = APIKeyHeader(name='x-api-key', auto_error=False)

class Auth:
    def is_valid_api_key(self, creds):
        if creds == API_TOKEN:
            return True
        return False
    
    @abc.abstractmethod
    def authenticate(self):
        pass

    
class APIKeyAuth(Auth):
    keyword = 'x-api-key'
    auth_error = "API Key error"
    
    def authenticate(self, creds: str = Security(api_key)):
        if creds:
            if self.is_valid_api_key(creds):
                return True
            else:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=self.auth_error, 
                    headers={'WWW-Authenticate': self.keyword})
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=self.auth_error, 
                    headers={'WWW-Authenticate': self.keyword})
