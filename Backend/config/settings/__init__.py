import os

# Detect the environment based on an environment variable
ENVIRONMENT = os.environ.get('DJANGO_ENV', 'development')

# Import the corresponding settings file
if ENVIRONMENT == 'production':
    from .production import *
else:
    from .development import *
