"""
> pip install python-dotenv
"""
import logging

import dotenv

# Required vars use direct key access
# Optional vars use .get() with sensible default

# Read in variables defined in our environment file
env_vars: dict = dotenv.dotenv_values('.env')

# Set application-wide variables here to be imported

# Authentication variables
SUPER_SECRET_USERNAME = env_vars['SUPER_SECRET_USERNAME']
SUPER_SECRET_PASSWORD = env_vars['SUPER_SECRET_PASSWORD']

# Setup Logging
LOG_FILE = env_vars.get('LOG_FILE', 'root.log')
LOGGING_LEVEL = env_vars.get('LOGGING_LEVEL', 'INFO')
logging.basicConfig(
    filename=LOG_FILE,
    level=LOGGING_LEVEL
)
