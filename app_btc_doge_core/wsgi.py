import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_btc_doge_core.settings')

application = get_wsgi_application()
