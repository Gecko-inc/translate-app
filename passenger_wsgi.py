# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, '/var/www/u1433011/data/www/translate-app')
sys.path.insert(1, '/var/www/u1433011/data/www/translate-app/env/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_template.settings'
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
