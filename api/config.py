import os, random, string
from datetime import timedelta
from typing import Optional

class BaseConfig():
    '''App secrets configs / settings'''
    
    SECRET_KEY: Optional[str | None] = os.getenv('SECRET_KEY', None)
    if not SECRET_KEY:
        SECRET_KEY: str = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 64 ))

    SWAGGER_VALIDATOR_URL: str = 'http://localhost:5000/docs'#'http://domain.com/validator'