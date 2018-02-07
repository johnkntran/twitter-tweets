"""
Configuration file: This file goes somewhere in your PYTHONPATH on your server, 
such as /Library/python/2.7/site-packages/.
"""

import sys

# Change this to the directory where your scripts are served on the webserver.
EXECUTABLES_DIR = "/var/www/wsgi-scripts"

# This controls whether requests are sent through HTTPS or HTTP
USE_HTTPS = True

sys.path.append(EXECUTABLES_DIR)
